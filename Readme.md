# Hiring Test - FAQ Management System(Django)

This is a Django-based FAQ management system with multilingual support, WYSIWYG editor integration, and a REST API.

## Features
- **Multilingual Support**: FAQs can be translated into multiple languages (e.g., English, Hindi, Bengali).
- **WYSIWYG Editor**: Answers can be formatted using a rich text editor.
- **REST API**: Fetch FAQs in different languages using the API.
- **Caching**: Redis is used for caching to improve performance.
- **Admin Panel**: Manage FAQs easily using the Django admin interface.

## Installation

### Prerequisites
- Python 3.8+
- Redis (for caching)
- Django 5.0+

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hiring-test.git
   cd hiring-test

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Set up the database
   ```bash
   python manage.py migrate

4. Create a superuser
   ```bash
   python manage.py createsuperuser

5. Start the Redis server
   ```bash
   sudo service redis-server start

6. Run the development server
   ```bash
   python manage.py runserver

7. Access the admin panel
   ```bash
   http://localhost:8000/admin

## API Usage

### Fetch FAQs
- **Endpoint**: `/api/faqs/`
- **Query Parameters**:
  - `lang`: Language code (e.g., `en`, `hi`, `bn`). Defaults to `en`.

#### Example Requests
1. Fetch FAQs in English:
   ```bash
   http://localhost:8000/api/faqs/

2. Fetch FAQs in Hindi:
   ```bash
   http://localhost:8000/api/faqs/?lang=hi 

## 🛠️ Docker Setup 🐳

### 1️⃣ Build and Run the Docker Containers
```
docker-compose up --build
```

### 2️⃣ Stop the Containers
```
docker-compose down
```

---

## Linting and Code Formatting
1. To check for PEP8 compliance, run:
   ```bash
   flake8   

2. To automatically format the code, run:   
   ```bash
   black .
