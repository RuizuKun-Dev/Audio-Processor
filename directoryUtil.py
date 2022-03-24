import os

def createDir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def getDir(path):
    if os.path.exists(path):
        return path
    return None


def removeDir(path):
    if os.path.exists(path):
        os.system('rmdir /S /Q "{}"'.format(path))
