#!/usr/bin/python
# This code is written to work with Python 3.11
#
#   This file is part of FBI-Theme-Unistore
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import json

import os.path as path

from buildUnistoreUtils import *
from themeChecking import *

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

            # yo let's make sure this exists rq
            curThemeDirPath = path.join(curAuthorDirPath, themeName)
            if not path.isdir(curThemeDirPath):
                print("\tSkipping "+themeName+" at "+curThemeDirPath+" cause not a dir lmao")
                continue
            print("\t"+themeName)

            curThemeObj = getNewThemeObj(themeName, authorName)
            curThemeObj['Install'] = getInstallSteps(themeName, authorName)

            if checkThemeZipForThemeDir(themeName, authorName) == False:
                print("\t\tNo \'theme\' base theme dir found in theme zip, skipping")
                continue
            if checkThemeZipForOldVersion(themeName, authorName):
                print("\t\t"+"Older theme format; theme/button.png is present")

            if getThemeZipLogoSize(themeName, authorName) != (128, 128):
                print("\t\t"+"Logo size is non-standard: "+ str(getThemeZipLogoSize(themeName, authorName)))

            # Add previews if they exist
            curPreviewsDirPath = path.join(curThemeDirPath, "Previews")
            if path.isdir(curPreviewsDirPath):
                if path.isfile(path.join(curPreviewsDirPath, "P1.png")):
                    print("\t\tFound preview 1, adding to theme entry")
                    # ugly way to do this but I don't feel like changing it rn
                    curThemeObj['info']['screenshots'].append({
                        "description": "Main menu",
                        "url": getPreviewURLString(themeName, authorName, "P1.png")
                        })
                    if path.isfile(path.join(curPreviewsDirPath, "P2.png")):
                        print("\t\tFound preview 2, adding to theme entry")
                        curThemeObj['info']['screenshots'].append({
                            "description": "Browsing",
                            "url": getPreviewURLString(themeName, authorName, "P2.png")
                            })
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
