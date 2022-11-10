import pyttsx3


#initialise the engine
engine = pyttsx3.init()

text = ". How does this voice sound for Jarvis?"
voice_list = engine.getProperty("voices")
engine.setProperty("rate", 150)

for voice_count in range(11, 18):
    engine.setProperty("voice", voice_list[voice_count].id)
    engine.say(str(voice_count) + text)
    engine.runAndWait()
