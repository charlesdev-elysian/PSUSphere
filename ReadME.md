# 🎓 PSUSphere - Educational Institution Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A modern Django web platform revolutionizing educational administration through digital transformation.

## 🌟 Table of Contents
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Tech Stack](#-tech-stack)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Team](#-team)
- [License](#-license)

## ✨ Features

### 🏛️ Institutional Management
| Feature | Description |
|---------|-------------|
| College Dashboard | Centralized view of all colleges |
| Program Catalog | Manage academic programs |
| Department Setup | Organize by departments and faculties |

### 👥 Student Lifecycle
| Feature | Description |
|---------|-------------|
| Student Profiles | Complete academic/personal records |
| Enrollment System | Course registration workflow |
| Academic Tracking | Progress monitoring and reporting |

### 🏢 Organization Tools
```mermaid
graph TD
    A[Student] -->|Joins| B(Organization)
    B --> C[Events]
    B --> D[Members]
    B --> E[Documents]

### 🚀 Installation

Prerequisites
Python 3.10+

PostgreSQL 14+

Node.js (for frontend assets)

### Setup

# Clone repository
git clone https://github.com/charlesdev-elysian/PSUSphere.git
cd PSUSphere

# Initialize environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements/dev.txt

# Configure environment
cp .env.example .env
nano .env  # Edit configuration

### ⚙️ Configuration

# Sample settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'psusphere_db',
        'USER': 'admin',
        'PASSWORD': 'securepassword123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 💻 Usage
# Run development server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Run background tasks
celery -A core worker -l info

### 🔌 API Endpoints


Endpoint	Method	Description
/api/students/	GET	List all students
/api/colleges/	POST	Create new college
/api/enroll/	PUT	Update enrollment

### 🛠️ Tech Stack
Backend:

Django 4.2

Django REST Framework

Celery

Frontend:

Bootstrap 5

HTMX

Chart.js

Database:

PostgreSQL

Redis (caching)

### 🧑‍💻 Development

# Run linters
flake8 .
black --check .

# Generate requirements
pip freeze > requirements.txt

# DB migrations
python manage.py makemigrations
python manage.py migrate

### 🧪 Testing

# Run all tests
python manage.py test

# Generate coverage
coverage run manage.py test
coverage report -m

### 🚀 Deployment
# Production setup
pip install -r requirements/prod.txt

# Collect static
python manage.py collectstatic

# Gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:8000

###B 👥 Team


Role	Member	Contact
Lead Developer	Charles Jazon Dorero	@charlesdev
UI/UX Designer	Mark Oseas Eray	@markdesign

