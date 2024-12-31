# Projet X News

Bienvenue dans le projet X News, un bot Twitter automatisé qui récupère des informations depuis une API d'actualités et les publie sur un compte Twitter.

## Fonctionnalités

- Récupère les titres des articles récents via l'API **NewsAPI**.
- Vérifie si un article a déjà été tweeté pour éviter les doublons.
- Publie automatiquement des tweets avec les titres et les liens des articles.
- Utilise Selenium pour automatiser la connexion et l'interaction avec Twitter.

## Installation

1. Clonez le dépôt ou téléchargez le code source.
2. Assurez-vous d'avoir Python installé sur votre machine.
3. Installez les bibliothèques nécessaires à l'aide du fichier `requirements.txt` :
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **API NewsAPI** :

   - Créez un compte sur [NewsAPI](https://newsapi.org) pour obtenir une clé API. (Vous pouvez très bien utiliser une autre Api)
   - Remplissez la variable `newsapi_api_key` avec votre clé API dans le script.

2. **Compte Twitter** :

   - Ajoutez vos identifiants Twitter (`username` et `password`) dans le script pour permettre la connexion automatisée.

3. **Fichier JSON pour les articles tweetés** :
   - Le fichier `tweeted_articles.json` est utilisé pour enregistrer les articles déjà tweetés. Il sera automatiquement créé et mis à jour si inexistant.

## Utilisation

Exécutez le script pour lancer le bot :

```bash
python twitter.py
```

Le bot :

1. Se connectera à votre compte Twitter.
2. Récupérera les articles récents.
3. Publiera un tweet pour chaque nouvel article.

## Notes

- Le bot utilise un intervalle défini (`interval`) pour vérifier régulièrement les nouveaux articles. Vous pouvez modifier cette valeur dans le script.

## Prérequis

- **Google Chrome** installé.
- **Chromedriver** compatible avec la version de votre navigateur. Le gestionnaire de pilotes (`webdriver-manager`) s'en charge automatiquement.

---
