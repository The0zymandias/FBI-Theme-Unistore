import os.path as path

import os
import json

authorDirPath = path.join(os.curdir, "Authors")
storeInfoPath = path.join(os.curdir, "storeInfo.json")

def getStoreInfo() -> dict:
    with open(storeInfoPath, "r") as storeInfo:
        return json.load(storeInfo)

def getNewThemeObj(name: str, author: str) -> dict:
    return {
        'info': {
            'title': name,
            'author': author,
            'last_updated': '',
            'screenshots': []
        }
    }

def addScreenshotsToThemeObj(obj, screenshots: list[dict]) -> None:
    for screenshot in screenshot:
        obj['info']['screenshots'].append(screenshot)

def getStoreContent() -> list[dict]:

    storeContent = []

    for authorName in os.listdir(authorDirPath):

        curAuthorDirPath = path.join(authorDirPath, authorName)
        if not path.isdir(curAuthorDirPath):
            print("Skipping "+authorName+" cause not a dir lmao")
            continue
        print(authorName)

        for themeName in os.listdir(curAuthorDirPath):

            curThemeDirPath = path.join(curAuthorDirPath, themeName)
            curPreviewsDirPath = path.join(curThemeDirPath, "Previews")
            if not path.isdir(curThemeDirPath):
                print("Skipping "+themeName+" preview cause not a dir lmao")
                continue
            print("\t"+themeName)

            curThemeObj = getNewThemeObj(themeName, authorName)

            if path.isdir(curPreviewsDirPath) and path.isfile(path.join(curPreviewsDirPath, "p1.png")) and path.isfile(path.join(curPreviewsDirPath, "p2.png")):
                print("Found previews 1 and 2 for "+ themeName)



def buildStore() -> None:
    print("cwd: "+os.curdir)
    unistore = {
        ['storeInfo']: getStoreInfo(),
        ['storeContent']: getStoreContent()
    }

if __name__ == '__main__':
    buildStore()
