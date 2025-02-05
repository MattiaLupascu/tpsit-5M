import socket

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 5000))
        print("Connessione al server riuscita")

        nome_utente = input("Inserisci il tuo nome utente: ")
        client.send(nome_utente.encode('utf-8'))
        print(f"Inviato nome utente: {nome_utente}")

        risposta = client.recv(1024).decode('utf-8')
        if risposta == "Non autenticato":
            print("Non autenticato")
            client.close()
            return
        elif risposta == "Autenticato":
            print("Autenticato con successo")

        while True:
            messaggio = input("Inserisci il messaggio da inviare (QUIT per uscire, LIST per la lista): ")
            client.send(messaggio.encode('utf-8'))
            if messaggio == "QUIT":
                break
            elif messaggio == "LIST":
                buffer = ""
                while True:
                    parte = client.recv(1024).decode('utf-8')
                    buffer += parte
                    if "Fine lista" in buffer:
                        break
                # Rimuoviamo il delimitatore
                buffer = buffer.replace("Fine lista\n", "")
                print("Server:\n" + buffer)
            else:
                risposta = client.recv(1024).decode('utf-8')
                print(f"Server: {risposta}")
        print("Chiusura connessione")
        client.close()
    except Exception as e:
        print(f"Errore durante la comunicazione con il server: {e}")

if __name__ == "__main__":
    main()