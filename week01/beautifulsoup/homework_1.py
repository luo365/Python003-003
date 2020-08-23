import json
import requests
import time
from bs4 import BeautifulSoup as bs


def load_headers():
    with open('headers.json', 'r') as f:
        headers = json.load(f)
    return headers


def get_movies_top10():
    url = r'https://maoyan.com/films?showType=3'
    headers = load_headers()
    r = requests.get(url=url, headers=headers)
    soup = bs(r.text, 'lxml')

    movies = []

    for tags in soup.find_all('div', attrs={'class': 'channel-detail'}):
        for atag in tags.find_all('a'):
            item = {}
            item['name'] = atag.text
            item['url'] = 'https://maoyan.com' + atag.get('href')
            movies.append(item)

    movies_top10 = movies[:10]
    cookies = r.cookies

    return movies_top10, cookies


def extract_movie_info(movie_url, headers, cookies):
    r_movie = requests.get(url=movie_url, headers=headers, cookies=cookies)
    soup_movie = bs(r_movie.text, 'lxml')

    genre = []
    for tags in soup_movie.find_all('div', attrs={'class': 'movie-brief-container'}):
        for atag in tags.find_all('a'):
            genre.append(atag.text.strip())

    date_time = soup_movie.select(
        'ul > li.ellipsis:nth-of-type(3)')[0].getText()
    return genre, date_time


def update_movie_info(movie_list, cookies):
    headers = load_headers()
    time.sleep(0.5)
    for movie in movie_list:
        movie_url = movie['url']
        genre, date_time = extract_movie_info(movie_url, headers, cookies)
        movie['genre'] = genre
        movie['date_time'] = date_time
        time.sleep(0.5)


def output_movies(movies):
    with open(r'.\maoyan_movies.csv', 'a+', encoding='utf-8') as article:
        for item in movies:
            output = item['name'] + ';' + \
                     str(item['genre']) + ';' + item['date_time'] + '\n'
            article.write(output)
        article.close()


if __name__ == "__main__":
    movies_top10, cookies = get_movies_top10()
    update_movie_info(movies_top10, cookies)
    output_movies(movies_top10)
