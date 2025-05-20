from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as yasg_get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from employees.views import (
    HomeView, LoginView, LogoutView, WebRegisterView,
    EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,
    DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView
)

schema_view = yasg_get_schema_view(
   openapi.Info(
      title="Employee Management API",
      default_version='v1',
      description="API for managing employees and departments",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-alt'),

    # Authentication URLs
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', WebRegisterView.as_view(), name='register'),

    # Employee CRUD URLs
    path('employees/add/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),

    # Department CRUD URLs
    path('departments/add/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/edit/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),
]