import socket

def main():
    # Crea un socket per il client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connette il client al server
    client.connect(('127.0.0.1', 5000))

    # Invia il nome utente al server per l'autenticazione
    nome_utente = input("Inserisci il tuo nome utente: ")
    client.send(nome_utente.encode('utf-8'))

    # Riceve la risposta dal server
    risposta = client.recv(1024).decode('utf-8')
    if risposta == "Non autenticato":
        print("Non autenticato")
        client.close()
        return None
    else:
        ciclo = True
        while ciclo:
            # Legge il messaggio da inviare al server
            messaggio = input("Inserisci il messaggio da inviare: ")
            # Invia il messaggio al server
            client.send(messaggio.encode('utf-8'))
            if messaggio == "QUIT":
                ciclo = False
            else:
                # Riceve la risposta dal server
                risposta = client.recv(1024).decode('utf-8')
                print(f"Risposta del server: {risposta}")

        client.close()

if __name__ == "__main__":
    main()