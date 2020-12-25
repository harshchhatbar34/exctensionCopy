import shutil
import os
import sys

sourceFolder = sys.argv[1]

fileDict = {
    '.txt':'textFile',
    '.png':'pngFile',
    '.pdf':'pdfFile'
}
if __name__ == "__main__":
    sourceFolder = sys.argv[1]
    for file in os.listdir(sourceFolder):
        filename,fileExtension = os.path.splitext(file)
        if fileExtension in fileDict.keys():
            destFolderName = os.path.join(sys.argv[2], fileDict[fileExtension])
            if not os.path.exists(destFolderName):
                os.makedirs(destFolderName)
            print("Copping: {} to {}".format(os.path.join(sourceFolder, file), destFolderName))
            shutil.copy(os.path.join(sourceFolder, file), destFolderName)



