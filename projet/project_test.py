import unittest
from unittest import mock
from pymongo import MongoClient
from project import scrap, insert_Db
from streamlit import streamlit_Func
import streamlit as st
import pandas as pd


class TestScraping(unittest.TestCase):

    def test_scraping(self):
        results = scrap()
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        for product in results:
            self.assertIn("names", product)
            self.assertIn("brands", product)
            self.assertIn("prices", product)
            self.assertIn("processors", product)
            self.assertIn("graphic_cards", product)


class TestInsertDb(unittest.TestCase):

    def setUp(self):
        # connect to test database
        self.client = MongoClient()
        self.db = self.client['test_db']

    

    def test_inserts_data_into_database(self):
        # scrap data to use as test input
        data = scrap()

        # call function to test 
        insert_Db(self.db['scrapping'],data)

        # check that data was inserted into collection
        collection = self.db['scrapping']
        result = collection.find({'names': data[0]['names']})
        self.assertIsNotNone(result)

    def tearDown(self):
        # drop test collection and close connection
        self.db['scrapping'].drop()
        self.client.close()

def mock_collection():
    # create a mock collection with some data to return
    data = [
        {"names": "Computer A", "prices": 1000, "graphic_cards": "Nvidia"},
        {"names": "Computer B", "prices": 1200, "graphic_cards": "AMD"},
        {"names": "Computer C", "prices": 800, "graphic_cards": "Intel"},
    ]
    collection = mock.Mock()
    collection.find.return_value = data
    return collection


def test_streamlit_func(mock_collection, monkeypatch):
    # monkeypatch the create_Db function to return a mock database and collection
    monkeypatch.setattr("project.create_Db",
                        lambda: mock.Mock(scrapping=mock_collection))

    # monkeypatch the plt and st functions to avoid displaying graphics and text in the test output
    monkeypatch.setattr("my_module.plt", mock.Mock())
    monkeypatch.setattr("my_module.st", mock.Mock())

    # call the function
    streamlit_Func()

    # check that the mock collection was queried and the data was displayed in the correct format
    mock_collection.find.assert_called_once_with({}, {'_id': 0})
    st.write.assert_called_once_with('Boulanger web scrapping')
    st.write.assert_called_once_with(
        pd.DataFrame(mock_collection.find.return_value))
    st.pyplot.assert_called_once()



