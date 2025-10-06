# Django CORS Headers

Django CORS Headers est un package Django qui ajoute la gestion des en-têtes CORS (Cross-Origin Resource Sharing) à vos applications Django. Il est essentiel pour permettre aux applications frontend (React, Vue, Angular) de communiquer avec votre API Django.

## Pourquoi l'utiliser ?

- **Sécurité** : Contrôle précis des domaines autorisés à accéder à votre API
- **Développement** : Facilite le développement d'applications frontend séparées
- **Production** : Configuration flexible pour différents environnements
- **Simplicité** : Installation et configuration en quelques lignes

## Installation et configuration

```bash
pip install django-cors-headers
```

Ajoutez `corsheaders` à vos `INSTALLED_APPS` :

```python
INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
]
```

Ajoutez le middleware en haut de votre liste de middlewares :

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]
```

## Configuration de base

```python
# Autoriser tous les domaines (développement uniquement)
CORS_ALLOW_ALL_ORIGINS = True

# Ou spécifier des domaines autorisés (recommandé pour la production)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://votre-domaine.com",
]

# Autoriser les cookies
CORS_ALLOW_CREDENTIALS = True
```

## Configuration avancée

```python
# Autoriser des en-têtes personnalisés
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Autoriser des méthodes HTTP spécifiques
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
```

## Bonnes pratiques

- **Développement** : Utilisez `CORS_ALLOW_ALL_ORIGINS = True` uniquement en local
- **Production** : Listez explicitement les domaines autorisés
- **Sécurité** : Configurez `CORS_ALLOW_CREDENTIALS` selon vos besoins
- **Tests** : Testez vos configurations CORS avec différents domaines