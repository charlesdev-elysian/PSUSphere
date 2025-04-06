# 🎓 PSUSphere - Educational Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## 📌 Core Features
- **🏛️ College Management**: CRUD operations for institutions
- **🎓 Program Management**: Academic program administration
- **👥 Student Portal**: Records, enrollment, and tracking
- **🤝 Organization System**: Club management with membership tracking

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- Node.js 16+ (for frontend assets)

```bash
# Clone & Setup
git clone https://github.com/charlesdev-elysian/PSUSphere.git
cd PSUSphere
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Install & Configure
pip install -r requirements.txt
cp .env.example .env  # Edit with your credentials
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver