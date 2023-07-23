from newsapi import NewsApiClient
import psycopg2 
import requests

# API Keys and Enpoints (URL)
API_KEY = 'SECRET KEY'
API_ENDPOINT_HEADLINES = 'https://newsapi.org/v2/top-headlines'
API_ENDPOINT_EVERYTHING = 'https://newsapi.org/v2/everything'
API_ENDPOINT_SOURCES = 'https://newsapi.org/v2/top-headlines/sources'

# Create table query
create = f"""
            CREATE TABLE IF NOT EXISTS news (
               title          varchar(512),
               news_company   varchar(30),
               news_url       text,
               story          text
            )
         """

# Insert query
insert = f"""
            INSERT INTO 
               news(title, news_company, news_url, story)
               VALUES(%s, %s, %s, %s)
         """

# Establish connection to Postgres server and database
connection = psycopg2.connect(
      host='localhost',
      port='5432',
      user='postgres',
      database='articles',
      password='articlenlp'
   )

# Create connection to Postgres
cursor = connection.cursor()

# Create NewsApi object
newsapi = NewsApiClient(api_key=API_KEY)

# Get all links
def get_links():
   # Store sources and domains
   sources = []
   domains = []

   # Establish link to NewsApi to get all sources and domains
   links = newsapi.get_sources()

   # Get all sources and domains
   for data in links['sources']:
      if data['language'] == 'en':
         sources.append(data['id'])
         domains.append(data['url'])

   return sources, domains
   

# Get the news article
def get_data(sources_, domains_):

    # All articles for every source and domain
    all_articles = newsapi.get_everything(sources=sources_,
                                          domains=domains_,
                                          language='en',
                                          sort_by='relevancy')
    
    return all_articles['articles']

# Get all sources and domains
sources, domains = get_links()

# Create new table if it doesn't exist
cursor.execute(create) 

# Gather and print the title, news company, and news url of all the articles
for s, d in zip(sources, domains):
   data = get_data(s, d)
   for i, article in enumerate(data):
      # Get the title, company name, url, story, and place them in values tuple
      title = article['title']
      news_company = article['source']['name']
      news_url = article['url']
      story = article['content']
      values = (title, news_company, news_url, story)

      # Print all values
      print(f"{i + 1}. Title: {title}") 
      print(f"   News Company: {news_company}") 
      print(f"   Main News URL: {news_url}") 
      print(f"   Description: {story}")

      # Add values to the table
      cursor.execute(insert, values)

      # Makes sure every SQL statement is properly executed
      connection.commit()

# Close connection to Postgres
cursor.close()
