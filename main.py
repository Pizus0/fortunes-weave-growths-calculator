from bs4 import BeautifulSoup # parses the data
import requests # fetches the data
import tkinter as tk
from tkinter import ttk

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

def combine (character_growths: dict[str, int], class_growths: dict[str, int], ) -> dict[str, int]:
    return {stat: character_growths.get(stat, 0) + class_growths.get(stat, 0) for stat in stats}

# window stuff below

window = tk.Tk() # creates a window

window.geometry("420x520")
window.title("Fortunes Weave Growth Checker")
window.config(background="#363636")

title = tk.Label(
    window,
    text="Character & Class Growths",
    font=("Arial", 18, "bold"),
    foreground="white",
    background="#363636",
)
title.pack(pady=(24, 12))

character_label = tk.Label(
    window,
    text="Character name",
    font=("Arial", 12),
    foreground="white",
    background="#363636",
)
character_label.pack(pady=(8, 2))
character_entry = ttk.Combobox(
    window,
    values=tuple(characters),
    font=("Arial", 14),
    width=26,
    state="normal",
)
character_entry.pack(padx=20, pady=(0, 8))
character_entry.focus_set()

class_label = tk.Label(
    window,
    text="Class name",
    font=("Arial", 12),
    foreground="white",
    background="#363636",
)
class_label.pack(pady=(4, 2))
class_entry = ttk.Combobox(
    window,
    values=tuple(classes),
    font=("Arial", 14),
    width=26,
    state="normal",
)
class_entry.pack(padx=20, pady=(0, 8))

growths_label = tk.Label(
    window,
    text="Enter a character, class, or both to see growths.",
    font=("Arial", 12),
    foreground="white",
    background="#363636",
    justify=tk.LEFT,
    anchor="nw",
    wraplength=360,
)
growths_label.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)


def show_growths(_event=None) -> None:
    character_name = character_entry.get().strip()
    class_name = class_entry.get().strip()
    if not character_name and not class_name:
        growths_label.config(text="Enter a character, class, or both to see growths.")
        return

    character_growths = characters.get(character_name) if character_name else None
    class_growths = classes.get(class_name) if class_name else None
    if character_name and character_growths is None:
        growths_label.config(text=f"No character named '{character_name}' was found.")
        return
    if class_name and class_growths is None:
        growths_label.config(text=f"No class named '{class_name}' was found.")
        return

    if character_growths is not None and class_growths is not None:
        result_growths = combine(character_growths, class_growths)
        heading = f"{character_name} + {class_name} (combined growths)"
    elif character_growths is not None:
        result_growths = character_growths
        heading = f"{character_name} (character growths)"
    else:
        result_growths = class_growths
        heading = f"{class_name} (class growths)"

    growth_list = "\n".join(
        f"{stat}: {growth}%" for stat, growth in result_growths.items()
    )
    growths_label.config(text=f"{heading}\n\n{growth_list}")


search_button = tk.Button(
    window,
    text="Show Growths",
    command=show_growths,
    font=("Arial", 12),
)
search_button.pack(pady=(0, 20))
character_entry.bind("<Return>", show_growths)
class_entry.bind("<Return>", show_growths)

window.mainloop() #summons window