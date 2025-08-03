# Django REST API Boilerplate

A clean Django REST API boilerplate with JWT authentication, custom user model, and essential endpoints to kickstart your project.

## Features

- Django 4.2.23 + Django REST Framework
- JWT Authentication with Simple JWT
- Custom User Model (email-based login)
- User registration, login, and profile management
- Password reset functionality
- CORS support
- Docker support

## Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone and setup
git clone https://github.com/samirpatil2000/django-boiler-plate.git
cd django-boiler-plate
cp .env.example .env

# Run with Docker
docker-compose up --build

# Setup database
docker exec -it backend python manage.py migrate
docker exec -it backend python manage.py createsuperuser
```

### Option 2: Local Setup

```bash
# Clone and setup
git clone https://github.com/samirpatil2000/django-boiler-plate.git
cd django-boiler-plate

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies and setup
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Endpoints

**Base URL:** `http://127.0.0.1:8000/account/`

### Authentication
- `POST /register` - Register new user
- `POST /login` - Login and get JWT token
- `POST /token/refresh` - Refresh JWT token
- `GET /register` - Get user profile (requires auth)

### Password Management
- `GET /password-reset` - Request password reset
- `GET /password-reset-confirm/<uidb64>/<token>` - Confirm reset
- `GET /password_change` - Change password form

## Usage Examples

### Register User
```bash
curl -X POST http://127.0.0.1:8000/account/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepass123",
    "password2": "securepass123",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Login
```bash
curl -X POST http://127.0.0.1:8000/account/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepass123"
  }'
```

### Access Protected Endpoint
```bash
curl -X GET http://127.0.0.1:8000/account/register \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Project Structure

- **Custom User Model**: Email-based authentication instead of username
- **JWT Authentication**: Secure token-based authentication
- **Modular Design**: Clean separation of concerns
- **API-First**: RESTful API architecture

## Database Configuration

The project supports both PostgreSQL and SQLite3 databases. Configure via the `DB_ENGINE` environment variable in your `.env` file:

**SQLite3 (Default):**
```env
DB_ENGINE=sqlite3
```

**PostgreSQL:**
```env
DB_ENGINE=postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

## Development

```bash
# Run tests
python manage.py test

# Access admin panel
http://127.0.0.1:8000/admin/
```

## Deployment

1. Set `DEBUG = False` in settings
2. Configure production database (PostgreSQL/MySQL)
3. Set up environment variables in `.env`
4. Configure static files and HTTPS
5. Update CORS settings for your domain

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details.
