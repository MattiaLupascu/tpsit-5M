import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5000))

    # Invia il nome utente per l'autenticazione
    client.send("Mario".encode('utf-8'))

    # Riceve la risposta di autenticazione
    response = client.recv(1024).decode('utf-8')
    print(f"Server: {response}")

    if response == "Autenticato":
        while True:
            # Invia un comando al server
            command = input("Inserisci un comando (LIST, QUIT, o un messaggio): ")
            client.send(command.encode('utf-8'))

            if command == "QUIT":
                break
            elif command == "LIST":
                while True:
                    response = client.recv(1024).decode('utf-8')
                    print(f"Server: {response}")
                    if response == "Fine lista":
                        break
            else:
                response = client.recv(1024).decode('utf-8')
                print(f"Server: {response}")

    client.close()

if __name__ == "__main__":
    main()