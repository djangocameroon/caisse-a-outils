# Django Debug Toolbar

La barre d'outils ajoute un panneau flottant sur vos pages de développement. Elle montre les requêtes SQL, le temps d'exécution, et l'utilisation du cache, ce qui permet de repérer les goulets d'étranglement sans quitter le navigateur.

## Pourquoi l'utiliser ?
- Visualiser instantanément les requêtes générées par vos vues.
- Détecter les points chauds de performance avec des métriques détaillées.
- Étendre le panneau avec des modules personnalisés adaptés à votre équipe.

## Mise en route
Installez le paquet, ajoutez-le à `INSTALLED_APPS`, puis activez le middleware. Limitez l'affichage aux adresses IP de votre réseau de développement pour garder la barre confidentielle.
