import pygame.midi
import time

# Initialisation de pygame.midi
pygame.midi.init()

# Ouverture du port MIDI pour utiliser un dispositif de sortie (généralement, le premier périphérique disponible)
player = pygame.midi.Output(0)

# Sélectionner l'instrument Ocarina sur le patch MIDI 70 (General MIDI)
# Les instruments MIDI sont désignés par des numéros, le patch 70 est souvent l'ocarina
player.set_instrument(70)

# Liste des fréquences MIDI des notes (Do, Ré, Mi, Fa, Sol, La, Si)
notes_midi = {
    "Do": 60,  # MIDI note 60 = Do
    "Ré": 62,  # MIDI note 62 = Ré
    "Mi": 64,  # MIDI note 64 = Mi
    "Fa": 65,  # MIDI note 65 = Fa
    "Sol": 67,  # MIDI note 67 = Sol
    "La": 69,  # MIDI note 69 = La
    "Si": 71   # MIDI note 71 = Si
}

# Liste des chansons complètes avec les vraies notes de musique
songs = {
    "Zelda's Lullaby": [
        "Fa", "La", "Ré", "Fa", "La", "Ré", "Fa", "La", "Ré", "Fa", "La", "Ré"
    ],
    "Song of Storms": [
        "Ré", "Fa", "Ré", "Fa", "Ré", "Fa", "Ré", "La", "Sol", "Fa", "Sol", "Fa"
    ],
    "Epona's Song": [
        "Fa", "Ré", "Si", "Fa", "Ré", "Si", "Ré", "Si",
    ],
    "Saria's Song": [
        "Ré", "Fa", "Sol", "Ré", "Fa", "Sol", "Ré", "Fa", "Sol"
    ],
    "Sun's Song": [
        "Do", "Fa", "La", "Do", "Fa", "La", "Do", "Fa", "La"
    ],
    "Song of Time": [
        "La", "Ré", "Fa", "La", "Ré", "Fa", "La", "Ré", "Fa", "La"
    ]
}

def play_note(note):
    """Joue une note MIDI."""
    midi_note = notes_midi[note]
    player.note_on(midi_note, 127)  # Joue la note avec une vélocité de 127 (volume maximal)
    time.sleep(0.5)  # Attendre 0.5 seconde avant de couper la note
    player.note_off(midi_note, 127)  # Arrêter la note

def play_song(song_name):
    """Joue une chanson complète en utilisant les notes MIDI."""
    song = songs.get(song_name)
    if not song:
        print("❌ Chanson non trouvée !")
        return

    print(f"🎶 Lecture de : {song_name}")
    for note in song:
        play_note(note)

# Menu de sélection des chansons
while True:
    print("\n🎵 Choisis une chanson :")
    for name in songs.keys():
        print(f"- {name}")

    choice = input("> ").strip()
    play_song(choice)

# Fermeture du port MIDI une fois terminé
player.close()
pygame.midi.quit()
