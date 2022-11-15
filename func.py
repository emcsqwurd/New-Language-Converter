from ast import Not
from pickle import TRUE
#from pickle import FALSE
import numpy as np
from dict import newAlphabet, newAlphabetInvert





"""Function to convert an input string into a list containing the composite 
letters of said string"""
def convertStringToListOfLetters(string):
    oldList = []
    for letter in string:
        oldList.append(letter)
    return oldList
#print(convertStringToListOfLetters("hello world"))


"""Function to convert the list of letters of input string into a new list of 
letters of new language, through the use of dictionary"""
def convertLettersListToNewLettersList(string):
    newList = []
    listOldLetters = convertStringToListOfLetters(string)
    for letter in listOldLetters:
        newLetters = newAlphabet[letter]
        newList.append(newLetters)
    return newList
#print(convertLettersListToNewLettersList("helloworld"))    


"""Function to convert the list of new language letters into a string to be output"""
def convertStringToNewLanguage(string):
    finalstring = ""
    newLetterList = convertLettersListToNewLettersList(string)
    for letter in newLetterList:
        finalstring += letter
    return finalstring
#print(convertNewListLettersToNewString("helloworld"))    



#------------------NEW GOING BACKWARDS------------

"""Function to convert the list of new letters into a list of letters corresponding
to input string back to standard alphabet implementation"""

#two possible problems may arise:
#(1): may pick up letter before actual letter is recognised (i.e i and h)
#(2): once there is a match it must be removed from the list and loop ran again,
#---This 're-startiing' is neccessary for the correct detection of letters


def convertNewLetterListToStandardList(newString):
    listNewLanguage = convertStringToListOfLetters(newString)
    
    #e.g [1,2,3,4] = [[1],[1,2],[1,2,3],[1,2,3,4]] - many lists in one list
    newList = []
    for sym in range(0, len(listNewLanguage) - 1):
        desiredTerms = listNewLanguage[:sym + 1]
        newList.append(desiredTerms)
    print("newList:")
    print(newList) 

    #joining the items within each sublist together
    finalList = []
    for listGroup in newList:
        finalTerms = ''.join(listGroup)
        finalList.append(finalTerms)  
    print("finalList:")
    print(finalList)     
    
    #then trying when matches with item in invert dictionary, append to list
    possList = []
    for possNewLetter in finalList:
        if possNewLetter in newAlphabetInvert:
            possList.append(possNewLetter)
    print("possList:")
    print(possList)         
       

    #
    testList = []
    for char in finalList:
        for char2 in possList:
            if char2 in char:
                testitem = char.replace(char2, '')
                testList.append(testitem)
            #if len(char) >= len(char2):
                
    maybeList = []            
    for choice in testList:
        if choice in newAlphabetInvert:
            maybeList.append(choice)



            

    #using Invert dictionary to now append standard alphabet letters of input word to list
    itemList = []
    for item in possList:
        final = newAlphabetInvert[item]
        itemList.append(final)


    






    """Trying: if english dictionary element is determined in list,
    find another element of same list that has that 'symbol' as a composite
    of another item, then remove the previously determined symbol
    from that composite item

    resList = []
    for choice in range(0, len(itemList) - 1):
        if itemList[choice] in itemList[choice + 1]:
            res = itemList.remove(choice) in itemList[choice + 1]
            resList.append(res)
            """
    
    print("final output: itemList")
    return itemList, testList, maybeList
#print(convertNewLetterListToStandardList("|‾||x||._|._|.x"))



"""Function to convert list of letters of standard alphabet back into standard 
alphabet string"""
def convertNewStringToStandardString(string):
    finalstring = ""
    letterList = convertNewLetterListToStandardList(string)
    for letter in letterList:
        finalstring += letter
    return finalstring

