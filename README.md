honestly this is just a test for me messing with data scrapers with some minor practical use

if you somehow stumble upon this hi

## Character growth checker

Run `python main.py` to open the Tkinter window. Choose a character or class
from its drop-down list, type a name directly, or provide both, then select
**Show Growths** or press Enter to display HP, Str, Mag, Spd, Dex, Def, Res,
Lck, and Cha growth rates. Searching for both displays the sum of the character
and class growth rates for each stat. The script fetches character and class
data from Serenes Forest at startup, so an internet connection is required.

The script requires `requests` and `beautifulsoup4`; Tkinter is included with
most Python installations.