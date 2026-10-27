honestly this is just a test for me messing with data scrapers with some minor practical use

if you somehow stumble upon this hi

## Character growth checker

Run `python main.py` to open the Tkinter window. Enter a character's name as it
appears in the scraped character list, then select **Show Growths** or press
Enter to display their HP, Str, Mag, Spd, Dex, Def, Res, Lck, and Cha growth
rates. The script fetches character and class data from Serenes Forest at
startup, so an internet connection is required.

The script requires `requests` and `beautifulsoup4`; Tkinter is included with
most Python installations.