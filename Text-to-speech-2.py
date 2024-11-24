from win32com.client import *
x = Dispatch("SAPI.SpVoice")

l = ["Harry", "Afaq", "Ronak", "Shruti", "zeba"]

for name in l:
    x.speak(f"hello dear {name}")
