# django-rest-framework

Django REST Framework (DRF) est une bibliothèque puissante et flexible pour construire des API Web avec Django. Elle simplifie le développement d'API RESTful en fournissant des outils et des abstractions pour gérer les requêtes HTTP, la sérialisation des données, l'authentification, et bien plus encore.

## Points forts

- **Sérialisation** : Convertit facilement les objets Django en formats JSON, XML, etc.
- **Vues basées sur les classes** : Facilite la création de vues réutilisables et modulaires.
- **Authentification et permissions** : Supporte divers mécanismes d'authentification (Token, OAuth, JWT) et contrôle d'accès.
- **Pagination** : Gère efficacement les grandes collections de données.
- **Documentation automatique** : Génère automatiquement la documentation de l'API.
- **Support pour les tests** : Intègre des outils pour tester

## Mise en route

Pour intégrer Django REST Framework dans votre projet Django, suivez ces étapes simples :

1. **Installation** : Installez le package via pip :
   ```
   pip install djangorestframework
   ```

2. **Configuration dans settings.py** : Ajoutez `'rest_framework'` à la liste `INSTALLED_APPS` :
   ```python
   INSTALLED_APPS = [
       # ... vos autres applications
       'rest_framework',
   ]
   ```

3. **Configuration optionnelle** : Vous pouvez personnaliser les paramètres par défaut de DRF en ajoutant un dictionnaire `REST_FRAMEWORK` dans votre `settings.py`, par exemple pour la pagination ou l'authentification :
   ```python
   REST_FRAMEWORK = {
       'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
       'PAGE_SIZE': 10,
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.TokenAuthentication',
       ],
   }
   ```

4. **Création de votre première API** : Créez un modèle, un sérialiseur et une vue basée sur les classes pour exposer vos données via l'API.

Pour plus de détails, consultez la [documentation officielle de DRF](https://www.django-rest-framework.org/).

