import socket
import threading

def gestisci_client(socket_client, indirizzo, utenti):
    # Riceve il primo messaggio dal client
    utente = socket_client.recv(1024).decode('utf-8')
    if utente not in utenti:
        print(f"{indirizzo}: Non autenticato")
        socket_client.send("Non autenticato".encode('utf-8'))
        socket_client.close()
        return None # Termina l'esecuzione della funzione e ritorna None
    else:
        socket_client.send("Autenticato".encode('utf-8'))  # Invia conferma di autenticazione
        ciclo = True
        while ciclo:
            try:
                # Riceve il messaggio dal client
                messaggio = socket_client.recv(1024).decode('utf-8')
                if messaggio == "QUIT":
                    ciclo = False
                print(f"Ricevuto {utente}: {messaggio}")
                # Invia una conferma al client
                socket_client.send("Messaggio ricevuto".encode('utf-8'))
            except:
                ciclo = False
        socket_client.close()

def main():
    # Crea una lista dei utenti disponibili
    utenti = ["Mario", "PierMariaLuigi", "Franco", "Giampino"]
    # Crea un socket per il server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associa il socket all'indirizzo e alla porta
    server.bind(('0.0.0.0', 5000))
    # Il server inizia ad ascoltare le connessioni in arrivo
    server.listen(2)
    print("Server in ascolto sulla porta 5000")

    ciclo = True
    while ciclo:
        # Accetta una nuova connessione
        socket_client, indirizzo = server.accept()
        print(f"Connessione accettata da {indirizzo}")
        # Crea un nuovo thread per gestire il client
        gestore_client = threading.Thread(target=gestisci_client, args=(socket_client, indirizzo, utenti))
        gestore_client.start()

if __name__ == "__main__":
    main()