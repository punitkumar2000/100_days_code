from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup)
article_tag = soup.find_all(name="span", class_="titleline")
# print(article_tag)
all_article_texts = []
all_article_links = []
for tag in article_tag:

    #get all the tags
    all_titles = tag.getText()
    all_titles = all_titles.split("(")[0].strip()
    all_article_texts.append(all_titles)

    links = tag.find('a')['href']
    all_article_links.append(links)

article_upvotes = [score.getText().split()[0] for score in soup.find_all(name="span", class_="score")]
print(all_article_texts)
print(all_article_links)
print(article_upvotes)

max_upvote = max(article_upvotes)
max_index = article_upvotes.index(max_upvote)

values = [all_article_texts[max_index], all_article_links[max_index]]
print(values)

        
