import socket
import threading

def gestisci_client(socket_client, indirizzo, utenti, collegamenti):
    try:
        utente = socket_client.recv(1024).decode('utf-8')
        print(f"Ricevuto tentativo di autenticazione da {indirizzo}: {utente}")
        if utente not in utenti:
            print(f"{indirizzo}: Non autenticato")
            socket_client.send("Non autenticato".encode('utf-8'))
            socket_client.close()
            return
        else:
            socket_client.send("Autenticato".encode('utf-8'))
            print(f"{indirizzo}: Autenticato")
            connessione = 0
            for i in utenti:
                if utente == i:
                    collegamenti[connessione] = 1
                connessione += 1
            print("Stato collegamenti:", collegamenti)
            ciclo = True
            while ciclo:
                try:
                    messaggio = socket_client.recv(1024).decode('utf-8')
                    if messaggio == "QUIT":
                        ciclo = False
                    elif messaggio == "LIST":
                        print(f"Ricevuto comando LIST da {utente}")
                        risposta = ""
                        for i in range(len(utenti)):
                            if collegamenti[i] == 1:
                                risposta += f"{utenti[i]} è connesso\n"
                        risposta += "Fine lista\n"
                        socket_client.sendall(risposta.encode('utf-8'))
                    else:
                        print(f"Ricevuto {utente}: {messaggio}")
                        socket_client.send("Messaggio ricevuto".encode('utf-8'))
                except Exception as e:
                    print(f"Errore durante la ricezione del messaggio: {e}")
                    ciclo = False
            socket_client.close()
    except Exception as e:
        print(f"Errore durante la gestione del client: {e}")

def main():
    utenti = ["Mario", "PierMariaLuigi", "Franco", "Giampino"]
    collegamenti = [0] * len(utenti)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))
    server.listen(2)
    print("Server in ascolto sulla porta 5000")
    
    ciclo_main = True
    while ciclo_main:
        try:
            socket_client, indirizzo = server.accept()
            print(f"Connessione accettata da {indirizzo}")
            threading.Thread(target=gestisci_client, args=(socket_client, indirizzo, utenti, collegamenti)).start()
        except Exception as e:
            print(f"Errore durante l'accettazione della connessione: {e}")
            ciclo_main = False

if __name__ == "__main__":
    main()