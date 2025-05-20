from rest_framework import viewsets, status, views
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing employees.

    list:
    Return a list of all employees.

    create:
    Create a new employee.

    retrieve:
    Return the given employee.

    update:
    Update the given employee.

    partial_update:
    Partially update the given employee.

    destroy:
    Delete the given employee.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing departments.

    list:
    Return a list of all departments.

    create:
    Create a new department.

    retrieve:
    Return the given department.

    update:
    Update the given department.

    partial_update:
    Partially update the given department.

    destroy:
    Delete the given department.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class CustomAuthToken(ObtainAuthToken):
    """
    API endpoint for obtaining an authentication token.

    post:
    Create a new authentication token for the given user.
    """
    permission_classes = [AllowAny]  # Allow anyone to get a token

    def post(self, request, *args, **kwargs):
        """
        Create a new authentication token for the given user.
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(views.APIView):
    """
    API endpoint for registering a new user.

    post:
    Create a new user and return an authentication token.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Create a new user and return an authentication token.

        Parameters:
        - name: Username for the new user
        - email: Email address for the new user
        - password: Password for the new user

        Returns:
        - token: Authentication token for the new user
        - user_id: ID of the new user
        - email: Email address of the new user
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeView(View):
    """
    View for the home page that displays employees and departments
    """
    def get(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return redirect('login')

        # Get all employees and departments
        employees = Employee.objects.all()
        departments = Department.objects.all()

        # Render the template with context
        return render(request, 'index.html', {
            'employees': employees,
            'departments': departments
        })

class LoginView(View):
    """
    View for handling user login
    """
    def get(self, request):
        # If user is already authenticated, redirect to home
        if request.user.is_authenticated:
            return redirect('home')

        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    """
    View for handling user logout
    """
    def get(self, request):
        logout(request)
        return redirect('login')

class WebRegisterView(View):
    """
    View for handling user registration through web interface
    """
    def get(self, request):
        # If user is already authenticated, redirect to home
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, 'register.html')

    def post(self, request):
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Basic validation
        errors = {}
        if not name:
            errors['name'] = 'Username is required'
        if not email:
            errors['email'] = 'Email is required'
        if not password:
            errors['password'] = 'Password is required'

        # Check if username already exists
        if User.objects.filter(username=name).exists():
            errors['name'] = 'Username already exists'

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            errors['email'] = 'Email already exists'

        if errors:
            return render(request, 'register.html', {'form': errors})

        # Create user
        user = User.objects.create_user(username=name, email=email, password=password)

        # Create token (we don't need to use the token in the web interface)
        Token.objects.get_or_create(user=user)

        # Log the user in
        login(request, user)

        # Redirect to home
        return redirect('home')
