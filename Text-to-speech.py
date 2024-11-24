from win32com.client import *

# don't save in python course folder, cuz it's giving error

x = Dispatch("SAPI.SpVoice")

l = ["Anshuman", "Afaaq", "Dhanashree", "Anuj", "Suraj sir"]

for name in l:
    x.speak(f"hii {name}")
