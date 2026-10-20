from bs4 import BeautifulSoup # parses the data
import requests # fetches the data
import csv # csv omegalol

growths = requests.get("https://serenesforest.net/fortunes-weave/characters/growth-rates/") # gets the character growths
soup = BeautifulSoup(growths.text, "html.parser") # grabs the entire website
data = [td.get_text(strip=True) for td in soup.find_all("td")] # grabs every instance of <td> + variables, then removes <td>'

stats = ["HP", "Str", "Mag", "Spd", "Dex", "Def", "Res", "Lck", "Cha"]

characters = {}
for i in range(0, len(data), 10):
    name = data[i]
    growths = [int(x) for x in data[i + 1:i + 10]]
    characters[name] = dict(zip(stats, growths))

clgrowths = requests.get("https://serenesforest.net/fortunes-weave/classes/growth-rates/") # same as before but for classes
clsoup = BeautifulSoup(clgrowths.text, "html.parser")
cldata = [td.get_text(strip=True) for td in clsoup.find_all("td")]


print(characters["Eshmel"]["HP"])
print(characters["Leda"])