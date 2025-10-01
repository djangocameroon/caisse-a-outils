# Caisse A Outils

Caisse A Outils est une application Django qui recense des outils utiles pour la communauté Django Cameroun. Le contenu provient de fichiers JSON et Markdown stockés dans le dossier `data/`.

## Prérequis
- Python 3.11+
- [uv](https://github.com/astral-sh/uv)

## Démarrer
1. Installer les dépendances : `uv sync`
2. Appliquer les migrations : `uv run python manage.py migrate`
3. Lancer le serveur : `uv run python manage.py runserver`

Ouvrez ensuite http://127.0.0.1:8000/ pour consulter la liste des outils. Les pages utilisent Tailwind CSS via le CDN officiel, aucun build supplémentaire n'est nécessaire.

## Contenu
- `data/tools.json` répertorie les outils affichés sur la page d'accueil et la page listant tous les outils.
- Chaque entrée d'outil référence un fichier Markdown dans `data/tools/` qui est rendu sur la page de détail.
- `data/resources/` contient les astuces, snippets et guides au format JSON, YAML ou TOML. Chaque fichier peut inclure directement du Markdown (`body`) ou pointer vers un fichier dédié dans `data/resources/content/` via `content_path`.

Pour proposer un nouvel outil ou une ressource, suivez les étapes décrites dans [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence
Ce projet est distribué sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
