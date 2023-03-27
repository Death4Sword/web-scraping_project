from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

def scrap():

    page_content = requests.get("https://www.boulanger.com/c/pc-portable-gamer-49965").content
    soup = BeautifulSoup(page_content, 'lxml')

    # print(soup)

#Script 1
    x = soup.findAll("article", {"class":"product-item"})

    array_ = []

    for i in x:
        dataset = {}
        name = i.find("a").attrs["data-analytics_product_name"].split("pc_gamer_")[1]
        dataset["names"] = name
        brand = i.find("a").attrs["data-analytics_product_trademark"]
        dataset["brands"] = brand
        price = i.find("a").attrs["data-analytics_product_unitprice_ati"]
        dataset["prices"] = price
        processor = i.find("li", {"class":"keypoints__item"}).text.strip()
        dataset["processors"] = processor
        graphic_card = i.findAll("li", {"class":"keypoints__item"})[1].text.strip()
        dataset["graphic_cards"] = graphic_card
        array_.append(dataset)

    # print(array_)
    return array_

#Script 2
bdd = scrap()


def create_Db():
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.2"
   
      # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   return client['Computers']

mydb=create_Db()
myCollection= mydb['scrapping']

def insert_Db(myCollection_, data):
    data = scrap()
    myCollection_.drop()
    myCollection_ = mydb['scrapping']

    for item in data:
        if not myCollection_.find_one({'names': item['names']}):
            myCollection_.insert_one(item)

    list(myCollection_.find())