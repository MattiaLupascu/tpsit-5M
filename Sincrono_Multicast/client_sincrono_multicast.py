import socket

def main():
    try:
        # Creazione del socket del client (IPv4, TCP)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connessione al server in esecuzione in localhost sulla porta 5000
        client.connect(('127.0.0.1', 5000))
        print("Connessione al server riuscita")

        # Invia il nome utente per l'autenticazione
        nome_utente = input("Inserisci il tuo nome utente: ")
        client.send(nome_utente.encode('utf-8'))
        print(f"Inviato nome utente: {nome_utente}")

        # Ricevi la risposta del server riguardo l'autenticazione
        risposta = client.recv(1024).decode('utf-8')
        if risposta == "Non autenticato":
            print("Non autenticato")
            client.close()
            return
        elif risposta == "Autenticato":
            print("Autenticato con successo")

        # Ciclo principale per inviare messaggi al server
        ciclo = True
        while ciclo:
            # Richiesta di un comando (QUIT, LIST, o messaggio qualsiasi)
            messaggio = input("Inserisci il messaggio da inviare (QUIT per uscire, LIST per la lista): ")
            client.send(messaggio.encode('utf-8'))
            if messaggio == "QUIT":
                # Se il comando è QUIT, imposta ciclo a False per uscire dal ciclo
                ciclo = False
            elif messaggio == "LIST":
                # Gestione del comando LIST: ricezione della lista degli utenti connessi
                buffer = ""
                ciclo_2 = True
                while ciclo_2:
                    # Riceve in modo iterativo i dati dal server e li accumula nel buffer
                    parte = client.recv(1024).decode('utf-8')
                    buffer += parte
                    # Verifica se nel buffer è presente il delimitatore per la fine della lista
                    if "Fine lista" in buffer:
                        ciclo_2 = False
                # Rimuove il delimitatore "Fine lista\n" dalla risposta
                buffer = buffer.replace("Fine lista\n", "")
                # Stampa la lista degli utenti connessi
                print("Server:\n" + buffer)
            else:
                # Per ogni altro messaggio, riceve la risposta del server e la stampa
                risposta = client.recv(1024).decode('utf-8')
                print(f"Server: {risposta}")
        print("Chiusura connessione")
        client.close()
    except Exception as e:
        # Gestione degli errori durante la comunicazione
        print(f"Errore durante la comunicazione con il server: {e}")

if __name__ == "__main__":
    main()