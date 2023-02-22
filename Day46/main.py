from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")


music_names = soup.find_all(name="h3", class_="c-title")
# music_names = soup.find_all(name="h3", id= "title-of-a-story")

all_data = [music.getText().split() for music in music_names]
result = ''
for sublst in all_data:
    result += ' '.join(sublst) + ' '
print(result)
