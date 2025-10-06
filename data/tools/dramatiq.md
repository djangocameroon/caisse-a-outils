# Dramatiq

Dramatiq est une bibliothèque de traitement de tâches en arrière-plan pour Python, conçue pour être simple, fiable et performante. C'est une alternative moderne à Celery, souvent appréciée pour sa simplicité et sa robustesse. Elle utilise Redis ou RabbitMQ comme brokers de messages pour distribuer les tâches entre différents workers.

## Pourquoi l'utiliser ?

- **Simplicité** : Une API claire et une configuration minimale pour démarrer rapidement.
- **Fiabilité** : Les messages ne sont acquittés qu'après un traitement réussi, garantissant qu'aucune tâche n'est perdue en cas d'échec d'un worker.
- **Performance** : Conçu pour être rapide et léger, il utilise des threads pour une exécution efficace des tâches.
- **Fonctionnalités modernes** : Supporte nativement les retentatives automatiques avec un backoff exponentiel, la priorisation des tâches et les délais d'expiration.

## Installation et configuration

L'installation de Dramatiq et de son intégration avec Django se fait via pip.

```bash
pip install dramatiq[redis] django-dramatiq
```

Ajoutez `django_dramatiq` à vos `INSTALLED_APPS` dans le fichier `settings.py` de votre projet Django.

### Configuration dans settings.py

```python
# Broker Redis
DRAMATIQ_BROKER = {
    "BROKER": "dramatiq.brokers.redis.RedisBroker",
    "OPTIONS": {
        "host": "localhost",
        "port": 6379,
        "db": 0,
    },
    "MIDDLEWARE": [
        "dramatiq.middleware.AgeLimit",
        "dramatiq.middleware.TimeLimit",
        "dramatiq.middleware.Retries",
        "django_dramatiq.middleware.DbConnectionsMiddleware",
    ]
}

# Découverte automatique des tâches (actors)
DRAMATIQ_ACTORS_MODULE = "mon_app.actors"
```

## Exemple d'utilisation

Avec Dramatiq, les tâches sont appelées des "actors".

### Création d'un actor

Créez un fichier `actors.py` dans votre application Django :

```python
import dramatiq
from django.core.mail import send_mail

@dramatiq.actor
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
        print(f"Email envoyé à {len(destinataires)} destinataires")
    except Exception as e:
        print(f"Erreur lors de l'envoi: {str(e)}")
        raise  # Propage l'exception pour que Dramatiq la gère (retry)
```

### Appel de la tâche

```python
from .actors import envoyer_email_async

def ma_vue(request):
    # Traitement immédiat
    resultat = traitement_rapide()
    
    # Tâche en arrière-plan
    envoyer_email_async.send(
        "Confirmation",
        "Votre demande a été traitée",
        [request.user.email]
    )
    
    return JsonResponse({'status': 'success'})
```

## Tâches périodiques avec Periodiq

Dramatiq lui-même ne gère pas les tâches périodiques, mais un package complémentaire appelé `periodiq` le fait de manière très simple.

```bash
pip install periodiq
```

Configurez le middleware dans `settings.py` et décorez vos acteurs :

```python
# Dans settings.py, ajoutez le middleware
# ...
    "MIDDLEWARE": [
        # ... autres middlewares
        "periodiq.middleware.PeriodiqMiddleware",
    ]
# ...

# Dans actors.py
from periodiq import cron

@dramatiq.actor(periodic=cron('* * * * *')) # Toutes les minutes
def ma_tache_periodique():
    print("Cette tâche s'exécute toutes les minutes !")

@dramatiq.actor(periodic=cron('0 2 * * *')) # Tous les jours à 2h
def nettoyer_cache():
    print("Nettoyage du cache...")
```

## Commandes utiles

```bash
# Démarrer les workers Dramatiq (découverte automatique via Django)
python manage.py rundramatiq

# Démarrer le planificateur Periodiq (pour les tâches périodiques)
periodiq mon_projet.actors

# Monitoring avec le dashboard intégré (pour Redis)
pip install dramatiq_dashboard
# Puis intégrez le middleware WSGI dans votre projet
```

## Bonnes pratiques

- **Idempotence** : Assurez-vous que vos tâches peuvent être exécutées plusieurs fois sans effets de bord indésirables, car des pannes peuvent entraîner des reprises.
- **Messages simples** : Passez des identifiants (comme un ID d'utilisateur) plutôt que des objets complexes sérialisés dans les paramètres de vos tâches.
- **Timeouts** : Définissez des `time_limit` pour vos acteurs afin d'éviter qu'ils ne restent bloqués indéfiniment.
- **Tests** : Utilisez le `StubBroker` fourni par Dramatiq pour tester vos acteurs de manière synchrone et unitaire.
- **Monitoring** : Utilisez des outils comme `dramatiq_dashboard` pour Redis ou intégrez Prometheus pour un suivi de la santé de vos workers.