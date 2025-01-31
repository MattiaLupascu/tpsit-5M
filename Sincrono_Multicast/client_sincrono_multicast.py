import socket

def main():
    try:
        # Crea un socket per il client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connette il client al server
        client.connect(('127.0.0.1', 5000))
        print("Connessione al server riuscita")

        # Invia il nome utente al server per l'autenticazione
        nome_utente = input("Inserisci il tuo nome utente: ")
        client.send(nome_utente.encode('utf-8'))
        print(f"Inviato nome utente: {nome_utente}")

        # Riceve la risposta dal server
        risposta = client.recv(1024).decode('utf-8')
        if risposta == "Non autenticato":
            print("Non autenticato")
            client.close()
            return
        elif risposta == "Autenticato":
            print("Autenticato con successo")

        ciclo = True
        while ciclo:
            # Legge il messaggio da inviare al server
            messaggio = input("Inserisci il messaggio da inviare: ")
            # Invia il messaggio al server
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
                            print(f"Risposta del server: {risposta}")
                    except Exception as e:
                        print(f"Errore durante ricezione della lista: {e}")
                        ciclo_lista = False
                continue  # Aggiungi questa linea per continuare il ciclo principale
            else:
                try:
                    risposta = client.recv(1024).decode('utf-8')
                    print(f"Risposta del server: {risposta}")
                except Exception as e:
                    print(f"Errore durante ricezione del messaggio: {e}")
                    ciclo = False

        client.close()
    except Exception as e:
        print(f"Errore durante la comunicazione con il server: {e}")

if __name__ == "__main__":
    main()