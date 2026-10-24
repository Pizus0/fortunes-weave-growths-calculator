from bs4 import BeautifulSoup # parses the data
import requests # fetches the data
from tkinter import *

growths = requests.get("https://serenesforest.net/fortunes-weave/characters/growth-rates/") # gets the character growths
soup = BeautifulSoup(growths.text, "html.parser") # grabs the entire website
data = [td.get_text(strip=True) for td in soup.find_all("td")] # grabs every instance of <td> + variables, then removes <td>'

stats = ["HP", "Str", "Mag", "Spd", "Dex", "Def", "Res", "Lck", "Cha"]

characters = {} 
for i in range(0, len(data), 10):
    name = data[i]
    growths = [int(x) for x in data[i + 1:i + 10]]
    characters[name] = dict(zip(stats, growths)) # puts characters growths in an iterable dict

clgrowths = requests.get("https://serenesforest.net/fortunes-weave/classes/growth-rates/") # same as before but for classes
clsoup = BeautifulSoup(clgrowths.text, "html.parser")
cldata = [td.get_text(strip=True) or 0 for td in clsoup.find_all("td")]

classes = {} 
for i in range(0, len(cldata), 10):
    name = cldata[i]
    clgrowths = [int(x) for x in cldata[i + 1:i + 10]]
    classes[name] = dict(zip(stats, clgrowths))

def combine(characters: dict, classes: dict) -> dict: # combines characters and classes together
    keys = dict.fromkeys((*characters, *classes))
    return {k: characters.get(k, 0) + classes.get(k, 0)for k in keys}


window = Tk() # creates a window

window.geometry("420x420")
window.title("Fortunes Weave Growth Checker")
window.config(background="#363636")
entry = Entry(window, font=("Arial", 50), width = 30)
entry.pack()
window.mainloop() # summons window