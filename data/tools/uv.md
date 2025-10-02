# UV

UV est un gestionnaire de paquets Python ultra-rapide écrit en Rust. Il remplace pip et pip-tools avec des performances jusqu'à 10-100x plus rapides, tout en maintenant une compatibilité complète avec l'écosystème Python existant.

## Pourquoi l'utiliser ?
- Installation de dépendances jusqu'à 100x plus rapide que pip traditionnel.
- Résolution des dépendances intelligente et déterministe comme Poetry mais en plus rapide.
- Compatible avec tous les projets Python existants sans migration complexe.
- Gestion intégrée des environnements virtuels et des versions Python.
- Interface simple et familière pour les utilisateurs de pip.

## Mise en route
Installez UV avec `pip install uv` ou téléchargez le binaire. Remplacez `pip install` par `uv add` pour ajouter des dépendances, ou `uv pip install` pour un remplacement direct de pip. Créez des projets avec `uv init` et gérez les environnements avec `uv venv`. UV génère automatiquement des fichiers de verrouillage pour des builds reproductibles.
