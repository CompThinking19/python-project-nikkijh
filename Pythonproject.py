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







print ('A1. A persons condition with regard to their {oneadjective} and {twoadjective}.' .format(
    oneadjective = '(oneadjective)' , twoadjective = '(twoadjective)'))
print ('A2. One in {threenumber} students have a diagnosable illness.' .format(
    threenumber = '(threenumber)'))
print ('A3. {fournumber} percent of students have become so anxious that they struggled in school.' .format(
    fournumber = '(fournumber)'))
print ('A4. There are three main kinds of symptoms for depression: {fiveadjective} symptoms, {sixadjective} symptoms, and {sevenadjective} symptoms.' .format(
    fiveadjective = '(fiveadjective)' , sixadjective = '(sixadjective)' , sevenadjective = '(sevenadjective)'))

#This will print out the sentence with the blank so people can try to fill it in with what they think the correct answer is
#I want people to read these facts about mental health and try to fill in the missing parts to test their knowledge abnout this subject because not many people take it serious








print 'Correct answers are listed below'
print ('B1. A persons condition with regard to their {oneadjective} and {twoadjective}.' .format(
    oneadjective = 'psychological' , twoadjective = 'emotional'))
print ('B2. One in {threenumber} students have a diagnosable illness.' .format(
    threenumber = 'four'))
print ('B3. {fournumber} percent of students have become so anxious that they struggled in school.' .format(
    fournumber = 'Fifty'))
print ('B4. There are three main kinds of symptoms for depression: {fiveadjective} symptoms, {sixadjective} symptoms, and {sevenadjective} symptoms.' .format(
    fiveadjective = 'physical' , sixadjective = 'emotional' , sevenadjective = 'thinking'))

    #This will print out the sentence with the correct answers and then can be compared to what they thought the answer was
# after they submitted their answers, I want them to see the correct answers to see how close they were to answering it correctly and it will show how much they know. Hopefully by seeing teh correct facts about mental health, it will make them realixe more on how import mental health is
