from bs4 import BeautifulSoup

content = open("Day45/scrap.html", "r")
soup = BeautifulSoup(content, "html.parser")
# print(soup)
# print(soup.title)
# print(soup.title.name)   #will give the tag name
# print(soup.title.string)  #will give the title string
# print(soup.prettify())

# all_ancher_tag = soup.find_all(name="a")
# for tag in all_ancher_tag:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading.text)


# To find out a particular anchor tag
# company_url = soup.select_one(selector="p a")
# print(company_url)


# To find the tag using the text
# a_tag = soup.find("a", href=lambda href: href and "hobbies" in href)
# print(a_tag.text)
# print(a_tag['href'])