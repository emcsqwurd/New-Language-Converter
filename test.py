import numpy as np
from func import convertStringToNewLanguage, convertNewStringToStandardString




def testNewLanguageImplementation():
    print("Enter sentence to be converted to the new Language:")
    string = input()
    newString = convertStringToNewLanguage(string)
    print("Input words in new language reads:")
    print(newString)
    print("would you like to convert the new language sentence back to original? Type YES or NO below:")
    answer = input()
    if answer == str("YES"):
        print("New String converted back to original string below:")
        print(convertNewStringToStandardString(newString))
    if answer == str("NO"):
        print("Enjoy new language implementation!")    
    return 
print(testNewLanguageImplementation())




