import glob
import os
import shutil
import threading

import directoryUtil


def extractZipFiles():
    threads = []
    for file in os.scandir("Input"):
        if not directoryUtil.getDir(file.path.replace(".zip", "")):
            if file.path.endswith(".zip"):
                print("extracting " + file.path)
                thread = threading.Thread(target=shutil.unpack_archive, args=(
                    file.path, file.path.replace(".zip", ""), "zip"))
                threads.append(thread)
                thread.start()

    for thread in threads:
        thread.join()


def archiveFiles():
    for file in os.scandir("Output"):
        if not file.path.endswith(".pdf"):
            fileName = file.path.replace("Output\\", "")
            if not directoryUtil.getDir(file.path + "\\" + fileName + ".zip"):
                print("archiving " + fileName)
                shutil.make_archive(file, "zip", file.path)

    for file in glob.glob("Output/*.zip", recursive=True):
        shutil.move(file, file.replace(".zip", "\\"))
