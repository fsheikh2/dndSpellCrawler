This is a simple web crawler program made to get info on spells for D&D 5e from two main online sources. 

Using the "dndSpellCrawler.py" script gets the data on all spells loaded into individual text files based on spell names, schools, levels, casting times, range, components, durations, descriptions, page number location, and classes.

Then you can go into the spellInfo directory and use the "converToAndroid.py" script to take the info from all those files generated above and format them into new files that can be used as resources for an Android app. I used this to create a personal use app that lets me easily browse and filter the large list of spells.

These scripts depend on the bs4, time, and selenium libraries. You will need them for the program to work. 