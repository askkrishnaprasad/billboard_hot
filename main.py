import requests
from bs4 import BeautifulSoup


# Ask user for input
year = input("What year you would like to travel to in YYY-MM-DD format: ")

URL = f"https://www.billboard.com/charts/hot-100/{year}"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")

song_list = [song.getText().strip() for song in all_songs]
print(song_list)

