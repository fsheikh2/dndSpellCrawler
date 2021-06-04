#!/usr/local/bin/python3

print("\n names unique in fullSpellNames, i.e. those missing from Roll20 \n\n")
file1 = open("fullSpellNames.txt")
file2 = open("roll20SpellNames.txt")

namesList1 = file1.readlines()
namesList2 = file2.readlines()

print("Full Spell List Len: " + str(len(namesList1)))
print("Roll20 Spell List Len: " + str(len(namesList2)))


missing = []
for i in range(0, len(namesList1)):
	match = False
	for j in range(0, len(namesList2)):
		name1 = namesList1[i].strip(" ")
		name1 = name1.lower()
		name2 = namesList2[j].strip(" ")
		name2 = name2.lower()
		if name1 == name2:
			match = True
	if(not match):
		missing.append(namesList1[i])
		print(namesList1[i])


print("\nMissing number of names is " + str(len(missing)) + "\n\n")