import socket

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 5000))
        print("Connessione al server riuscita")

        nome_utente = input("Inserisci il tuo nome utente: ")
        client.send(nome_utente.encode('utf-8'))

        risposta = client.recv(1024).decode('utf-8')
        if risposta == "Non autenticato":
            print("Non autenticato")
            client.close()
            return
        elif risposta == "Autenticato":
            print("Autenticato con successo")

        ciclo = True
        while ciclo:
            messaggio = input("Inserisci il messaggio da inviare: ")
            client.send(messaggio.encode('utf-8'))

            if messaggio == "QUIT":
                ciclo = False
            elif messaggio == "LIST":
                ciclo_lista = True
                while ciclo_lista:
                    try:
                        risposta = client.recv(1024).decode('utf-8')
                        if risposta == "Fine lista":
                            ciclo_lista = False
                        else:
                            print("Risposta del server:", risposta)
                    except:
                        ciclo_lista = False
            else:
                try:
                    risposta = client.recv(1024).decode('utf-8')
                    print("Risposta del server:", risposta)
                except:
                    ciclo = False

        client.close()
    except:
        print("Errore durante la comunicazione con il server")

if __name__ == "__main__":
    main()