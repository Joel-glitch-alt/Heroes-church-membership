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
