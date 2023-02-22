from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)

content = response.text

soup = BeautifulSoup(content, "html.parser")

movies = soup.find_all(name="h3", class_="title")
get_all_movies = [movie.getText() for movie in movies]
get_all_movies.reverse()

with open("Day45/movies.txt", mode="w") as file:
    for get_movies in get_all_movies:
        file.write(f"{get_movies}\n")
