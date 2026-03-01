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

import urllib.parse as urlparse

def getNewThemeObj(name: str, author: str) -> dict:
    return {
        'info': {
            'title': name,
            'author': author,
            "version": "v1",
            "category": ["theme"],
            "console": ["3DS"],
            "description": "Tap on the photo icon on the bottom of your screen to see a preview",
            'last_updated': '',
            'screenshots': []
        }
    }

def getInstallSteps(themeName, authorName) -> list[dict]:
    return [
            {
                "type": "downloadFile",
                "file": "https://github.com/The0zymandias/FBI-Theme-Unistore/raw/refs/heads/main/Authors/"+urlparse.quote(authorName)+"/"+urlparse.quote(themeName)+"/theme.zip",
                "output": "sdmc:/fbi-theme.zip"
            },
            {
                "type": "mkdir",
                "directory": "sdmc:/fbi/",
            },
            {
                "type": "extractFile",
                "file": "sdmc:/fbi-theme.zip",
                "input": "",
                "output": "sdmc:/fbi/"
            },
            {
                "type": "deleteFile",
                "file": "sdmc:/fbi-theme.zip"
            }

        ]

def getPreviewURLString(themeName: str, authorName: str, previewFileName: str) -> str:
    return "https://github.com/The0zymandias/FBI-Theme-Unistore/raw/refs/heads/main/Authors/"+urlparse.quote(authorName)+"/"+urlparse.quote(themeName)+"/Previews/"+urlparse.quote(previewFileName)

def addClearFBIThemeOption(storeContent: list) -> None:
    clearThemeObj = getNewThemeObj("Reset to Default Theme", "Ozymandias")
    clearThemeObj['info']['category'][0] = 'utility'
    clearThemeObj['info']['last_updated'] = '2/22/26'
    clearThemeObj['Clear'] = [
        {
            "type": "rmdir",
            "directory": "sdmc:/fbi/theme"
        }
    ]
    storeContent.append(clearThemeObj)
