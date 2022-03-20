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

# if input("Press Enter Y/N to confirm Input and Output deletion") == "y":
#     cleanUp.clearInput()
#     cleanUp.clearOutput()
# else:
#     if input("Press Enter Y/N to confirm Input deletion") == "y":
#         cleanUp.clearInput()

#     if input("Press Enter Y/N to confirm Output deletion") == "y":
#         cleanUp.clearOutput()
