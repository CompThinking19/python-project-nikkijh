print 'DIRECTIONS: Type your asnwer in for every blank spot in the sentence.'

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

#prints out the types of speech so the users know what kind of word is muissing from the sentence


print
print ('A1. A persons condition with regard to their {firstadjective} and {secondadjective}.' .format(
    firstadjective = '(firstadjective)' , secondadjective = '(secondadjective)'))
print
print ('A2. One in {thirdnumber} students have a diagnosable illness.' .format(
    thirdnumber = '(thirdnumber)'))
print
print ('A3. {fourthnumber} percent of students have become so anxious that they struggled in school.' .format(
    fourthnumber = '(fourthnumber)'))
print
print ('A4. There are three main kinds of symptoms for depression: {fifthadjective} symptoms, {sixthadjective} symptoms, and {seventhadjective} symptoms.' .format(
    fifthadjective = '(fifthadjective)' , sixthadjective = '(sixthadjective)' , seventhadjective = '(seventhadjective)'))

#This will print out the sentence with the blank so people can try to fill it in with what they think the correct answer is
#I want people to read these facts about mental health and try to fill in the missing parts to test their knowledge abnout this subject because not many people take it serious

print
print
print
print
print
print
print
print
print
print
print
print
#these prints will add a new blank line between each sentence and so the answers are further down and not right next to the quiz part
print 'CORRECT ANSWERS ARE LISTED BELOW'
#This will print out the statement to tell them the correct answers are listed below so they can compare answers
print

print ('B1. A persons condition with regard to their {firstadjective} and {secondadjective}.' .format(
    firstadjective = 'psychological' , secondadjective = 'emotional'))
print
print ('B2. One in {thirdnumber} students have a diagnosable illness.' .format(
    thirdnumber = 'four'))
print
print ('B3. {fourthnumber} percent of students have become so anxious that they struggled in school.' .format(
    fourthnumber = 'Fifty'))
print
print ('B4. There are three main kinds of symptoms for depression: {fifthadjective} symptoms, {sixthadjective} symptoms, and {seventhadjective} symptoms.' .format(
    fifthadjective = 'physical' , sixthadjective = 'emotional' , seventhadjective = 'thinking'))

#This will print out the sentence with the correct answers and then can be compared to what they thought the answer was
#After they submitted their answers, I want them to see the correct answers to see how close they were to answering it correctly and it will show how much they know. Hopefully by seeing teh correct facts about mental health, it will make them realixe more on how import mental health is
