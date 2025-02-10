# Lärdomar från django och htmx

## 1. Installation & Setup

### Installing Django
#### Prerequisites
Before installing Django, ensure you have the following installed:

- **Python** (Recommended version: 3.10+)
- **pip** (Python package manager)

#### Installation steps
Use python3 instead of python for MacOS and Linux!

1. **Upgrade/install pip:**
```sh
python -m pip install --upgrade pip
```
2. **Create a virtual environment**
```sh
python -m venv venv
```
3. **Activate the virtual environment:**
* MacOS and Linux
```sh
source venv/bin/activate
```
* Windows
```sh
venv\Scripts\activate
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
```sh
mkdir -p myapp/static myapp/templates
```
2. **Update settings.py to use these directories:**
```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'main/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
### Setting Up HTMX
1. **Include HTMX in the base HTML file:**
Create main/templates/index.html and include the HTMX script:
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
Now, you can visit http://127.0.0.1:8000/ to see the project running


## 3. Building Features (Using Django with HTMX, database integration, etc.)

## 4. Deployment & Best Practices
