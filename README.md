# django-boiler-plate

A comprehensive Django REST API boilerplate project designed to kickstart your web development with Django and Django REST Framework. This template provides a clean, modular, and scalable structure for building robust Django applications with JWT-based authentication and RESTful APIs.

## 🚀 Features

- **Django 4.2.23** with Django REST Framework
- **JWT Authentication** using Simple JWT
- **Custom User Model** with email-based authentication
- **RESTful API Architecture** with comprehensive endpoints
- **CORS Support** for cross-origin requests
- **Modular App Structure** for scalability
- **Password Reset Functionality** with email templates
- **User Management APIs** with profile information
- **Ready for Production** deployment
- **Comprehensive API Documentation**

## 📋 Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)
- SQLite (default) or PostgreSQL/MySQL for production

## 🛠️ Installation & Setup

You can run this application either using traditional Python setup or Docker. Choose the method that best suits your development environment.

## 🐳 Docker Setup (Recommended)

### Prerequisites for Docker
- Docker
- Docker Compose

### 1. Clone the Repository
```bash
git clone https://github.com/samirpatil2000/django-boiler-plate.git
cd django-boiler-plate
```

### 2. Environment Configuration
Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

### 3. Build and Run with Docker Compose
```bash
docker-compose up --build
```

### 4. Database Setup (Docker)
Run migrations inside the Docker container:
```bash
docker exec -it backend python manage.py makemigrations
docker exec -it backend python manage.py migrate
```

### 5. Create Superuser (Docker)
```bash
docker exec -it backend python manage.py createsuperuser
```

### 6. Access the Application
- **API Base URL**: [http://127.0.0.1:8000/account/](http://127.0.0.1:8000/account/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🐍 Traditional Python Setup

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)
- SQLite (default) or PostgreSQL/MySQL for production

### 1. Clone the Repository
```bash
git clone https://github.com/samirpatil2000/django-boiler-plate.git
cd django-boiler-plate
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
- **API Base URL**: [http://127.0.0.1:8000/account/](http://127.0.0.1:8000/account/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000/account/
```

### Authentication
This API uses JWT (JSON Web Token) authentication. Include the token in the Authorization header:
```
Authorization: Bearer <your_access_token>
```

---

## 🔐 Authentication Endpoints

### 1. User Registration
**Endpoint:** `POST /account/register`

**Description:** Register a new user account

**Request Body:**
```json
{
    "email": "user@example.com",
    "password": "securepassword123",
    "password2": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
}
```

**Response (Success):**
```json
{
    "status": 200,
    "message": "successfully register",
    "data": {
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    }
}
```

**Response (Error):**
```json
{
    "status": 400,
    "message": "Email already exists",
    "data": {}
}
```

### 2. User Login
**Endpoint:** `POST /account/login`

**Description:** Authenticate user and receive JWT token

**Request Body:**
```json
{
    "email": "user@example.com",
    "password": "securepassword123"
}
```

**Response (Success):**
```json
{
    "status": 200,
    "message": "successfully login",
    "data": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
}
```

**Response (Error):**
```json
{
    "status": 400,
    "message": "Invalid credentials"
}
```

### 3. Token Refresh
**Endpoint:** `POST /account/token/refresh`

**Description:** Refresh JWT access token using refresh token

**Request Body:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

## 👤 User Management Endpoints

### 1. Get User Profile
**Endpoint:** `GET /account/register`

**Description:** Get authenticated user's profile information

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (Success):**
```json
{
    "status": 200,
    "message": "successfully register",
    "data": {
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    }
}
```

**Response (Unauthorized):**
```json
{
    "status": 403,
    "message": "Not Authenticated!",
    "data": {}
}
```

---

## 🔑 Password Management Endpoints

### 1. Password Reset Request
**Endpoint:** `GET /account/password-reset`

**Description:** Request password reset (renders template)

### 2. Password Reset Done
**Endpoint:** `GET /account/password-reset/done`

**Description:** Password reset email sent confirmation

### 3. Password Reset Confirm
**Endpoint:** `GET /account/password-reset-confirm/<uidb64>/<token>`

**Description:** Confirm password reset with token

### 4. Password Reset Complete
**Endpoint:** `GET /account/password-reset-complete`

**Description:** Password reset completion page

### 5. Password Change
**Endpoint:** `GET /account/password_change`

**Description:** Change password form (requires authentication)

### 6. Password Change Done
**Endpoint:** `GET /account/password_change/done`

**Description:** Password change confirmation

---

## 📊 Data Models

### Account Model
The custom user model with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `email` | EmailField | User's email address (unique, used for login) |
| `date_joined` | DateTimeField | Account creation timestamp |
| `last_login` | DateTimeField | Last login timestamp |
| `is_admin` | BooleanField | Admin privileges flag |
| `is_active` | BooleanField | Account active status |
| `is_staff` | BooleanField | Staff privileges flag |
| `is_superuser` | BooleanField | Superuser privileges flag |

---

## 🔧 Configuration

### Dependencies
The project uses the following key dependencies:

```txt
Django==4.2.23
djangorestframework==3.16.0
djangorestframework-simplejwt==5.5.1
django-cors-headers==4.7.0
PyJWT==2.10.1
```

### Settings Configuration
Key settings for the API:

- **Authentication**: JWT-based authentication
- **CORS**: Enabled for cross-origin requests
- **Database**: SQLite (default), configurable for PostgreSQL/MySQL
- **User Model**: Custom Account model with email authentication

---

## 🚀 Usage Examples

### cURL Examples
```bash
# Register
curl -X POST http://127.0.0.1:8000/account/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpass123",
    "password2": "testpass123",
    "first_name": "Test",
    "last_name": "User"
  }'

# Login
curl -X POST http://127.0.0.1:8000/account/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpass123"
  }'

# Get Profile (replace TOKEN with actual token)
curl -X GET http://127.0.0.1:8000/account/register \
  -H "Authorization: Bearer TOKEN"
```

---

## 🧪 Testing

### Run Tests
```bash
python manage.py test
```

### API Testing with Postman
1. Import the API endpoints into Postman
2. Set up environment variables for base URL and tokens
3. Test each endpoint with various scenarios

---

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings
- [ ] Configure production database (PostgreSQL/MySQL)
- [ ] Set up environment variables
- [ ] Configure static files serving
- [ ] Set up HTTPS
- [ ] Configure CORS settings for production domains

### Environment Variables
Create a `.env` file with:
```env
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
ALLOWED_HOSTS=your-domain.com
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact: [your-email@example.com]

---

## 🔄 Changelog

### Version 1.0.0
- Initial release with JWT authentication
- User registration and login APIs
- Password reset functionality
- Custom user model implementation
