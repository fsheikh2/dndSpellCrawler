#!/usr/local/bin/python3

import requests, bs4, time
from selenium import webdriver

'''
res = requests.get("https://roll20.net/compendium/dnd5e/Spells%20List#content")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features='html.parser')

#body = soup.select('div[class="body"]')
#body = soup.select('div[class="list-content"]')
body = soup.select('div > div[class="header inapp-hide single-hide"]')
print(len(body))

#for i in range(10):
#	print(body[i])

print(body[0])
'''

'''
CSS SELECTOR Reference 

Selector 			Example		Example Description
#id					#firstname	Selects the element with id="firstname"
*					*			Selects all elements
element				p			Selects all <p> elements
element.class		p.intro		Selects all <p> elements with class="intro"
element,element		div, p		Selects all <div> elements and all <p> elements
element element		div p		Selects all <p> elements inside <div> elements
element>element		div > p		Selects all <p> elements where the parent is a <div> element
element+element		div + p		Selects all <p> elements that are placed immediately after <div> elements
'''


browser = webdriver.Firefox()
#print(type(browser))
browser.get("https://roll20.net/compendium/dnd5e/Spells%20List#content")

try: 
	time.sleep(3)
	selector = '[data-col-name="Level"]'
	levelFilterButton = browser.find_element_by_css_selector(selector)
	levelFilterButton.click()
except:
	print("First: No Level Element found :/ \n\n")


try:
	selector = "div.dropdown-toggle"
	dropDownElems = browser.find_element_by_css_selector(selector)	
	dropDownElems.click()
	time.sleep(1)
except:
	print("Second: No such element found :/\n\n")

source = browser.page_source

soup = bs4.BeautifulSoup(source, 'lxml')
ulElems = soup.select('div > ul')
'''
if len(ulElems) > 0:
	for ulElem in ulElems:
		h3s=ulElem.select('h3')
		#print(h3s)
		liElems = ulElem.select('li')
		for liElem in liElems:
			print(liElem)
'''
names = soup.select('a[name]')
liElems = soup.select('div > ul > li')
for name in names:
	print(name.text)
'''
for liElem in liElems:
	print(liElem.text)
	print("\n\n")
	'''