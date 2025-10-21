# Sentry

Sentry est une plateforme de **monitoring des erreurs** et de **suivi de performance** pour les applications web, notamment Django.  
Elle permet de détecter, enregistrer et analyser automatiquement les exceptions qui se produisent côté serveur (et même côté frontend).

## Pourquoi l'utiliser ?

- **Visibilité complète** sur les erreurs et bugs en production
- **Alerte en temps réel** par email, Slack, etc.
- **Stack trace détaillée** pour chaque exception
- **Suivi des performances** : requêtes lentes, goulots d’étranglement
- **Intégration facile** avec Django, Celery, etc.

## Installation et configuration

```bash
pip install --upgrade sentry-sdk
