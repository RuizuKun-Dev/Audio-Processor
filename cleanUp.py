
import directoryUtil
import fileManager


def clearInput():
    for dir, dic in fileManager.Audio.items():
        directoryUtil.removeDir(f"Input/{dir}")


def clearOutput():
    for dir, dic in fileManager.Audio.items():
        directoryUtil.removeDir(f"Output/{dir}")
