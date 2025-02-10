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


## 3. Building Features (Using Django with HTMX, database integration, etc.)

## 4. Deployment & Best Practices
