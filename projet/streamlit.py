from pymongo import MongoClient
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def create_Db():
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.2"
      # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   return client['Computers']

def streamlit_Func():
   mydb=create_Db()
   myCollection= mydb['scrapping'] 
   print(list(myCollection.find()))
   df = pd.DataFrame(list(myCollection.find({}, {'_id':0})))
   st.write('Boulanger web scrapping')
   st.write(df)   
   fig, ax = plt.subplots()
   ax.bar(df["names"], df["prices"])
   ax.set_ylabel('price per computer')
   ax.set_xlabel('computer names')
   plt.xticks(rotation=90)
   st.pyplot(fig)

   
   
   df['brands'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, counterclock=False)
   ax.set_ylabel('')
   ax.set_xlabel('')
   ax.set_title('Proportion of different brands')
   st.pyplot(fig)

   
   
streamlit_Func()
