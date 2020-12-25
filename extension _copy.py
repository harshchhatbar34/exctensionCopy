import shutil
import os
import sys

sourceFolder = sys.argv[1]

fileDict = {
    '.txt':'textFile',
    '.png':'pngFile',
    '.pdf':'pdfFile'
}

for file in os.listdir(sourceFolder):
    filename,fileExtension = os.path.splitext(file)
    if fileExtension in fileDict.keys():
        destFolderName = os.path.join(sys.argv[2], fileDict[fileExtension])
        if not os.path.exists(destFolderName):
            os.makedirs(destFolderName)
        shutil.copy(os.path.join(sourceFolder, file), destFolderName)


