# Project X News

Welcome to the Project X News, an automated Twitter bot that fetches information from a news API and posts it on a Twitter account.

## Features

- Fetches recent article headlines via the **NewsAPI**.
- Checks if an article has already been tweeted to avoid duplicates.
- Automatically posts tweets with article titles and links.
- Uses Selenium to automate login and interaction with Twitter.

## Installation

1. Clone the repository or download the source code.
2. Ensure Python is installed on your machine.
3. Install the required libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **NewsAPI**:

   - Create an account on [NewsAPI](https://newsapi.org) to obtain an API key. (You can also use another API if preferred.)
   - Fill the `newsapi_api_key` variable with your API key in the script.

2. **Twitter Account**:

   - Add your Twitter credentials (`username` and `password`) in the script to enable automated login.

3. **JSON File for Tweeted Articles**:
   - The `tweeted_articles.json` file is used to store already tweeted articles. It will be automatically created and updated if it doesn't exist.

## Usage

Run the script to start the bot:

```bash
python twitter.py
```

The bot will:

1. Log in to your Twitter account.
2. Fetch recent articles.
3. Post a tweet for each new article.

## Notes

- The bot uses a defined interval (`interval`) to regularly check for new articles. You can modify this value in the script.

## Prerequisites

- **Google Chrome** installed.
- **Chromedriver** compatible with your browser version. The driver manager (`webdriver-manager`) handles this automatically.

---
