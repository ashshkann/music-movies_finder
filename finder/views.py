from django.shortcuts import redirect, render
from .forms import form_music, form_movies
import requests as req
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    return render(request, 'temp/home.html', {})

def music(request):
    form = form_music(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name_music = form.cleaned_data.get('finder_music_form')
            
            if " " in name_music:
                name_music = name_music.replace(" ", "+")
            data_music = req.get(f'https://www.music-map.com/{name_music}')
            soup = BeautifulSoup(data_music.text, 'html.parser')
            finder_div = soup.find("span", class_="the_title")
            str_div = finder_div.string
            errortext = "I got 404 problems"
            data = []
            number = 0
            number_music = [] 
            if errortext in str_div:
                form.add_error('finder_music_form', "we don't know this one. Is the spelling correct?")
            else:
                div = soup.find("div", id='gnodMap')
                for text in div:
                    name_music = text.string.replace("\n", "")
                    data.append(name_music)
                    number += 1
                    number_music.append(number)
                filter_data = filter(lambda i: i != '',  data)
                all_data_music = list(filter_data)
                request.session['musicname'] = all_data_music
                request.session['number'] = number_music
                return redirect('/music-result')

    context = {
        'form':form,
    }
    return render(request, 'temp/music/music.html', context)

def music_views(request):
    music_names = request.session['musicname']
    number = request.session['number']
    zippedList = zip(number, music_names)
    context = {
        'data': zippedList,
    }
    return render(request, 'temp/music/music_views.html', context)


def movies(request):
    form = form_movies(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            input_movies = form.cleaned_data.get("finder_movies_form")
            if " " in input_movies:
                input_movies = input_movies.replace(" ", "+")
            data_movies = req.get(f'https://www.movie-map.com/{input_movies}')
            soup = BeautifulSoup(data_movies.text, 'html.parser')

            divfind = soup.find("span", class_="the_title")
            strdiv = divfind.string
            errortext = "I got 404 problems"

            data_name = []
            number = 0
            number_movies = [] 
            
            if errortext in strdiv:
                form.add_error('finder_movies_form', "we don't know this one. Is the spelling correct?") 
            else:
                div = soup.find("div", id='gnodMap')
                for text in div:
                    name_movies = text.string.replace("\n", "")
                    data_name.append(name_movies)
                    number += 1
                    number_movies.append(number)

                filter_data = filter(lambda i: i != '',  data_name)
                list_data_movies = list(filter_data)
                request.session['movies'] = list_data_movies
                request.session['number'] = number_movies
                return redirect('/movies-result')
    context = {
        'form': form,
    }
    return render(request, 'temp/movies/movies.html', context)

def movies_views(request):
    movies_names = request.session['movies']
    number = request.session['number']
    zippedList = zip(number, movies_names)
    context = {
        'data': zippedList,
    }
    return render(request, 'temp/movies/movies_views.html', context)