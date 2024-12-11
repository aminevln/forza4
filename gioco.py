# Funzione per creare un tabellone vuoto
def crea_tabellone():
    return [[' ' for _ in range(7)] for _ in range(6)]

# Funzione per stampare il tabellone nel terminale (per debug)
def stampa_tabellone(tabellone):
    for riga in tabellone:
        print('|'.join(riga))
    print('-' * 15)

# Funzione per verificare se c'è una vittoria
def verifica_vittoria(tabellone, giocatore):
    # Controlla le righe
    for riga in range(6):
        for colonna in range(4):
            if tabellone[riga][colonna] == giocatore and \
               tabellone[riga][colonna + 1] == giocatore and \
               tabellone[riga][colonna + 2] == giocatore and \
               tabellone[riga][colonna + 3] == giocatore:
                return True

    # Controlla le colonne
    for colonna in range(7):
        for riga in range(3):
            if tabellone[riga][colonna] == giocatore and \
               tabellone[riga + 1][colonna] == giocatore and \
               tabellone[riga + 2][colonna] == giocatore and \
               tabellone[riga + 3][colonna] == giocatore:
                return True

    # Controlla la diagonale (dal basso verso l'alto)
    for riga in range(3, 6):
        for colonna in range(4):
            if tabellone[riga][colonna] == giocatore and \
               tabellone[riga - 1][colonna + 1] == giocatore and \
               tabellone[riga - 2][colonna + 2] == giocatore and \
               tabellone[riga - 3][colonna + 3] == giocatore:
                return True

    # Controlla la diagonale (dall'alto verso il basso)
    for riga in range(3):
        for colonna in range(4):
            if tabellone[riga][colonna] == giocatore and \
               tabellone[riga + 1][colonna + 1] == giocatore and \
               tabellone[riga + 2][colonna + 2] == giocatore and \
               tabellone[riga + 3][colonna + 3] == giocatore:
                return True

    return False
