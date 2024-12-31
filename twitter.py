from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import requests
import json
from selenium.webdriver.common.keys import Keys

# api infos
newsapi_url = "https://newsapi.org/v2/top-headlines"
newsapi_api_key = ""

# compte twitter
username = ''
password = ''

def get_news_titles():
    headers = {'Authorization': f'Bearer {newsapi_api_key}'}
    params = {
        'country': 'us',
        'category': 'general',
        'pageSize': 5
    }
    response = requests.get(newsapi_url, headers=headers, params=params)
    data = response.json()
    titles = [article['title'] + ' ' + article['url']  for article in data['articles']]
    return titles

# Chemin vers le fichier JSON pour enregistrer les données des articles déjà tweetés
tweeted_articles_file_path = "tweeted_articles.json"

# Fonction pour charger les articles déjà tweetés depuis le fichier JSON
def load_tweeted_articles():
    try:
        with open(tweeted_articles_file_path, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

# Fonction pour enregistrer les articles tweetés dans le fichier JSON
def save_tweeted_articles(articles):
    with open(tweeted_articles_file_path, "w") as json_file:
        json.dump(articles, json_file, indent=4)

# Lien vers la page de login de Twitter
twitter_url = 'https://twitter.com/i/flow/login'

# Configuration & démarrage de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')  # Navigation en mode incognito
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Se connecter à Twitter une seule fois
driver.get(twitter_url)

# Attendre que le champ email soit visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "text")))

# Remplir le champ email
email_field = driver.find_element(By.NAME, "text")
email_field.send_keys(username)
email_field.send_keys(Keys.RETURN)

# Attendre une peu afin que le champ mot de passe soit visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))

# Remplir le champ mot de passe
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

time.sleep(5)  # Attente pour laisser la page se charger après la connexion

# Liste pour suivre les articles déjà tweetés
tweeted_articles = load_tweeted_articles()

# Intervalles de vérification des nouveaux articles (en secondes)
interval = 3

while True:
    # Récupérer les titres d'articles
    news_titles = get_news_titles()

    # Filtrer les nouveaux articles non encore tweetés
    new_articles = [title for title in news_titles if title not in tweeted_articles]

    if new_articles:
        # Ouvrir la page de composition d'un nouveau tweet
        tweet_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="SideNav_NewTweet_Button"]')
        driver.execute_script("arguments[0].click();", tweet_button)

        # Attendre que le champ de texte soit visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')))

        # Trouver le champ de texte par le sélecteur CSS
        tweet_textarea = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')

        # Texte à insérer (choix aléatoire parmi les nouveaux textes)
        tweet_text = random.choice(new_articles)

        # Simuler l'entrée de texte caractère par caractère
        for char in tweet_text:
            tweet_textarea.send_keys(char)
            time.sleep(0.1)  # Ajoutez un petit temps d'attente pour laisser le temps au texte de s'insérer

        # Attendre que le bouton de publication soit visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]')))

        # Trouver le bouton de publication par le sélecteur CSS
        tweet_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButton"]')
        tweet_button.click()

        # Enregistrer la liste mise à jour dans le json pour pas le retweeter
        tweeted_articles.append(tweet_text)
        save_tweeted_articles(tweeted_articles)

    time.sleep(interval)
