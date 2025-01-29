import socket
import threading

def gestisci_client(socket_client, indirizzo, utenti, collegamenti):
    try:
        # Riceve il primo messaggio dal client
        utente = socket_client.recv(1024).decode('utf-8')
        print(f"Ricevuto tentativo di autenticazione da {indirizzo}: {utente}")
        if utente not in utenti:
            print(f"{indirizzo}: Non autenticato")
            socket_client.send("Non autenticato".encode('utf-8'))
            socket_client.close()
            return None  # Termina l'esecuzione della funzione e ritorna None
        else:
            socket_client.send("Autenticato".encode('utf-8'))  # Invia conferma di autenticazione
            print(f"{indirizzo}: Autenticato")
            connessione = 0
            for i in utenti:
                if utente == i:
                    collegamenti[connessione] = 1
                connessione += 1

            ciclo = True
            while ciclo:
                try:
                    # Riceve il messaggio dal client
                    messaggio = socket_client.recv(1024).decode('utf-8')
                    if messaggio == "QUIT":
                        ciclo = False
                    elif messaggio == "LIST":
                        for i in range(len(utenti)):
                            if collegamenti[i] == 1:
                                socket_client.send(f"{utenti[i]} è connesso".encode('utf-8'))
                    print(f"Ricevuto {utente}: {messaggio}")
                    # Invia una conferma al client
                    socket_client.send("Messaggio ricevuto".encode('utf-8'))
                except:
                    print(f"Errore durante la ricezione del messaggio")
                    ciclo = False
            socket_client.close()
    except:
        print(f"Errore durante la gestione del client")

def main():
    # Crea una lista dei utenti disponibili
    utenti = ["Mario", "PierMariaLuigi", "Franco", "Giampino"]
    collegamenti = [0, 0, 0, 0]
    # Crea un socket per il server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associa il socket all'indirizzo e alla porta
    server.bind(('0.0.0.0', 5000))
    # Il server inizia ad ascoltare le connessioni in arrivo
    server.listen(2)
    print("Server in ascolto sulla porta 5000")

    ciclo = True
    while ciclo:
        try:
            # Accetta una nuova connessione
            socket_client, indirizzo = server.accept()
            print(f"Connessione accettata da {indirizzo}")
            # Crea un nuovo thread per gestire il client
            threading.Thread(target=gestisci_client, args=(socket_client, indirizzo, utenti, collegamenti)).start()
        except:
            print("Errore durante l'accettazione della connessione")
            ciclo = False

if __name__ == "__main__":
    main()