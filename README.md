# Employee Management System

A Django REST API and web interface for managing employees and departments. This system provides a comprehensive solution for tracking employees, their departments, and related information.

## Live Demo

This project is hosted and available for use at:
**[https://greymatter.pythonanywhere.com/](https://greymatter.pythonanywhere.com/)**

### Demo Access
- **Web Interface**: [https://greymatter.pythonanywhere.com/](https://greymatter.pythonanywhere.com/)
- **Admin Interface**: [https://greymatter.pythonanywhere.com/admin/](https://greymatter.pythonanywhere.com/admin/)
- **API Documentation**:
  - [https://greymatter.pythonanywhere.com/redoc/](https://greymatter.pythonanywhere.com/redoc/)
  - [https://greymatter.pythonanywhere.com/swagger/](https://greymatter.pythonanywhere.com/swagger/)

### Demo Credentials
- **Username**: admin
- **Password**: admin

You can use these credentials to log in and explore all features, including CRUD operations on Employees and Departments directly from the web interface or admin panel.

## Features

- **Authentication System**
  - User registration and login functionality
  - Token-based authentication for API access
  - Session-based authentication for web interface

- **Web Interface**
  - Responsive Bootstrap 5 UI with modern design
  - Dashboard showing employees and departments
  - Direct CRUD operations from the web interface:
    - Add, edit, and delete employees
    - Add, edit, and delete departments
  - User-friendly forms with validation
  - Mobile-responsive design

- **API Features**
  - RESTful API for Employees and Departments
  - Token-based authentication
  - Comprehensive API documentation with Swagger and ReDoc
  - Filtering and search capabilities
  - Secure endpoints with proper authentication

- **Admin Interface**
  - Django admin interface for advanced management
  - User management
  - Data export/import capabilities

## Technology Stack

- **Backend**
  - Django 5.2.1 - Python web framework
  - Django REST Framework 3.16.0 - API toolkit
  - drf-yasg - Swagger/OpenAPI documentation generator

- **Frontend**
  - Bootstrap 5.3 - CSS framework for responsive design
  - HTML5 & CSS3 - Frontend markup and styling
  - JavaScript - Client-side interactivity
  - Bootstrap Icons - Icon library

- **Database**
  - SQLite (default) - Development database
  - Can be configured for PostgreSQL, MySQL, or other databases for production

- **Authentication**
  - Django's built-in authentication system
  - Token-based authentication for API
  - Session-based authentication for web interface

- **Development Tools**
  - Git - Version control
  - Django Debug Toolbar (optional) - Development debugging

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd employee_mgmt
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On Linux/macOS
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   # Apply migrations
   python manage.py migrate

   # Load initial data (optional)
   python manage.py loaddata initial_data.json  # If you have fixture data
   ```

5. **Create a superuser for admin access**
   ```bash
   python manage.py createsuperuser
   # Follow the prompts to create an admin user
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application locally**
   - Web Interface: http://127.0.0.1:8000/
   - Admin Interface: http://127.0.0.1:8000/admin/
   - API Documentation:
     - ReDoc: http://127.0.0.1:8000/redoc/
     - Swagger UI: http://127.0.0.1:8000/swagger/

   > **Note**: These are local URLs when running the development server. For the live demo, use the URLs mentioned in the [Live Demo](#live-demo) section.

### Configuration (Optional)

- **Environment Variables**: Create a `.env` file in the project root for environment-specific settings
- **Database Configuration**: Edit `settings.py` to configure a different database backend
- **Email Configuration**: Configure email settings in `settings.py` for password reset functionality

## API Endpoints

The API is available at both the live demo site and locally when running the development server.

- **Live API Base URL**: `https://greymatter.pythonanywhere.com/api/`
- **Local API Base URL**: `http://127.0.0.1:8000/api/` (when running locally)

### Authentication

- **Register User**: `POST /api/auth/register/`
  - Example:
    - Live: `https://greymatter.pythonanywhere.com/api/auth/register/`
    - Local: `http://127.0.0.1:8000/api/auth/register/`
  - Request Body: `{"name": "username", "email": "user@example.com", "password": "password"}`
  - Response: `{"token": "auth-token", "user_id": 1, "email": "user@example.com"}`

- **Get Auth Token**: `POST /api/auth/token/`
  - Example:
    - Live: `https://greymatter.pythonanywhere.com/api/auth/token/`
    - Local: `http://127.0.0.1:8000/api/auth/token/`
  - Request Body: `{"username": "username", "password": "password"}`
  - Response: `{"token": "auth-token", "user_id": 1, "email": "user@example.com"}`

### Employees

- **List Employees**: `GET /api/employees/`
  - Headers: `Authorization: Token <auth-token>`
  - Response: List of employee objects

- **Get Employee by ID**: `GET /api/employees/{id}/`
  - Headers: `Authorization: Token <auth-token>`
  - Response: Employee object

- **Create Employee**: `POST /api/employees/`
  - Headers: `Authorization: Token <auth-token>`
  - Request Body: `{"employee_id": "1", "name": "John Doe", "email": "john@example.com", "designation": "Developer", "department": 1}`
  - Response: Created employee object

- **Update Employee**: `PUT /api/employees/{id}/`
  - Headers: `Authorization: Token <auth-token>`
  - Request Body: `{"employee_id": "1", "name": "John Doe", "email": "john@example.com", "designation": "Senior Developer", "department": 1}`
  - Response: Updated employee object

- **Delete Employee**: `DELETE /api/employees/{id}/`
  - Headers: `Authorization: Token <auth-token>`
  - Response: 204 No Content

### Departments

- **List Departments**: `GET /api/departments/`
  - Headers: `Authorization: Token <auth-token>`
  - Response: List of department objects

- **Get Department by ID**: `GET /api/departments/{id}/`
  - Headers: `Authorization: Token <auth-token>`
  - Response: Department object

- **Create Department**: `POST /api/departments/`
  - Headers: `Authorization: Token <auth-token>`
  - Request Body: `{"department_id": "1", "name": "Engineering"}`
  - Response: Created department object

- **Update Department**: `PUT /api/departments/{id}/`
  - Headers: `Authorization: Token <auth-token>`
  - Request Body: `{"department_id": "1", "name": "Engineering & Development"}`
  - Response: Updated department object

- **Delete Department**: `DELETE /api/departments/{id}/`
  - Headers: `Authorization: Token <auth-token>`
  - Response: 204 No Content

> **Note**: For testing the API, you can use tools like Postman or cURL. The Swagger UI and ReDoc documentation provide interactive interfaces to explore and test the API endpoints.

## Web Interface

The web interface provides a user-friendly way to manage employees and departments. It's available both on the live demo site and locally when running the development server.

### Authentication Pages

- **Login Page**:
  - Live: [https://greymatter.pythonanywhere.com/login/](https://greymatter.pythonanywhere.com/login/)
  - Local: http://127.0.0.1:8000/login/ (when running locally)
  - User authentication with username and password
  - Link to registration page for new users

- **Register Page**:
  - Live: [https://greymatter.pythonanywhere.com/register/](https://greymatter.pythonanywhere.com/register/)
  - Local: http://127.0.0.1:8000/register/ (when running locally)
  - New user registration with username, email, and password
  - Validation to prevent duplicate usernames/emails

- **Logout**:
  - Live: [https://greymatter.pythonanywhere.com/logout/](https://greymatter.pythonanywhere.com/logout/)
  - Local: http://127.0.0.1:8000/logout/ (when running locally)

### Dashboard

- **Home/Dashboard**:
  - Live: [https://greymatter.pythonanywhere.com/](https://greymatter.pythonanywhere.com/)
  - Local: http://127.0.0.1:8000/ (when running locally)
  - Overview of all employees and departments
  - Quick access buttons for all CRUD operations
  - Responsive layout that works on mobile devices

### Employee Management

- **Add Employee**:
  - Live: [https://greymatter.pythonanywhere.com/employees/add/](https://greymatter.pythonanywhere.com/employees/add/)
  - Local: http://127.0.0.1:8000/employees/add/ (when running locally)
  - Form to create new employees
  - Dropdown to select department

- **Edit Employee**:
  - Live: https://greymatter.pythonanywhere.com/employees/{id}/edit/
  - Local: http://127.0.0.1:8000/employees/{id}/edit/ (when running locally)
  - Form to update existing employee details

- **Delete Employee**:
  - Live: https://greymatter.pythonanywhere.com/employees/{id}/delete/
  - Local: http://127.0.0.1:8000/employees/{id}/delete/ (when running locally)
  - Confirmation page before deletion

### Department Management

- **Add Department**:
  - Live: [https://greymatter.pythonanywhere.com/departments/add/](https://greymatter.pythonanywhere.com/departments/add/)
  - Local: http://127.0.0.1:8000/departments/add/ (when running locally)
  - Form to create new departments

- **Edit Department**:
  - Live: https://greymatter.pythonanywhere.com/departments/{id}/edit/
  - Local: http://127.0.0.1:8000/departments/{id}/edit/ (when running locally)
  - Form to update existing department details

- **Delete Department**:
  - Live: https://greymatter.pythonanywhere.com/departments/{id}/delete/
  - Local: http://127.0.0.1:8000/departments/{id}/delete/ (when running locally)
  - Confirmation page before deletion

## Models

### Employee

- `employee_id`: Unique identifier for the employee
- `name`: Employee's full name
- `email`: Employee's email address (unique)
- `department`: Foreign key to Department
- `designation`: Employee's job title or position
- `date_joined`: Date when the employee joined

### Department

- `department_id`: Unique identifier for the department
- `name`: Department name

## Web-based CRUD Operations

One of the key features of this application is the ability to perform CRUD operations directly from the web interface without needing to use the Django admin site.

> **Try it live**: You can try these CRUD operations on the live demo at [https://greymatter.pythonanywhere.com/](https://greymatter.pythonanywhere.com/) using the demo credentials provided in the [Live Demo](#live-demo) section.

### Employee Management
- **Create**: Click the "+" button in the Employee List header to add a new employee
- **Read**: All employees are displayed on the dashboard with their details
- **Update**: Click the edit (pencil) icon next to any employee to modify their details
- **Delete**: Click the delete (trash) icon next to any employee to remove them

### Department Management
- **Create**: Click the "+" button in the Departments header to add a new department
- **Read**: All departments are displayed on the dashboard
- **Update**: Click the edit (pencil) icon next to any department to modify its details
- **Delete**: Click the delete (trash) icon next to any department to remove it

## Security Features

- **Authentication Required**: All CRUD operations require user authentication
- **CSRF Protection**: All forms are protected against Cross-Site Request Forgery
- **Form Validation**: Input validation on all forms to prevent invalid data
- **Secure Password Handling**: Passwords are securely hashed and never stored in plaintext

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django and Django REST Framework communities
- Bootstrap team for the excellent UI framework
- All contributors who have helped improve this project
