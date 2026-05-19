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

import zipfile
import tempfile

from os import path
from PIL import Image

def checkThemeZipForThemeDir(themeName: str, authorName: str) -> bool:
    zipPath = path.join("Authors", authorName, themeName, "theme.zip")
    with zipfile.ZipFile(zipPath, "r") as themeZip:
        return zipfile.Path(themeZip, at='theme/').is_dir()
        # return "theme/" in themeZip.namelist() or "theme" in themeZip.namelist() or "theme\\" in themeZip.namelist()

def checkThemeZipForOldVersion(themeName: str, authorName: str) -> bool:
    zipPath = path.join("Authors", authorName, themeName, "theme.zip")
    with zipfile.ZipFile(zipPath, "r") as themeZip:
        return zipfile.Path(themeZip, at='theme/button.png').is_file()

def getThemeZipLogoSize(themeName: str, authorName: str) -> tuple:
    zipPath = path.join("Authors", authorName, themeName, "theme.zip")

    with zipfile.ZipFile(zipPath, "r") as themeZip:
        if not zipfile.Path(themeZip, at='theme/logo.png').is_file():
            return (-1, -1)

        with tempfile.TemporaryFile() as pngFile:
            pngFile.write(themeZip.read("theme/logo.png"))
            pngFile.seek(0)
            with Image.open(pngFile) as img:
                return img.size


