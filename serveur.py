import socket
import threading

# L'adresse IP sur laquelle le serveur va écouter.
# '0.0.0.0' signifie que le serveur acceptera les connexions de toutes les interfaces réseau disponibles (votre Wi-Fi, Ethernet, etc.).
HOST = '0.0.0.0'
# Le port sur lequel le serveur va écouter. Choisissez un port non utilisé par d'autres services.
PORT = 55559

# Liste pour stocker tous les objets socket des clients connectés.
clients = []
# Liste parallèle pour stocker les noms d'utilisateur des clients.
usernames = []

# --- Fonctions du serveur ---

def broadcast(message, _client):
    """
    Diffuse un message donné à tous les clients connectés, sauf l'expéditeur.

    Args:
        message (bytes): Le message à envoyer (doit être encodé en octets).
        _client (socket.socket): Le socket du client qui a envoyé le message,
                                 pour ne pas lui renvoyer le message à lui-même.
    """
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                # Si l'envoi échoue (le client est probablement déconnecté),
                # nous retirons ce client de nos listes.
                remove_client(client)

def handle_client(client_socket):
    """
    Gère la communication avec un client spécifique dans un thread séparé.

    Args:
        client_socket (socket.socket): Le socket de la connexion client.
    """
    while True:
        try:
            # Reçoit le message du client. La taille du buffer est de 1024 octets.
            message = client_socket.recv(1024)
            # Diffuse le message reçu à tous les autres clients.
            broadcast(message, client_socket)
        except:
            # Si une erreur de connexion survient (par exemple, le client se déconnecte),
            # nous retirons ce client.
            remove_client(client_socket)
            break # Sort de la boucle de gestion du client

def remove_client(client_socket):
    """
    Retire un client déconnecté et son nom d'utilisateur des listes.

    Args:
        client_socket (socket.socket): Le socket du client à retirer.
    """
    if client_socket in clients:
        # Trouve l'index du client pour pouvoir retirer aussi son nom d'utilisateur.
        index = clients.index(client_socket)
        username_to_remove = usernames[index]

        # Retire le client et son nom d'utilisateur des listes.
        clients.remove(client_socket)
        usernames.remove(username_to_remove)

        print(f"[{username_to_remove}] a quitté le chat.")
        # Informe tous les autres clients que cet utilisateur a quitté.
        broadcast(f"[{username_to_remove}] a quitté le chat.".encode('utf-8'), client_socket)
        client_socket.close() # Ferme la connexion socket du client.

def start_server():
    """
    Démarre le serveur de chat et attend les connexions des clients.
    """
    print("Démarrage du serveur de chat...")

    # Crée un objet socket.
    # AF_INET indique l'utilisation d'adresses IPv4.
    # SOCK_STREAM indique un socket de type TCP (orienté connexion, fiable).
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permet de réutiliser rapidement le port après la fermeture du serveur,
    # évitant les erreurs "Address already in use".
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Lie le socket à l'adresse IP et au port spécifiés.
    server.bind((HOST, PORT))
    # Met le serveur en mode écoute. Le chiffre (ici 5) indique le nombre maximum
    # de connexions en attente avant que le serveur ne les accepte.
    server.listen(5)

    print(f"Serveur en écoute sur {HOST}:{PORT}")

    while True:
        # Accepte une nouvelle connexion entrante.
        # server.accept() renvoie un nouvel objet socket pour la connexion client
        # et l'adresse (IP, port) du client.
        client_socket, address = server.accept()
        print(f"Nouvelle connexion depuis {str(address)}")

        # Envoie un signal au client pour qu'il envoie son nom d'utilisateur.
        client_socket.send("USERNAME".encode('utf-8'))
        # Reçoit le nom d'utilisateur du client et le décode.
        username = client_socket.recv(1024).decode('utf-8')

        # Ajoute le client et son nom d'utilisateur aux listes globales.
        usernames.append(username)
        clients.append(client_socket)

        print(f"Nom d'utilisateur du nouveau client : {username}")
        # Informe le client qu'il est connecté.
        client_socket.send("Vous êtes connecté au serveur de chat !".encode('utf-8'))
        # Diffuse à tous les autres clients que quelqu'un a rejoint.
        broadcast(f"[{username}] a rejoint le chat.".encode('utf-8'), client_socket)

        # Démarre un nouveau thread pour gérer la communication avec ce client.
        # Cela permet au serveur d'accepter de nouvelles connexions
        # tout en gérant les clients existants.
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

# --- Exécution du serveur ---
if __name__ == "__main__":
    start_server()