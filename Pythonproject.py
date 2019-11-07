import re
#importing the regex module
def getwordtypes (text):
    #function to get the types of speech
    result = re.findall(r'%\w*\b', text)
    #finds all the words in text with % in front of it
    result = map(removeprefix, result)
    #uses the removeprefix function on every element of result
    return result
    #returns the result

def removeprefix(element):
    #function to remove the % symbol in front of the word
    return element[1:]
    #returns the substring starting at the 2nd character of the word

file = open("story.txt", "r")
#opens the text file for reading
textfile = file.read()
#reads the file
typesofspeech = getwordtypes(textfile)
#calls getwordtypes on the textfile
print typesofspeech
#prints out the types of speech 
