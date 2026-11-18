# Comunidad Científica de Chile (CCCh) — Manual Técnico Full-Stack (EPE2)

Plataforma web con arquitectura desacoplada **Angular + Python/Django + PostgreSQL 18**.

## 1. Arquitectura
- **backend-django/**: API REST (GET/POST), modelos ORM, poblar_orm.py y Panel Admin.
- **frontend-angular/**: SPA interactiva en TypeScript, Signals y componentes modulares.

## 2. Instalación en cualquier PC (Paso a Paso)

### Paso 1: Clonar repositorio
    git clone https://github.com/Javierbr35/ccch-fullstack-epe2.git
    cd ccch-fullstack-epe2

### Paso 2: Base de datos PostgreSQL 18
Crear una base de datos vacía llamada **ccch_db** en pgAdmin 4.

### Paso 3: Backend (Django)
    cd backend-django
    copy .env.example .env
    # Editar .env con tu contraseña local de PostgreSQL
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@ccch.cl', 'admin123')"
    python poblar_orm.py
    python manage.py runserver

### Paso 4: Frontend (Angular, en otra terminal)
    cd frontend-angular
    npm install
    npm start

## 3. Pruebas Realizadas y Verificación
1. **Lectura (GET):** Abrir http://localhost:4200/ y verificar carga de Científicos/as y Vitrina desde PostgreSQL.
2. **Interactividad:** Probar filtros en Ciencia Accesible, buscador en Bolsa de Trabajo, Foro y acordeón FAQ.
3. **Escritura (POST):** Enviar formulario en Únete a la comunidad o Conversemos y verificar confirmación.
4. **Auditoría Admin:** Ingresar a http://127.0.0.1:8000/admin/ (admin / admin123) y revisar Solicitudes de la Comunidad.