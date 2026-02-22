import os
import json

import os.path as path
import urllib.parse as urlparse

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

def getInstallSteps(themeName, authorName) -> list[dict]:
    return [
            {
                "type": "downloadFile",
                "file": "https://raw.githubusercontent.com/The0zymandias/FBI-Theme-Unistore/raw/refs/heads/main/Authors/"+urlparse.quote(authorName)+"/"+urlparse.quote(themeName)+"/theme.zip",
                "output": "sdmc:/fbi-theme.zip"
            },
            {
                "type": "mkdir",
                "directory": "sdmc:/fbi/",
            },
            {
                "type": "rmdir",
                "directory": "sdmc:/fbi/theme",
            },
            {
                "type": "extractFile",
                "file": "sdmc:/fbi-theme.zip",
                "input": "",
                "output": "sdmc:/fbi/"
            }

        ]


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
                print("\tSkipping "+themeName+" at "+curThemeDirPath+" cause not a dir lmao")
                continue
            print("\t"+themeName)

            curThemeObj = getNewThemeObj(themeName, authorName)

            if path.isdir(curPreviewsDirPath) and path.isfile(path.join(curPreviewsDirPath, "p1.png")) and path.isfile(path.join(curPreviewsDirPath, "p2.png")):
                print("\tFound previews 1 and 2 for "+ themeName)
                # TODO: code this

            curThemeObj['Install'] = getInstallSteps(themeName, authorName)

            storeContent.append(curThemeObj)

    return storeContent

def buildStore() -> None:
    print("cwd: "+os.curdir)
    unistore = {
        'storeInfo': getStoreInfo(),
        'storeContent': getStoreContent()
    }
    with open('fbi-themes.unistore', "w") as storeFile:
        json.dump(unistore, storeFile, indent=4)

if __name__ == '__main__':
    buildStore()
