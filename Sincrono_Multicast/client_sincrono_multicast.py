import socket

def main():
    # Crea un socket per il client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connette il client al server
    client.connect(('127.0.0.1', 5000))
    ciclo=True

    while ciclo:
        # Legge il messaggio da inviare al server
        messaggio = input("Inserisci il messaggio da inviare: ")
        # Invia il messaggio al server
        client.send(messaggio.encode('utf-8'))
        if messaggio=="QUIT":
            ciclo=False
        else:    
            # Riceve la risposta dal server
            risposta = client.recv(1024).decode('utf-8')
            print(f"Risposta del server: {risposta}")

if __name__ == "__main__":
    main()