from pydub import AudioSegment
import glob
import shutil
import threading
import re

import directoryUtil

Audio = {}


def __scanForAudio(TYPE, EXTENTION):
    for path in glob.iglob(f"**/*{EXTENTION}", recursive=True):
        dirName = path.split("\\")[1]
        name = path.split("\\")[-1].replace(f"{EXTENTION}", "")

        if not Audio.get(dirName):
            Audio[dirName] = {}

        if not Audio[dirName].get(f"{TYPE}"):
            Audio[dirName][f"{TYPE}"] = {}

        Audio[dirName][f"{TYPE}"][name] = path


def __scanForALLAudio():
    __scanForAudio("WAV", ".wav")
    __scanForAudio("MP3", ".mp3")
    __scanForAudio("OGG", ".ogg")


def __convertToMP3(dic, path, dir, name):
    print(f"converting {name} to .mp3")
    AudioSegment.from_wav(path).export(
        f"Input/{dir}/{name}.mp3", format="mp3")
    dic["MP3"][name] = f"Input/{dir}/{name}.mp3"


def __convertToOGG(dic, path, dir, name):
    print(f"converting {name} to .ogg")
    AudioSegment.from_wav(path).export(
        f"Input/{dir}/{name}.ogg", format="ogg")
    dic["OGG"][name] = f"Input/{dir}/{name}.ogg"


def __convertFromWAV():
    __scanForALLAudio()
    threads = []
    for dir, dic in Audio.items():
        if not dic.get('MP3'):
            dic["MP3"] = {}

        if not dic.get("OGG"):
            dic["OGG"] = {}

        if dic.get("WAV"):
            for name, path in dic["WAV"].items():
                if not dic["MP3"].get(name):
                    # print(f"Converting {name} to .mp3")
                    thread = threading.Thread(
                        target=__convertToMP3, args=(dic, path, dir, name))
                    threads.append(thread)
                    thread.start()

                if not dic["OGG"].get(name):
                    # print(f"Converting {name} to .ogg")
                    thread = threading.Thread(
                        target=__convertToOGG, args=(dic, path, dir, name))
                    threads.append(thread)
                    thread.start()

    for thread in threads:
        thread.join()


PDF = []


def __scanForPDF():
    for path in glob.iglob("**/*.pdf", recursive=True):
        PDF.append(path)


def __copyPFDFiles():
    __scanForPDF()
    for path in PDF:
        if not directoryUtil.getDir(path.replace("Input", "Output")):
            shutil.copy(path, path.replace(
                "Input", "Output").replace(".pdf", ""))


def __copyAudioFiles():
    __convertFromWAV()
    for dir, dic in Audio.items():
        directoryUtil.createDir(f"Output/{dir}")
        for type, files in dic.items():
            for name, path in files.items():
                if len(files.keys()) == 1:
                    if not directoryUtil.getDir(path.replace("Input", "Output")):
                        name = re.sub('\W+', ' ', name).replace("_", " ")
                        shutil.copy(
                            path, f"Output/{dir}/{name}.{type.lower()}")
                else:
                    directoryUtil.createDir(f"Output/{dir}/{type}")
                    for name, path in files.items():
                        if not directoryUtil.getDir(path.replace("Input", "Output")):
                            name = re.sub('\W+', ' ', name).replace("_", " ")
                            shutil.copy(
                                path, f"Output/{dir}/{type}/{name}.{type.lower()}")


def copyFilesToOutput():
    __copyAudioFiles()
    __copyPFDFiles()
