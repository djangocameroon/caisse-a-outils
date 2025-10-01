# Contribuer

Merci de votre intérêt pour Caisse A Outils. Voici la marche à suivre pour proposer une contribution :

1. Installez les dépendances avec `uv sync` puis lancez `uv run python manage.py migrate` si nécessaire.
2. Créez une branche descriptive et ajoutez vos changements.
3. Pour ajouter un outil, mettez à jour `data/tools.json` puis ajoutez un fichier Markdown dans `data/tools/` avec le même slug.
4. Pour une ressource (tip ou snippet), créez un fichier JSON, YAML ou TOML dans `data/resources/`. Vous pouvez soit renseigner la clé `body` pour du Markdown inline, soit utiliser `content_path` pour référencer un fichier dans `data/resources/content/`.
5. Vérifiez votre travail avec `uv run python manage.py check` et, si pertinent, `uv run python manage.py test`.
6. Ouvrez une pull request en décrivant clairement vos modifications et les impacts attendus.

Les pistes de documentation ou de correction sont toujours les bienvenues tant qu'elles respectent le [Code of Conduct](CODE_OF_CONDUCT.md).
