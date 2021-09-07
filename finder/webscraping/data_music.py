import requests as req
from bs4 import BeautifulSoup


def operations_music(input_music):

    if " " in input_music:
        input_music = input_music.replace(" ", "+")
    data_music = req.get(f'https://www.music-map.com/{input_music}')
    soup = BeautifulSoup(data_music.text, 'html.parser')

    divfind = soup.find("span", class_="the_title")
    strdiv = divfind.string
    errortext = "I got 404 problems"

    data = []
    
    if errortext in strdiv:
        print("esm in film motabar nist") 
    else:
        div = soup.find("div", id='gnodMap')
        for text in div:
            name_music = text.string.replace("\n", "")
            data.append(name_music)

        filter_data = filter(lambda i: i != '',  data)
        list_data_music = list(filter_data)

