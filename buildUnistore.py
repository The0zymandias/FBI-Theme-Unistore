# This code is written to work with Python 3.11

import os
import json

import os.path as path

from buildUnistoreUtils import *

authorDirPath = path.join(os.curdir, "Authors")
storeInfoPath = path.join(os.curdir, "storeInfo.json")

def getStoreInfo() -> dict:
    with open(storeInfoPath, "r") as storeInfo:
        return json.load(storeInfo)

def getStoreContent() -> list[dict]:

    storeContent = []
    addClearFBIThemeOption(storeContent)

    for authorName in os.listdir(authorDirPath):

        curAuthorDirPath = path.join(authorDirPath, authorName)
        if not path.isdir(curAuthorDirPath):
            print("Skipping "+authorName+" cause not a dir lmao")
            continue
        print(authorName)

        for themeName in os.listdir(curAuthorDirPath):

            # Creating install option/unistore entry
            curThemeDirPath = path.join(curAuthorDirPath, themeName)
            if not path.isdir(curThemeDirPath):
                print("\tSkipping "+themeName+" at "+curThemeDirPath+" cause not a dir lmao")
                continue
            print("\t"+themeName)

            curThemeObj = getNewThemeObj(themeName, authorName)
            curThemeObj['Install'] = getInstallSteps(themeName, authorName)

            # Add previews if they exist
            curPreviewsDirPath = path.join(curThemeDirPath, "Previews")
            if path.isdir(curPreviewsDirPath) and path.isfile(path.join(curPreviewsDirPath, "p1.png")) and path.isfile(path.join(curPreviewsDirPath, "p2.png")):
                print("\t\tFound previews 1 and 2, adding them to theme entry")
                curThemeObj['info']['screenshots'].append(getPreviewURLString(themeName, authorName, "P1.png"))
                curThemeObj['info']['screenshots'].append(getPreviewURLString(themeName, authorName, "P2.png"))
            else:
                print("\t\tCouldn't find previews")

            storeContent.append(curThemeObj)

    print("Total store entries: "+str(len(storeContent)))
    return storeContent

def buildStore() -> None:
    unistore = {
        'storeInfo': getStoreInfo(),
        'storeContent': getStoreContent()
    }
    with open('fbi-themes.unistore', "w") as storeFile:
        json.dump(unistore, storeFile, indent=4)

if __name__ == '__main__':
    buildStore()
