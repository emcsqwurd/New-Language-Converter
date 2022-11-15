from asyncore import read
from func import convertStringToNewLanguage, convertNewStringToStandardString
import sys, os
import codecs





#-----Reading Text documents to translate into New Language-----

def readDoc(path):
    doc = open(path, 'r') #open text document
    with doc as file:
        text = file.read().rstrip()
    doc.close()
    return text


def convert(path):
    text = readDoc(path)
    translation = convertStringToNewLanguage(text)
    print(translation)
    print(sys.getfilesystemencoding())
    newFile = open('convertedText.txt', 'w')
    return newFile
    

def test():
    print("Enter document.txt to be considered:")
    path = input()
    print("Enter 'YES' to convert document to new language:")
    if input() == "YES": 
        print("")
        print("Input .txt document reads:")
        print(readDoc(path))
        convert(path)
    return 
print(test())





