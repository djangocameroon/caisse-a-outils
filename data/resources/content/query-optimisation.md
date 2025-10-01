## Actions à mener
- Préchargez les relations avec `select_related` et `prefetch_related`.
- Exploitez les annotations pour regrouper les calculs côté base de données.
- Mesurez avec la barre d'outils de debug avant et après vos optimisations.

## Exemple rapide
```python
articles = (
    Article.objects.select_related("auteur")
    .prefetch_related("tags")
    .filter(est_publie=True)
)
```

Commencez par identifier les vues qui génèrent des `N+1` grâce à l'inspection des requêtes dans la barre d'outils.
