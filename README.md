# Web Scraping
Ce projet avait pour but de scrap un site (boulanger pour ma part), et de récupérer les informations souhaitées afin de les ajouter dans notre base de donnée et les visualiser avec streamlit

# Prérequis :
Python 3.2 ou supérieur

# Installation

Clonez le repository, et ouvrez le sur vs:code

# Les différents scripts python

## project.py

Ce script contient la base de notre code, le scraping, l'insertion dans la db.
Le scraping est fait à partir de la librairie BS4 (Beautiful Soup).
Ce script python, récupère différents ordinateurs du site boulanger.
Plus précisément, il récupère le nom, la marque, le prix, le processeur ainsi que la carte graphique de chaque ordinateur.
Les données récupérées sont stockées dans une liste de dictionnaire, puis insérées dans une base de données MongoDB.

## streamlit.py

Ce script, utilise la bibliothèque Streamlit permettant d'afficher nos données, précédemment mise dans la base de donnée.
Cette bibliothèque en lien avec matplotlib et pandas, permet d'afficher des graphiques, et de comparer des données.

## project_test.py
#### class TestScraping :
    Cette classe contient les tests unitaires pour la fonction de scraping
#### class TestInsertDb :
    cette classe contient les tests unitaires pour la fonction d'insertion dans la base de donnée.

#### def test_streamlit_func :
    Cette fonction, permet de faire les tests unitaires pour la fonction générant notre site en utilisant streamlit



# Auteur
Ce projet a été réalisé par Antoine Ducoudré pour un cours de python.

