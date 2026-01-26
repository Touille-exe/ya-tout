import socket
import threading

# L'adresse IP du serveur de chat.
# Si le serveur tourne sur la même machine que le client, utilisez '127.0.0.1' (localhost).
# Sinon, remplacez par l'adresse IP de la machine où tourne votre serveur.
HOST = '88.189.46.5'
# Le port sur lequel le serveur écoute. Doit être le même que celui du serveur.
PORT = 49001

# Demande le nom d'utilisateur au démarrage du client.
username = input("Choisissez votre nom d'utilisateur pour le chat : ")

# --- Fonctions du client ---

def receive_messages(client_socket):
    """
    Reçoit et affiche les messages du serveur.

    Args:
        client_socket (socket.socket): Le socket de la connexion au serveur.
    """
    while True:
        try:
            # Reçoit le message du serveur et le décode.
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                # Si le serveur demande le nom d'utilisateur, l'envoie.
                client_socket.send(username.encode('utf-8'))
            else:
                # Affiche le message reçu dans le terminal.
                print(message)
        except:
            # Si une erreur survient (par exemple, le serveur se ferme),
            # affiche un message d'erreur et ferme le client.
            print("Une erreur est survenue, vous avez été déconnecté du serveur.")
            client_socket.close()
            break # Sort de la boucle de réception

def write_messages(client_socket):
    """
    Lit l'entrée de l'utilisateur et envoie les messages au serveur.

    Args:
        client_socket (socket.socket): Le socket de la connexion au serveur.
    """
    while True:
        # Lit le message tapé par l'utilisateur.
        user_input = input('')
        # Formate le message avec le nom d'utilisateur.
        message = f"[{username}]: {user_input}"
        # Envoie le message encodé au serveur.
        client_socket.send(message.encode('utf-8'))

# --- Exécution du client ---
if __name__ == "__main__":
    # Crée un objet socket pour le client.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Tente de se connecter au serveur à l'adresse et au port spécifiés.
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        # Gère le cas où le serveur n'est pas lancé ou n'est pas accessible.
        print(f"Impossible de se connecter au serveur sur {HOST}:{PORT}.")
        print("Veuillez vous assurer que le serveur est lancé et accessible.")
        exit() # Quitte le programme client si la connexion échoue.

    print("Connecté au serveur de chat ! Tapez votre message et appuyez sur Entrée pour envoyer.")

    # Démarre un thread séparé pour recevoir les messages du serveur.
    # Cela permet au client d'envoyer des messages tout en en recevant simultanément.
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Démarre un thread séparé pour envoyer les messages au serveur.
    write_thread = threading.Thread(target=write_messages, args=(client_socket,))
    write_thread.start()
