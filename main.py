from bs4 import BeautifulSoup # parses the data
import requests # fetches the data
import tkinter as tk

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


window = tk.Tk() # creates a window

window.geometry("420x420")
window.title("Fortunes Weave Growth Checker")
window.config(background="#363636")

title = tk.Label(
    window,
    text="Character Growths",
    font=("Arial", 18, "bold"),
    foreground="white",
    background="#363636",
)
title.pack(pady=(24, 12))

name_entry = tk.Entry(window, font=("Arial", 14), width=28)
name_entry.pack(padx=20, pady=8)
name_entry.focus_set()

growths_label = tk.Label(
    window,
    text="Enter a character name to see their growths.",
    font=("Arial", 12),
    foreground="white",
    background="#363636",
    justify=tk.LEFT,
    anchor="nw",
    wraplength=360,
)
growths_label.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)


def show_growths(event=None) -> None:
    name = name_entry.get().strip()
    if not name:
        growths_label.config(text="Enter a character name to see their growths.")
        return

    character_growths = characters.get(name)
    if character_growths is None:
        growths_label.config(text=f"No character named '{name}' was found.")
        return

    growth_list = "\n".join(
        f"{stat}: {growth}%" for stat, growth in character_growths.items()
    )
    growths_label.config(text=f"{name}\n\n{growth_list}")


search_button = tk.Button(
    window,
    text="Show Growths",
    command=show_growths,
    font=("Arial", 12),
)
search_button.pack(pady=(0, 20))
name_entry.bind("<Return>", show_growths)

window.mainloop() # summons window