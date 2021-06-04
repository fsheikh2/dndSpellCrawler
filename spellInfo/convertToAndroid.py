#!/usr/local/bin/python3

def stripSpaceAndNewline(string):
	return string.replace(" ", "").replace("\n", "")

def replaceEscape(string):
	return string.replace("'","\\'").replace("’", "\\'")
# files to read from
nameFile = open('spellNames.txt')
schoolFile = open('spellSchools.txt')
levelFile = open('spellLevels.txt')
castingTimeFile = open('spellCastTimes.txt')
rangeFile = open('spellRanges.txt')
componentFile = open('spellComponents.txt')
durationFile = open('spellDurations.txt')
descriptionFile = open('spellDescriptions.txt')
pageFile = open('spellPages.txt')
classFile = open('spellClasses.txt')

# lists storing read data
names = nameFile.readlines()
schools = schoolFile.readlines()
levels = levelFile.readlines()
castingTimes = castingTimeFile.readlines()
ranges = rangeFile.readlines()
components = componentFile.readlines()
durations = durationFile.readlines()
descriptions = descriptionFile.readlines()
pages = pageFile.readlines()
classes = classFile.readlines()

#files to write to 
androidNameFile = open('AndroidVersions/androidSpellNames.txt', 'w')
androidSchoolFile = open('AndroidVersions/androidSpellSchools.txt', 'w')
androidLevelFile = open('AndroidVersions/androidSpellLevels.txt', 'w')
androidCastingTimeFile = open('AndroidVersions/androidSpellCastTimes.txt', 'w')
androidRangeFile = open('AndroidVersions/androidSpellRanges.txt', 'w')
androidComponentFile = open('AndroidVersions/androidSpellComponents.txt', 'w')
androidDurationFile = open('AndroidVersions/androidSpellDurations.txt', 'w')
androidDescriptionFile = open('AndroidVersions/androidSpellDescriptions.txt', 'w')
androidPageFile = open('AndroidVersions/androidSpellPages.txt', 'w')
androidClassFile = open('AndroidVersions/androidSpellClasses.txt', 'w')

androidRitualFile = open('AndroidVersions/androidSpellRitual.txt', 'w')
androidConcentrationFile = open('AndroidVersions/androidSpellConcentration.txt', 'w')

for i in range(len(names)):
	
	ritualIndex = names[i].find("(Ritual)")
	if(ritualIndex != -1):
		names[i]=names[i][0:ritualIndex]
		androidRitualFile.write("<item>"+"true"+"</item>\n")
	else:
		androidRitualFile.write("<item>"+"false"+"</item>\n")
	androidNameFile.write("<item>"+replaceEscape(names[i].rstrip("\n"))+"</item>\n") # was fine

	androidSchoolFile.write("<item>"+schools[i].rstrip("\n")+"</item>\n") # was fine
	androidLevelFile.write("<item>"+stripSpaceAndNewline(levels[i])+"</item>\n")
	androidCastingTimeFile.write("<item>"+castingTimes[i].replace("\n","").strip()+"</item>\n")
	androidRangeFile.write("<item>"+ranges[i].strip()+"</item>\n")
	androidComponentFile.write("<item>"+components[i].replace("\n", "").strip()+"</item>\n")
	
	androidDurationFile.write("<item>"+durations[i].replace("\n", "")+"</item>\n")
	concentraionIndex = durations[i].find("Concentration")
	if concentraionIndex != -1:
		androidConcentrationFile.write("<item>"+"true"+"</item>\n")
	else:
		androidConcentrationFile.write("<item>"+"false"+"</item>\n")

	androidPageFile.write("<item>"+replaceEscape(pages[i]).strip()+"</item>\n")

description = []
for i in range(len(descriptions)):
	if descriptions[i] != "*\n" and descriptions[i] != "Higher Level" and descriptions[i] != "\n":
		description.append(replaceEscape(descriptions[i]))
	elif descriptions[i] == "*\n":
		s = "\n".join(description)
		androidDescriptionFile.write("<item>"+s+"</item>\n")
		description=[]

classList = []
for i in range(len(classes)):
	if classes[i] != "*\n" and classes[i] != "\n" and classes[i] != "":
		classList.append(stripSpaceAndNewline( classes[i]))
	elif classes[i] == "*\n":
		s = "".join(classList)
		s = s[:len(s)-1]
		androidClassFile.write("<item>"+s+"</item>\n")
		classList = []


nameFile.close()
schoolFile.close()
levelFile.close()
castingTimeFile.close()
rangeFile.close()
componentFile.close()
durationFile.close()
descriptionFile.close()
pageFile.close()
classFile.close()

androidNameFile.close()
androidSchoolFile.close()
androidLevelFile.close()
androidCastingTimeFile.close()
androidRangeFile.close()
androidComponentFile.close()
androidDurationFile.close()
androidDescriptionFile.close()
androidPageFile.close()
androidClassFile.close()

androidRitualFile.close()
androidConcentrationFile.close()
