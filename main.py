
import requests
from bs4 import BeautifulSoup


date = input("Which year do you want to travel?Type in this Format YY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
music_data = response.text

soup = BeautifulSoup(music_data, "html.parser")
song_list = soup.findAll(name="h3", class_="a-no-trucate")

song_name = [song.get_text().strip("\n") for song in song_list]
print(song_name)
print(len(song_name))





