import pymongo
import pandas as pd
from scrape_mars import scrape
import json


# Create connection variable
conn = 'mongodb://localhost:27017'


# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db


#News
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
info = "News"
# Drops collection if available to remove duplicates
db.news.drop()
#Insert info
#print(scrape(info,url))
db.news.insert_many(scrape(info,url))

#Images
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
info = "Images"
# Drops collection if available to remove duplicates
db.images.drop()
#Insert info
#print(scrape(info,url))
db.images.insert_many(scrape(info,url))

#Weather
url = "https://twitter.com/marswxreport?lang=en"
info = "Weather"
# Drops collection if available to remove duplicates
db.weather.drop()
#Insert info
#print(scrape(info,url))
db.weather.insert_many(scrape(info,url))

#Facts
url = "https://space-facts.com/mars/"
info = "Facts"
# Drops collection if available to remove duplicates
db.facts.drop()
#Insert info
#print(scrape(info,url))
df = pd.DataFrame(scrape(info,url))
df_json = df.to_json()
df_json_list = json.loads(df_json).values()
db.facts.insert(df_json_list)

#Hemispheres
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
info = "Hemis"
# Drops collection if available to remove duplicates
db.hemis.drop()
#Insert info
#print(scrape(info,url))
db.hemis.insert_many(scrape(info,url))