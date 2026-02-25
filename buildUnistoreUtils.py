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
