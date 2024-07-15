# Job Portal

This project is a Job Portal application developed using Django. It allows users to search for jobs, post job listings, and manage applications. The project is designed to help users find job opportunities and employers to find suitable candidates.

## Features

- Token-based user registration and authentication
- Job search functionality
- Job posting for employers
- Application management
- User profile management, including education, skills, projects, and experience
- Completely API-based functionality, tested using Postman

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

## Tree 
```
JobPortal/
├── JobPortal/
├── accounts/
├── LICENSE
├── README.md
└── requirements.txt
```

### Prerequisites

- Python (3.6, 3.7, 3.8, or 3.9)
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Abdullah00110/JobPortal.git
    cd JobPortal
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Django project:

    ```bash
    django-admin startproject JobPortal
    cd JobPortal
    python manage.py startapp accounts
    ```

5. Apply migrations and start the development server:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
6. requirements.txt
   ```
    Django>=3.2,<4.0
    djangorestframework
    djangorestframework-simplejwt
   ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

This project is completely API-based. You can use Postman to test the API endpoints.

### Registration

1. Send a POST request to `/jobportal/accounts/register/` with the user details to register a new user.
2. Upon successful registration, you will receive a token.

### Login

1. Send a POST request to `/jobportal/accounts/login/` with the user credentials.
2. Upon successful login, you will receive a token.

### Profile Management

Use the received token to perform the following actions:

- **Profile**: Create or update the user profile.
- **Education**: Add or update education details.
- **Skills**: Add or update skills.
- **Projects**: Add or update projects.
- **Experience**: Add or update experience.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## Contact

If you have any questions or feedback, please contact me at [abdullahsunasara6@gmail.com].

