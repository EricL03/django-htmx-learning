# Django and htmx learnings

## 1. Installation & Setup

### Installing Django
#### Prerequisites
Before installing Django, ensure you have the following installed:

- **Python** (Recommended version: 3.10+)

#### Installation steps
Use python3 instead of python for MacOS and Linux!

1. **Create a virtual environment**
```sh
python -m venv venv
```
2. **Activate the virtual environment:**
* MacOS and Linux
```sh
source venv/bin/activate
```
* Windows
```sh
venv\Scripts\activate
```
2.1. **Deactivate the virtual environment:**
```sh
deactivate
```
### **Warning: From here on the virtual environment needs to be activated!**
If the virtual environment is deactivate or the terminal is restarted the 
venv needs to be activated again!

3. **Upgrade/install pip:**
```sh
python -m pip install --upgrade pip
```
4. **Install required packages:**
```sh
python -m pip install django
```
5. **Verify installation:**
```sh
django-admin --version
```


## 2. Project Initialization
Make sure to replace all instances of "myproject" and "myapp" with you desired names!

### Creating a Django Project
1. **Create a new Django project:**
```sh
django-admin startproject myproject
```
2. **Navigate into the project directory:**
```sh
cd myproject
```
3. **Start a new Django app:**
```sh
python manage.py startapp myapp
```
4. **Register the app in myproject/settings.py**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```
### Configuring Static Files
1. **Create directories for static files and templates:**
**Warning: This does not work on windows, create the directories manually istead!**
```sh
mkdir -p myapp/static myapp/templates
```
2. **Update settings.py to use these directories:**
```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "myapp", "static"),
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "myapp", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
### Setting Up HTMX
1. **Include HTMX in the index HTML file:**
Create myapp/templates/index.html and include the HTMX script:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Django App</title>
    <script src="https://unpkg.com/htmx.org@1.9.2"></script>
</head>
<body>
    <h1>Hello world!</h1>
    <p>This paragraph contains valuable information!</p>
    <button>This is a button :)</button>
</body>
</html>
```
### Running the Development Server
Start the Django development server:
```sh
python manage.py runserver
```
Now, you can visit http://127.0.0.1:8000/ to see the standard django welcome page! 


## 3. Building Features (Using Django with HTMX, database integration, etc.)

### Setup basic routes
1. **Render index.html file by modifying myapp/views.py**
```python
def index(request):
    return render(request, "index.html")
```
2. **Create a myapp/urls.py file and add the following:**
```python
from django.urls import path
from .views import index

urlpatterns = [
    path("", index, name="name"),
]
```
3. **Add the myapp urls to myproject/urls.py:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),  # Includes URLs from myapp
]
```
### Run you index page
1. **Migrate database changes:**
```sh
python manage.py migrate
```
2. **Run the website:**
```sh
python manage.py runserver
```


## 4. Deployment & Best Practices

### Create an admin user and log in to the admin panel
1. **Run the following command and follow the prompts to enter a username, email, and password:**
```sh
python manage.py createsuperuser
```
2. **Run the server:**
```sh
python manage.py runserver
```
3. **Open your browser and go to:**
```sh
http://127.0.0.1:8000/admin/
```
4. **Enter the username and password you set for the admin user**
