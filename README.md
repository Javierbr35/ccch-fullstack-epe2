# Comunidad Científica de Chile (CCCh) - Full-Stack (EPE2)

Plataforma web con arquitectura desacoplada **Angular + Django + PostgreSQL 18**.

## Guía de instalación para continuar el desarrollo

1. **Base de datos:** Crear una base vacía llamada `ccch_db` en PostgreSQL 18.
2. **Backend (Django):**

       cd backend-django
       copy .env.example .env
       python -m venv venv
       .\venv\Scripts\activate
       pip install -r requirements.txt
       python manage.py migrate
       python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@ccch.cl', 'admin123')"
       python poblar_orm.py
       python manage.py runserver

3. **Frontend (Angular, en otra terminal):**

       cd frontend-angular
       npm install
       npm start

## Accesos locales
- **Frontend:** `http://localhost:4200/`
- **Panel Admin Django:** `http://127.0.0.1:8000/admin/` (Usuario: `admin` / Contraseña: `admin123`)

