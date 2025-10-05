# Caisse A Outils

Caisse A Outils est une application Django qui recense des outils utiles pour la communauté Django Cameroun. Le contenu provient de fichiers JSON et Markdown stockés dans le dossier `data/`.


## Prérequis
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (optionnel)

Si vous ne souhaitez pas utiliser `uv`, vous pouvez installer les dépendances avec `pip` et le fichier `requirements.txt` fourni.


## Démarrer

### Avec uv (recommandé)
1. Installer les dépendances : `uv sync`
2. Créer les migrations : `uv run python manage.py makemigrations`
3. Appliquer les migrations : `uv run python manage.py migrate`
4. Charger les données : `uv run python manage.py load_data`
5. Lancer le serveur : `uv run python manage.py runserver`

### Avec pip
1. Installer les dépendances :
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Créer les migrations :
   ```bash
   python manage.py makemigrations
   ```
3. Appliquer les migrations :
   ```bash
   python manage.py migrate
   ```
4. Charger les données :
   ```bash
   python manage.py load_data
   ```
5. Lancer le serveur :
   ```bash
   python manage.py runserver
   ```
Ouvrez ensuite http://127.0.0.1:8000/ pour consulter la liste des outils. Les pages utilisent Tailwind CSS via le CDN officiel, aucun build supplémentaire n'est nécessaire.



## Contenu
- `data/tools.json` répertorie les outils affichés sur la page d'accueil et la page listant tous les outils.
- Chaque entrée d'outil référence un fichier Markdown dans `data/tools/` qui est rendu sur la page de détail.
- `data/resources/` contient les astuces, snippets et guides au format JSON, YAML ou TOML. Chaque fichier peut inclure directement du Markdown (`body`) ou pointer vers un fichier dédié dans `data/resources/content/` via `content_path`.

Pour proposer un nouvel outil ou une ressource, suivez les étapes décrites dans [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence
Ce projet est distribué sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
