import pyttsx3

# opening file
book = open(r"book.txt")

# reading all lines of the file
book_text = book.readlines()

# inicialaizing the engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)  # Velocidad de habla (palabras por minuto)
engine.setProperty("volume", 0.9)  # volumen (de 0 a 1)

voices = engine.getProperty("voices")  # obteniendo la lista de voces ( son solo 2)
# engine.setProperty("voice", voices[0].id)
engine.setProperty("voice", voices[1].id)

for line in book_text:
    engine.say(line)  # to read the line out loud
    engine.runAndWait()  # para que se mantenga ejecutandosae hasta el final del archivo
    engine.stop()

"""engine.save_to_file(book_text, "test_female_voice.mp3")
engine.runAndWait()"""
