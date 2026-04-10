📘 Heroes Summit Member Registration API

A Django-based web application for managing church member registrations, including referral tracking, REST API support, admin tools, and PostgreSQL database integration.

🚀 Features
Member registration system
Self-referential referral system (invited_by)
REST API built with Django REST Framework
PostgreSQL database integration (migrated from SQLite/SQL)
Admin dashboard with:
Excel import/export
PDF export (ReportLab)
Input validation and data cleaning
Simple frontend form (HTML, CSS, JS)

🧱 Tech Stack
Backend: Django 5.x
API: Django REST Framework
Database: PostgreSQL (via psycopg2)
Admin Tools: django-import-export
PDF Export: ReportLab
Config Management: python-decouple

🗃️ Database Migration (SQL → PostgreSQL)

This project was originally configured with a default SQL database (SQLite) and has been migrated to PostgreSQL for better scalability and production readiness.


✅ PostgreSQL Configuration

Update your settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

✅ Required Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

✅ Install PostgreSQL Driver
pip install psycopg2-binary
✅ Apply Migrations
python manage.py makemigrations
python manage.py migrate

📦 Installation
Clone the repository
git clone https://github.com/Joel-glitch-alt/heroes-summit.git
cd heroes-summit
Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
Install dependencies
pip install -r requirements.txt

Configure environment variables

Create .env as shown above.

Run migrations
python manage.py migrate
Start development server
python manage.py runserver

runserver
🔌 API Endpoints

Base URL:

http://127.0.0.1:8000/api/
Members
Method	Endpoint	Description
GET	/members/	List all members
POST	/members/	Create a new member
GET	/members/{id}/	Retrieve a member
PUT	/members/{id}/	Update a member
DELETE	/members/{id}/	Delete a member
🧩 Data Model
Member
class Member(models.Model):
    first_name
    last_name
    contact
    invited_by (self-referential FK)
    location
    date_joined
    created_at
Key Features
invited_by: Tracks referrals between members
full_name: Computed property
Ordered by newest (created_at)
✅ Validation Rules
Names cannot be blank and are title-cased
Contact:
Must be numeric
Ghana format normalization (e.g., 024xxxxxxx → 23324xxxxxxx)
Location cannot be empty
invited_by is optional
🧑‍💼 Admin Features

Accessible at:

/admin/
Capabilities
Search members
Filter by location and date
Pagination
Import/export via Excel
Export selected members to PDF
📄 PDF Export

Admins can export selected members as a PDF containing:

Full name
Contact
Location
Invited by
🌐 Frontend
Simple responsive registration form
Connects to API dynamically
Handles:
Validation
Submission
Success feedback
🔒 Security Notes
Uses environment variables for sensitive data
DEBUG should be set to False in production
Add production domain to ALLOWED_HOSTS
📌 Future Improvements
Authentication (JWT or session-based)
Pagination & filtering in API
Deployment (Render, Docker, etc.)
Email/SMS notifications
Dashboard analytics
👨‍💻 Author

Developed as part of a church member management system.
