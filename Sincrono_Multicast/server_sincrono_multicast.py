import socket
import threading

def gestisci_client(socket_client, indirizzo, utenti, collegamenti):
    # Prova a gestire il client in un blocco try per catturare eccezioni
    try:
        # Ricevi il nome utente inviato dal client e decodificalo
        utente = socket_client.recv(1024).decode('utf-8')
        print(f"Ricevuto tentativo di autenticazione da {indirizzo}: {utente}")
        # Verifica se l'utente è autorizzato (presente nella lista degli utenti)
        if utente not in utenti:
            print(f"{indirizzo}: Non autenticato")
            # Invia messaggio negativo al client e chiudi la connessione
            socket_client.send("Non autenticato".encode('utf-8'))
            socket_client.close()
            return
        else:
            # Se autenticato, invia conferma al client
            socket_client.send("Autenticato".encode('utf-8'))
            print(f"{indirizzo}: Autenticato")
            # Imposta lo stato del collegamento dell'utente
            connessione = 0
            for i in utenti:
                if utente == i:
                    collegamenti[connessione] = 1  # L'utente risulta ora connesso
                connessione += 1
            print("Stato collegamenti:", collegamenti)
            
            # Ciclo principale di comunicazione con il client
            ciclo = True
            while ciclo:
                try:
                    # Ricevi un messaggio dal client
                    messaggio = socket_client.recv(1024).decode('utf-8')
                    # Gestione dei comandi speciali
                    if messaggio == "QUIT":
                        # Esci dal ciclo se il client invia "QUIT"
                        ciclo = False
                    elif messaggio == "LIST":
                        print(f"Ricevuto comando LIST da {utente}")
                        risposta = ""
                        # Costruisci la lista degli utenti connessi
                        for i in range(len(utenti)):
                            if collegamenti[i] == 1:
                                risposta += f"{utenti[i]} è connesso\n"
                        # Aggiungi il delimitatore alla fine della lista
                        risposta += "Fine lista\n"
                        # Invia l'intera risposta in un unico pacchetto
                        socket_client.sendall(risposta.encode('utf-8'))
                    else:
                        # Gestione dei messaggi generici: stampa e invia conferma
                        print(f"Ricevuto {utente}: {messaggio}")
                        socket_client.send("Messaggio ricevuto".encode('utf-8'))
                except Exception as e:
                    # In caso di errore durante la ricezione, esci dal ciclo
                    print(f"Errore durante la ricezione del messaggio: {e}")
                    ciclo = False
            # Chiudi il socket del client
            socket_client.close()
    except Exception as e:
        # Gestione generale degli errori nella comunicazione con il client
        print(f"Errore durante la gestione del client: {e}")

def main():
    # Definizione della lista degli utenti autorizzati
    utenti = ["Mario", "PierMariaLuigi", "Franco", "Giampino"]
    # Inizializzazione dello stato di connessione per ogni utente (0 = disconnesso)
    collegamenti = [0] * len(utenti)
    # Creazione del socket del server (IPv4, TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))  # Associa il server alla porta 5000 su tutti gli indirizzi
    server.listen(2)  # Imposta il limite alle connessioni in coda
    print("Server in ascolto sulla porta 5000")
    
    # Ciclo principale per accettare connessioni in arrivo
    ciclo_main = True
    while ciclo_main:
        try:
            # Accetta la connessione di un nuovo client
            socket_client, indirizzo = server.accept()
            print(f"Connessione accettata da {indirizzo}")
            # Avvia un nuovo thread per gestire il client
            threading.Thread(target=gestisci_client, args=(socket_client, indirizzo, utenti, collegamenti)).start()
        except Exception as e:
            # In caso di errore durante l'accettazione, esce dal ciclo
            print(f"Errore durante l'accettazione della connessione: {e}")
            ciclo_main = False

if __name__ == "__main__":
    main()