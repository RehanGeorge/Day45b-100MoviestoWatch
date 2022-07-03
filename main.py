import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_page = response.text

soup = BeautifulSoup(empire_page, "html.parser")

all_titles = soup.find_all("h3", class_="title")

titles_inverse = [title.getText() for title in all_titles]

with open("movies.txt", mode="a", encoding="utf-8") as file:
    for i in range(99,-1, -1):
        file.write(f"{titles_inverse[i]}\n")