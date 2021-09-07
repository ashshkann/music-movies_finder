import requests as req
from bs4 import BeautifulSoup
import imdb

def operations():
    input_movies = str(input("input your fucking movies: "))

    ia = imdb.IMDb() 
    if " " in input_movies:
        input_movies = input_movies.replace(" ", "+")
    data_movies = req.get(f'https://www.movie-map.com/{input_movies}')
    soup = BeautifulSoup(data_movies.text, 'html.parser')

    divfind = soup.find("span", class_="the_title")
    strdiv = divfind.string
    errortext = "I got 404 problems"

    data_name = []
    
    if errortext in strdiv:
        print("esm in film motabar nist") 
    else:
        div = soup.find("div", id='gnodMap')
        for text in div:
            name_movies = text.string.replace("\n", "")
            data_name.append(name_movies)

        filter_data = filter(lambda i: i != '',  data_name)
        list_data_movies = list(filter_data)
