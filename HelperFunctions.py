""" 
Sparar funktioner jag kanske vill ha igen
Men hur fan importerar jag dem!!?
"""

# data = {'firstline', 'secondline', ... }
with open("copyRelativePath") as f:
    data = f.read()
    data = data.splitlines()

# check letter value a-z = 1-26, A-Z = 27-52
def getLetterValue(string: str):
    if string.isupper(): letterValue = ord(string) -38
    else: letterValue = ord(string) -96
    return letterValue