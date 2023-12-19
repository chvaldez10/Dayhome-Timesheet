# Django Project Setup Guide

This guide provides step-by-step instructions for setting up a Django project with a MySQL database. We are using `django-environ` to manage environment variables.

## Prerequisites

Before you begin, ensure you have installed:

- Python (3.6 or higher)
- pip (Python package manager)
- MySQL Server
- Virtualenv (optional but recommended)

## Configuration

1. **Environment Variables:**

   - Create a `.env` file in the same directory as `settings.py`.
   - Add the following environment variables:
     ```
     DATABASE_NAME=your_db_name
     DATABASE_USER=your_db_user
     DATABASE_PASSWORD=your_db_password
     DATABASE_HOST=your_db_host  # localhost if running locally
     DATABASE_PORT=your_db_port  # default is 3306
     ```
   - Replace `your_db_name`, `your_db_user`, `your_db_password`, `your_db_host`, and `your_db_port` with your actual MySQL database details.

2. **Configure Django with `django-environ`:**

   - In your `settings.py`, configure the database settings:

     ```python
     import environ

     env = environ.Env()
     environ.Env.read_env()

     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': env('DATABASE_NAME'),
             'USER': env('DATABASE_USER'),
             'PASSWORD': env('DATABASE_PASSWORD'),
             'HOST': env('DATABASE_HOST'),
             'PORT': env('DATABASE_PORT'),
         }
     }
     ```

## Running the Project

1. **Migrate Database:**

   ```bash
   python manage.py migrate
   ```

2. **Create a Superuser (Optional):**

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   The server will start on http://127.0.0.1:8000/ by default.

## Additional Information

- Make sure to add `.env` to your `.gitignore` file to avoid committing sensitive data to version control.
- For deployment, ensure that your environment variables are securely configured on the production server.

---

This README is a basic template and can be customized further based on the specific requirements and features of your Django project.
