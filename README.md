# Django-Boiler-Plate

A boilerplate Django project to kickstart your web development with Django. This template provides a clean, modular, and scalable structure for building robust Django applications.

## Features

- Django 4.x+ ready
- Modular app structure
- Environment-based settings (development/production)
- Pre-configured static and media file handling
- User authentication (login, logout, registration)
- Example app included
- Ready for deployment (Gunicorn, WhiteNoise, etc.)
- Docker support (if Dockerfile is present)
- Pre-configured for PostgreSQL (can be switched to SQLite/MySQL)
- Custom user model (if implemented)
- Sample templates and static files

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)
- PostgreSQL (or SQLite for development)
- [Optional] Docker

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/samirpatil2000/Django-Boiler-Plate.git
    cd Django-Boiler-Plate
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
    - Copy `.env.example` to `.env` and update values as needed.

5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the app:**
    - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
