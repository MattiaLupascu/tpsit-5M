import socket
import threading

def gestisci_client(socket_client, indirizzo, utenti, collegamenti):
    try:
        utente = socket_client.recv(1024).decode('utf-8')
        if utente not in utenti:
            socket_client.send("Non autenticato".encode('utf-8'))
            socket_client.close()
            return
        else:
            socket_client.send("Autenticato".encode('utf-8'))
            indice = 0
            while indice < len(utenti):
                if utenti[indice] == utente:
                    collegamenti[indice] = 1
                indice += 1

            ciclo = True
            while ciclo:
                try:
                    messaggio = socket_client.recv(1024).decode('utf-8')
                    if messaggio == "QUIT":
                        ciclo = False
                    elif messaggio == "LIST":
                        i = 0
                        while i < len(utenti):
                            if collegamenti[i] == 1:
                                socket_client.send((utenti[i] + " è connesso \n").encode('utf-8'))
                            i += 1
                        socket_client.send("Fine lista".encode('utf-8'))
                    else:
                        socket_client.send("Messaggio ricevuto".encode('utf-8'))
                except:
                    ciclo = False
            socket_client.close()
    except:
        socket_client.close()

def main():
    utenti = ["Mario", "PierMariaLuigi", "Franco", "Giampino"]
    collegamenti = [0, 0, 0, 0]

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))
    server.listen(2)
    print("Server in ascolto sulla porta 5000")

    ciclo = True
    while ciclo:
        try:
            socket_client, indirizzo = server.accept()
            threading.Thread(target=gestisci_client, args=(socket_client, indirizzo, utenti, collegamenti)).start()
        except:
            ciclo = False

if __name__ == "__main__":
    main()