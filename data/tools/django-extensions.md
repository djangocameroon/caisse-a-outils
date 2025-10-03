# Django Extensions

## Overview
Django Extensions adds a variety of management commands and utilities that improve productivity for developers.

## Key Features
- **shell_plus**: Enhanced interactive Python shell with all models pre-imported
- **graph_models**: Generate graphical representations of your models
- **runserver_plus**: Improved development server with debugger support
- **job scheduling**: Command to schedule periodic tasks
- **Export and import utilities**: Quick database inspection tools

## Installation
```bash
pip install django-extensions
```

Add to `INSTALLED_APPS` in `settings.py`:
```bash
INSTALLED_APPS += ["django_extensions"]
```

## Usage
Run shell with all models loaded
```bash
python manage.py shell_plus
```

Generate UML diagram of models
```bash
python manage.py graph_models -a -o my_project_models.png
```
