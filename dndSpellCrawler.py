#!/usr/local/bin/python3

import requests, bs4, time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def getSpellLinks(browser, spellLinksSelector):
	listOfLinks = []
	try:
		spellLinks = browser.find_elements_by_css_selector(spellLinksSelector)
		for spellLink in spellLinks:
			listOfLinks.append(spellLink.get_attribute('href'))
	except:
		print('getSpellLinks Message: No Links Found :/ \n\n')
		
	return listOfLinks

# issue is "At higher levels" sections get stored separately from rest of description, causing the size of the list to go from 5 to 6
def scrapeSpells(link):
	spellInfo = []
	spellPage = requests.get(link)
	spellPage.raise_for_status()
	spellSoup = bs4.BeautifulSoup(spellPage.text, features='lxml')
	fullInfo = spellSoup.select('div.col-md-12 > p')
	
	name = spellSoup.select('h1.classic-title > span')
	spellInfo.append(name[0].text)

	for i in range(len(fullInfo)-1):
		if i == 1:
			vitalInfo = fullInfo[i].text
			split = vitalInfo.split("Level: ")
			
			split = split[1].split("Casting time: ")
			level = "".join(split[0].splitlines())
			
			split = split[1].split("Range: ")
			castingTime = "".join(split[0].splitlines())
			
			split = split[1].split("Components: ")
			sRange = "".join(split[0].splitlines())
			
			split = split[1].split("Duration: ")
			components ="".join(split[0].splitlines())
			duration = split[1]
			
			spellInfo.append(level)
			spellInfo.append(castingTime)
			spellInfo.append(sRange)
			spellInfo.append(components)
			spellInfo.append(duration)

		elif i > 2 and len(fullInfo) == 6:
			if i == 3:
				pageInfo = fullInfo[i].text
				pageInfo = pageInfo.split("Page: ")[1]
				pageInfo = pageInfo.rstrip(" ")
				spellInfo.append(pageInfo)

			elif i == 4:
				classInfo = fullInfo[i].text
				classInfo = classInfo.split("A")[1].split("spell")[0]
				spellInfo.append(classInfo)

		elif i > 2 and len(fullInfo) == 7:
			if i == 3:
				higherLevel = fullInfo[i].text
				higherLevel = "".join(higherLevel.splitlines())
				spellInfo.append(higherLevel)
			elif i == 4:
				pageInfo = fullInfo[i].text
				pageInfo = pageInfo.split("Page: ")[1]
				pageInfo = "".join(pageInfo.splitlines())
				spellInfo.append(pageInfo)

			elif i == 5:
				classInfo = fullInfo[i].text
				classInfo = classInfo.split("A")[1].split("spell")[0]
				spellInfo.append(classInfo)

		else:
			spellInfo.append(fullInfo[i].text)

	return spellInfo

print("\n\n")

browser = webdriver.Firefox()
browser.get('https://www.dnd-spells.com/spells')
time.sleep(5)


# Set up selectors that will be used multiple times
resetSelector = "a#reset_table"

try:
	resetButton = browser.find_element_by_css_selector(resetSelector)
	resetButton.click()
except: 
	print("Reset Button Not Found :/ \n\n")



# grab level list element 
try:
	selector = "div.column-filter-widget.col-lg-2 select"
	levelList = browser.find_element_by_css_selector(selector)
	print(type(levelList))
	levelListSelector = Select(levelList)
except:
	print("First: No matches :/ \n\n")

print("Heres' the PAGE SOURCE Type: " + str(type(browser.page_source)))

nameFile = open('spellInfo/spellNames.txt', 'w')
schoolFile = open('spellInfo/spellSchools.txt', 'w')
levelFile = open('spellInfo/spellLevels.txt', 'w')
castingTimeFile = open('spellInfo/spellCastTimes.txt', 'w')
rangeFile = open('spellInfo/spellRanges.txt', 'w')
componentsFile = open('spellInfo/spellComponents.txt', 'w')
durationFile = open('spellInfo/spellDurations.txt', 'w')
descriptionFile = open('spellInfo/spellDescriptions.txt', 'w')
pageFile = open('spellInfo/spellPages.txt', 'w')
classFile = open('spellInfo/spellClasses.txt', 'w')


# set the filter from 1-9 one by one to get spells organized by level on site
try:
	startTime = time.time()
	for i in range(0,10):
		print("\n\t\tADDING FROM LEVEL " + str(i) + "\n\n")

		levelListSelector.select_by_value(str(i))
		selector="a.filter-term"
		choosenLevel = browser.find_element_by_css_selector(selector) # click on this to clear old filter
		

		# Grab all links in current spell level
		spellLinksSelector = "tbody > tr > td > a:nth-child(1)"
		listOfLinks = getSpellLinks(browser, spellLinksSelector)
		
		# Use BS to visit each link and scrape the relevant info
		i = 0
		for link in listOfLinks:
			returnedInfo = scrapeSpells(link)
		
			# Write the scraped info to relevant files
			nameFile.write(returnedInfo[0]+"\n")
			schoolFile.write(returnedInfo[1]+"\n")
			levelFile.write(returnedInfo[2]+"\n")
			castingTimeFile.write(returnedInfo[3]+"\n")
			rangeFile.write(returnedInfo[4]+"\n")
			componentsFile.write(returnedInfo[5]+"\n")
			durationFile.write(returnedInfo[6])
			
			if(len(returnedInfo) == 10):
				descriptionFile.write(returnedInfo[7]+"\n*\n")
				pageFile.write(returnedInfo[8]+"\n")
				classFile.write(returnedInfo[9]+"\n*\n")
			else:
				descriptionFile.write(returnedInfo[7] + "\nHigher Level\n" +returnedInfo[8]+"\n*\n")
				pageFile.write(returnedInfo[9]+"\n")
				classFile.write(returnedInfo[10]+"\n*\n")
			
		# Remove current filter in place to ready up for next filter selection
		choosenLevel.click()

except Exception as e:
	print("Second: No matches :/ \n\n")
	print(e)
	print("\n\n")

finally:
	print("\n\tTotal time elapsed: " + str(time.time()-startTime) + "\n")
	nameFile.close()
	schoolFile.close()
	levelFile.close()
	castingTimeFile.close()
	rangeFile.close()
	componentsFile.close()
	durationFile.close()
	descriptionFile.close()
	pageFile.close()
	classFile.close()

	browser.quit() # shuts down everything, .close() would only close window focus was on at time of call
