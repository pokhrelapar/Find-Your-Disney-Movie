
# Introduction

The Walt Disney Company has been around for almost 98 years.Fueled by my love for Disney movies, I attempted to create a dataset of every Walt Disney movies I could find. This projects uses webscrapping using BeautifulSoup library to extract required infromation to build the dataset and filter the dataset accordingly.

## Setup

The project was done in Google Colab. You can clone or download the repo to run it locally in Jupyter notebook. I recommend installing Anaconda as a virtual envrionment.

## Background Information

This project was done in a span of two weeks. I had to study up on documentation, ibraries, and data filtering methods. I have always donwloaded datasets from Kaggle and other open datasets for my projects. I had never attempeted to build one myself. Although this is a static database, future work may include building it towards an open dataset hosted on the web. This project showed an interesting look on how datasets are build.

I attempted to srape Wikipedia pages to build the Dataset.In this video we scrape Wikipedia pages to create a dataset on Disney movies.

The follwoing link https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films has references to Disney movies starting from the 1930s to present including some upcoming and undated movies. The main list has references to all the movies. Similarly, each movie has a Wiki page that holds the Infobox. Every possible infobox was craped and then filtered to build the dataset.

It is important to know that not every movie is included in the dataset. Some of the movies do not have a proper info box or do not have a Wikipage or are undated. Movies of these catogeries were excluded from the dataset.

## Libraries Used

-BeautifulSoup
-Pytest
-Re library
-datetime library
-Pickle, JSON, YAML
-Accessing data from OMDB API using Requests
-Pandas

## Final Datasets

The Datasets folder has datasets which contains different version during the filtering process. The xxxx_Final are the final datasets and are available in pickle, excel, cvsm, yaml and json format. You can load the pickle, yaml and json formatted data directly into python using respective load data commands. You can then load the data as a pandas Dataframe to conduct analysis on the data. The analsyis part is a work in progress.

## References

https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://www.omdbapi.com/
https://docs.python.org/3/library/re.html
https://docs.pytest.org/en/7.1.x/contents.html
