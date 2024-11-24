import time
from win32com.client import Dispatch

v = Dispatch("SAPI.SpVoice")

x = time.localtime()


def drink():
    while True:
        print("Hello Happiness Khushi,its Time to drink a glass of water.")
        v.speak("Hello Happiness Khushi,its Time to drink a glass of water.")
        time.sleep(5)


drink()
