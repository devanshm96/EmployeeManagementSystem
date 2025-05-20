# Employee Management System

A Django REST API and web interface for managing employees and departments. This system provides a comprehensive solution for tracking employees, their departments, and related information.

## Deployment

This project has been hosted at https://greymatter.pythonanywhere.com/

## Features

- Token-based authentication (login/register/logout)
- CRUD operations for Employees and Departments via RESTful API
- Responsive Bootstrap web UI for listing employees and departments
- Admin interface for managing data
- Filtering and search capabilities
- Secure API endpoints with token authentication

## Technology Stack

- **Backend**: Django 5.2.1, Django REST Framework 3.16.0
- **Database**: SQLite (default), can be configured for other databases
- **Frontend**: Bootstrap 5.3, HTML, CSS
- **Authentication**: Token-based authentication
- **Documentation**: drf-yasg for API documentation

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd employee_mgmt
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Web Interface: http://127.0.0.1:8000/
   - Admin Interface: http://127.0.0.1:8000/admin/
   - API Documentation: http://127.0.0.1:8000/redoc/

## API Endpoints

### Authentication

- **Register User**: `POST /api/auth/register/`
  - Request Body: `{"name": "username", "email": "user@example.com", "password": "password"}`
  - Response: `{"token": "auth-token", "user_id": 1, "email": "user@example.com"}`

- **Get Auth Token**: `POST /api/auth/token/`
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

## Web Interface

The web interface provides a user-friendly way to view employees and departments:

- **Login Page**: http://127.0.0.1:8000/login/
- **Home/Dashboard**: http://127.0.0.1:8000/
  - Displays a list of all employees with their details
  - Shows all departments
- **Logout**: http://127.0.0.1:8000/logout/

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

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
