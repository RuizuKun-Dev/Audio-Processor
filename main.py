import fileManager
import extractZip
import cleanUp
from time import sleep
print("Start...")


extractZip.extractZipFiles()

print("Extract...")

fileManager.copyFilesToOutput()

print("Convert...")

extractZip.archiveFiles()

print("Archive...")

cleanUp.clearInput()


