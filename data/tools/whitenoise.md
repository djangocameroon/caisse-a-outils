# Whitenoise

Whitenoise simplifie la distribution des fichiers statiques en production. Il prend en charge la compression, les en-têtes de cache et l'intégration avec la configuration par défaut de Django.

## Points forts
- Aucun serveur externe requis pour livrer vos CSS et JS.
- Compression gzip et brotli intégrée pour gagner en bande passante.
- Gestion du cache en fonction du fichier pour éviter les assets périmés.

## Mise en route
Ajoutez Whitenoise au middleware de sécurité, configurez `STATIC_ROOT`, puis exécutez `collectstatic` avant de déployer. Les assets seront servis par l'application tout en conservant de bonnes performances.
