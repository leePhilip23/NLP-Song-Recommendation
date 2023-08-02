from newsdataapi import NewsDataApiClient
import psycopg2 
import re

# Get all data
def get_data(api):
   # Store sources and domains
   categories = [
      'entertainment',
      'environment',
      'food',
      'health',
      'politics',
      'science',
      'sports',
      'technology',
      'tourism',
      'world'
   ]

   # Get news from 10 countries with highest GDP
   countries = [
      'us',
      'cn',
      'jp',
      'de',
      'gb',
      'in',
      'fr',
      'it',
      'ca',
      'kr'
   ]

   titles = []
   stories = []
   language = 'en'
   # Get all sources and domains
   for country in countries:
      for category in categories:
         response = api.news_api(country=country, category=category, language=language)
         results = response['results']

         for r in results:
            title = r['title']
            story = r['content']

            # Add titles and stories
            titles.append(title)
            stories.append(story)


   return titles, stories

def put_into_postgres(titles, stories):
   # Create table query
   create = f"""
               CREATE TABLE IF NOT EXISTS news (
                  title          varchar(512),
                  story          text
               )
            """

   # Insert query
   insert = f"""
               INSERT INTO news(title, story)
               VALUES(%s, %s)
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

   # Create new table if it doesn't exist
   cursor.execute(create) 

   count = 1
   # Gather and print the title, news company, and news url of all the articles

   print(len(stories), len(titles))
   for title, story in zip(titles, stories):
      # Print all values
      print(f"{count}. Title: {title}") 
      print(f"   Description: {story}")

      # Put into tuple
      values = (title, story)

      # Add values to the table
      cursor.execute(insert, values)

      # Makes sure every SQL statement is properly executed
      connection.commit()

      count += 1

   # Close connection to Postgres
   cursor.close()


def main():
   # API key authorization, Initialize the client with your API key
   SECRET_KEY = 'SECRET_KEY'
   api = NewsDataApiClient(apikey=SECRET_KEY)

   # Get all sources and domains
   titles, stories = get_data(api)

   put_into_postgres(titles, stories)


if __name__ == "__main__":
    main()