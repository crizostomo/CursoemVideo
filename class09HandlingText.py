#len() --> it counts how many characters that there are
#count('o') --> it counts every letter 'o'
#find('dem') --> it finds the charac
#replace(dem, med)
#upper()
#lower()
#capitalize() --> it capitalizes just the first characters
#title() --> it capitalizes every characters
#strip () --> it removes useless spaces
#rstrip() --> it removes just spaces in the right
#lstrip() --> it removes just spaces in the left
#'-'.join() --> it joins putting '-' in the middle
#split() --> it divides spaces in a String --> each word
#receives a new beginnig, each element will be divided in a list

phrase = " Curso em Video Python "
print(phrase[13:])
print(phrase[3])
print(phrase[3:13])
print(phrase[1:15:2])
print(phrase[1::3])
print(phrase.count('o'))
print(phrase.upper().count('O'))
print(len(phrase))
print(len(phrase.strip()))
print(phrase.replace('Python', 'Android'))
print(phrase[5])
print('curso' in phrase)
print(phrase.split())
divided = phrase.split()
print(divided[1])
print(divided[2][3])






#to print a long text in several lines, """ + """




