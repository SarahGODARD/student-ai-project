import json
import sys
import os
import unicodedata
import random
import csv
import pandas as pd

directory = "../annonces/"
csv_path = "../dataCsv/data.csv"

# get the file from filename
def getFile(fileName):
    return open(directory + fileName, "r", encoding="utf-8")

# turn file to dictionnary
def fileTextToDictionnary(fileText):
    return json.load(fileText)

# get and return a file
def getFileList():
    return os.listdir(directory)

# get the annonces from the jon file at the top of the code
def getAnnonceDict(fileList):
    Dict = {} 
    for fileName in fileList:
        fileText = getFile(fileName)
        fileDictionnary = fileTextToDictionnary(fileText)
        for e in fileDictionnary:
            prout = {}
            for cath in fileDictionnary[e]:
                title = cath
                res = str(fileDictionnary[e][cath])
                res = res.replace(",", "")
                res = res.replace("€", "")
                prout[title] = res
            Dict[e]= prout
    return Dict

# print the dictionnary given as parameter
def printDict(Dict):
    for elem in Dict:
        for cath in Dict[elem]:
            print(cath, Dict[elem][cath])

# create fake state for scam
def fakeScam(Dict):
    for elem in Dict:
        r = random.randint(0,1)
        Dict[elem]["state"] = False
        if r == 0:
            Dict[elem]["state"] = True
    return Dict

def dictToDf(Dict):
    columns = []
    df = pd.DataFrame()
    df = pd.DataFrame(Dict)
    return df.transpose()

def writeInCsv(df, csvfile):
    df.to_csv(csvfile, index= False)

if __name__ == "__main__":
    print("Getting file...")
    fileList = getFileList()
    print("Filling the directory...")
    Dict = getAnnonceDict(fileList)
    # Dict = fakeScam(Dict)
    print("Creating and filling csv...")
    csvfile = open(csv_path, "w", encoding="utf-8", newline='')
    df = dictToDf(Dict)
    writeInCsv(df, csvfile)
    print(Dict["-M3uYKRQkY203aEyqm9U"])
    print("The program ended well.")
