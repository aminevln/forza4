import tkinter as tk
import socket

class Forza4Client:
    def __init__(self, master, ip, port):
        self.master = master
        self.master.title("Forza 4")

        # Socket per la comunicazione con il server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

        # Configura la GUI
        self.pulsanti_colonna = []
        self.tabellone = []

        # Crea la griglia di Forza 4
        for riga in range(6):
            row = []
            for colonna in range(7):
                label = tk.Label(master, width=6, height=3, relief="solid", bg="lightblue")
                label.grid(row=riga, column=colonna)
                row.append(label)
            self.tabellone.append(row)

        # Aggiungi i pulsanti per le colonne
        for colonna in range(7):
            button = tk.Button(master, text=f"Colonna {colonna+1}", command=lambda c=colonna: self.mossa(c))
            button.grid(row=6, column=colonna)
            self.pulsanti_colonna.append(button)

        # Ricevi il tabellone iniziale
        self.aggiungi_punti()

    def mossa(self, colonna):
        # Invia la mossa al server
        self.socket.sendall(str(colonna).encode())
        # Aspetta la risposta dal server
        risposta = self.socket.recv(1024).decode()
        print(risposta)
        if risposta == "Hai vinto!":
            print("Hai vinto!")
            self.master.quit()
        else:
            # Aggiorna il tabellone
            self.aggiungi_punti()

    def aggiungi_punti(self):
        # Ottieni il tabellone dal server e aggiornalo
        self.socket.sendall("get_tabellone".encode())
        risposta = self.socket.recv(1024).decode()
        tabellone = eval(risposta)

        for riga in range(6):
            for colonna in range(7):
                if tabellone[riga][colonna] == 'X':
                    self.tabellone[riga][colonna].config(bg="red")
                elif tabellone[riga][colonna] == 'O':
                    self.tabellone[riga][colonna].config(bg="yellow")
                else:
                    self.tabellone[riga][colonna].config(bg="lightblue")


# Crea la finestra Tkinter
root = tk.Tk()
app = Forza4Client(root, '127.0.0.1', 12345)  # Usa l'IP e la porta del server
root.mainloop()
