import win32com.client as win32

speaker = win32.Dispatch("SAPI.SpVoice")

while True:
    s = input("entre what you want me to speak: ")
    speaker.Speak(s)
    if (s)=="q":
        break