# Celery

Celery est un système de files d'attente de tâches distribué pour Python, particulièrement populaire avec Django. Il permet d'exécuter des tâches en arrière-plan de manière asynchrone, ce qui améliore les performances et l'expérience utilisateur.

## Pourquoi l'utiliser ?

- **Performance** : Délègue les tâches lourdes en arrière-plan
- **Scalabilité** : Distribue les tâches sur plusieurs workers
- **Fiabilité** : Gestion des échecs et retry automatique
- **Flexibilité** : Support de différents brokers (Redis, RabbitMQ, etc.)

## Installation et configuration

```bash
pip install celery redis
```

Créez un fichier `celery.py` dans votre projet Django :

```python
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mon_projet.settings')

app = Celery('mon_projet')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

Ajoutez dans `__init__.py` de votre projet :

```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

## Configuration dans settings.py

```python
# Broker Redis
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Configuration des tâches
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Retry automatique
CELERY_TASK_RETRY_DELAY = 60
CELERY_TASK_MAX_RETRIES = 3
```

## Exemple d'utilisation

### Création d'une tâche

```python
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def envoyer_email_async(sujet, message, destinataires):
    """Envoie un email de manière asynchrone"""
    try:
        send_mail(
            sujet,
            message,
            'noreply@example.com',
            destinataires,
            fail_silently=False,
        )
        return f"Email envoyé à {len(destinataires)} destinataires"
    except Exception as e:
        return f"Erreur lors de l'envoi: {str(e)}"
```

### Appel de la tâche

```python
from .tasks import envoyer_email_async

def ma_vue(request):
    # Traitement immédiat
    resultat = traitement_rapide()
    
    # Tâche en arrière-plan
    envoyer_email_async.delay(
        "Confirmation",
        "Votre demande a été traitée",
        [request.user.email]
    )
    
    return JsonResponse({'status': 'success'})
```

## Tâches périodiques avec Celery Beat

```python
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'nettoyer-cache': {
        'task': 'mon_app.tasks.nettoyer_cache',
        'schedule': crontab(hour=2, minute=0),  # Tous les jours à 2h
    },
    'rapport-hebdomadaire': {
        'task': 'mon_app.tasks.generer_rapport',
        'schedule': crontab(day_of_week=1, hour=9, minute=0),  # Lundi 9h
    },
}
```

## Commandes utiles

```bash
# Démarrer Celery worker
celery -A mon_projet worker --loglevel=info

# Démarrer Celery Beat (tâches périodiques)
celery -A mon_projet beat --loglevel=info

# Monitoring avec Flower
pip install flower
celery -A mon_projet flower
```

## Bonnes pratiques

- **Idempotence** : Rendez vos tâches idempotentes quand possible
- **Timeouts** : Configurez des timeouts appropriés
- **Logging** : Ajoutez des logs détaillés dans vos tâches
- **Tests** : Testez vos tâches avec `CELERY_TASK_ALWAYS_EAGER = True`
- **Monitoring** : Utilisez Flower ou un outil similaire pour surveiller vos workers