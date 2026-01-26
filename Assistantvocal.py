import json
import vosk
import sounddevice as sd

# ... (gardez vos fonctions speak et ask_ollama d'avant) ...

WAKE_WORD = "jarvis"


def listen_for_wake_word():
    # Configuration du micro
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print(f"En attente du mot d'éveil : '{WAKE_WORD}'...")
        while True:
            data, overflowed = stream.read(8000)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")

                if WAKE_WORD in text:
                    print("Mot d'éveil détecté !")
                    speak("Oui, je vous écoute ?")
                    return True  # On sort de la veille


# Boucle Infinie de l'Assistant
while True:
    if listen_for_wake_word():
        # Une fois réveillé, on écoute la vraie commande
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
            data, _ = stream.read(16000)  # On capture la phrase suivante
            if rec.AcceptWaveform(data):
                command = json.loads(rec.Result()).get("text", "")
                if command:
                    print(f"Commande : {command}")
                    reponse = ask_ollama(command)
                    speak(reponse)