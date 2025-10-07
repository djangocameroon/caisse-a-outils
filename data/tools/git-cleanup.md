# Git Cleanup 🧹

**Git Cleanup** est un petit script Shell conçu pour maintenir votre dépôt Git propre en supprimant les branches locales déjà fusionnées dans la branche principale (`main` ou `master`).

> ⚠️ Il existe déjà un projet officiel maintenu par **mloughran**, que vous pouvez télécharger ici : [mloughran/git-cleanup](https://github.com/mloughran/git-cleanup)

---

## 💡 Pourquoi l’utiliser ?
Au fil du temps, un dépôt Git peut accumuler de nombreuses branches locales devenues inutiles après fusion.  
**Git Cleanup** automatise le nettoyage pour garder votre espace de travail clair, lisible et à jour.

---

## ⚙️ Installation & Utilisation

### 1️⃣ Téléchargement
Téléchargez le script officiel depuis le dépôt GitHub :
```bash
curl -O https://raw.githubusercontent.com/mloughran/git-cleanup/master/git-cleanup
chmod +x git-cleanup
