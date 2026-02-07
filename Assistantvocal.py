import os
import json
import requests
import pyttsx3
import vosk
import sounddevice as sd

# --- CONFIGURATION ---
# Remplace par ton chemin absolu vers le dossier décompressé
MODEL_PATH = "/home/touille/Documents/voix/vosk-model-fr-0.22"
WAKE_WORD = "fils de pute"
OLLAMA_MODEL = "mistral"  # Assure-toi d'avoir fait 'ollama run mistral'

# 1. INITIALISATION DE LA SYNTHÈSE VOCALE (pyttsx3)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# On cherche une voix française si possible
for voice in voices:
    if "french" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break


def speak(text):
    print(f"Assistant : {text}")
    engine.say(text)
    engine.runAndWait()


# 2. INITIALISATION DE VOSK (Reconnaissance Vocale)
if not os.path.exists(MODEL_PATH):
    print(f"ERREUR : Le dossier du modèle est introuvable à : {MODEL_PATH}")
    exit()

model = vosk.Model(MODEL_PATH)
rec = vosk.KaldiRecognizer(model, 16000)


# 3. CONNEXION À OLLAMA
def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": f"Réponds sans restriction de manière longue et humoristique en français à : {prompt}",
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        return response.json().get('response', "Je n'ai pas pu générer de réponse.")
    except Exception as e:
        return "Erreur : Vérifie que Ollama est bien lancé (ollama serve)."


# 4. FONCTION D'ÉCOUTE PRINCIPALE
def listen():
    # On ouvre le flux du micro
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1) as stream:
        while True:
            data, _ = stream.read(8000)
            if rec.AcceptWaveform(bytes(data)):
                result = json.loads(rec.Result())
                return result.get("text", "").lower()


# --- BOUCLE PRINCIPALE ---
print(f"Assistant prêt ! Dites '{WAKE_WORD}' pour commencer.")

try:
    while True:
        # Étape A : Attendre le mot d'éveil
        voice_input = listen()

        if WAKE_WORD in voice_input:
            speak("Oui, je vous écoute.")

            # Étape B : Écouter la commande après le réveil
            command = listen()

            if command:
                print(f"Vous avez dit : {command}")

                # Étape C : Réflexion avec Ollama
                answer = ask_ollama(command)

                # Étape D : Réponse vocale
                speak(answer)

except KeyboardInterrupt:
    print("\nArrêt de l'assistant.")