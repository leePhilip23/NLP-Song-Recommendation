import requests

API_KEY = 'secret_key'
API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

#Get the news articles from the US only
params = {
    'apiKey': API_KEY,
    'country': 'us',
}

# Get the news article
def get_data():
    # Top-headlines news articles in the us
    response = requests.get(API_ENDPOINT, params=params)
    
    # Get data in json format
    data = response.json()
    # Extract the articles and return
    articles = data.get('articles', [])
    return articles

# Gather the data and store 
data = get_data()

# Gather and print the title, news company, and news url of all the articles
for i, article in enumerate(data, 1):
    title = article['title']
    news_company = article['source']['name']
    news_url = article['url']

    print(f"{i}. Title: {title}") 
    print(f"   News Company: {news_company}") 
    print(f"   Main News URL: {news_url}") 
