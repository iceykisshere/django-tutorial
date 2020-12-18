# Django Blog Tutorial

### 0. Prep

* Sauce: Corey Schafer, https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
* handy utility to have: `tree`. 
* `django-admin` utility to see list of admin commands.
* run server: `python manage.py runserver`
* Access admin GUI: go to `localhost:8000/admin`
* The dir in which this README lives is *not* the root dir. The root dir to this project is actually `/django_project`. Notably, you'll call `manage.py` from within that dir.

### 1. Project-Level Config Files

* Start new project: `django-admin startproject name_of_project`. This creates a new dir which contains a number of project-level config files:

```
name_of_project
|__ __init__.py
|__ asgi.py
|__ settings.py
|__ urls.py # this is a "master" urls.py file. 
|__ wsgi.py
```

### 2. Basics

* create a new app (as in "app factory", I think): `python manage.py startapp $name_of_app`
* Parts of an app:
  * `views.py` - Views. Generically, routes. 
  * `urls.py` - Annoyingly, this must be manually created. This contains url routes that are usually decorators in Flask. Import the local `views.py`. So while flask handles routes and urls in one file, Django does this in two. The "master" `urls.py` will "import" all other module-level `urls.py` files with the `include()` function. 