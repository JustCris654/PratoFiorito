import arcade
from random import seed, randint
from SetupGame import *



class Cell(object):
    # Costruttore della classe Cell
    def __init__(self, is_bomb, column, row):
        # True if the cell is a bomb, false otherwise
        self.is_bomb = is_bomb
        # True if the cell is revealed, false otherwise
        self.revealed = False
        # Number of neighboring bombs
        self.neighboring_bombs = None
        # Unsure
        self.unsure = False
        # True if the cell is marked
        self.marked = False


class Grid(object):
    # Costruttore classe Grid
    def __init__(self, column_count, row_count):
        # Numero di righe del gioco
        self.row_count = row_count
        # Numero di colonne
        self.column_count = column_count
        # Creo la griglia con un doppio for annidato
        self.grid = [[Cell(False, column, row) for row in range(self.row_count)]
                     for column in range(self.column_count)]
                 
    def generate_bombs(self, level):
        # Calcolo il numero di bombe 
        max_bombs = (level) * 5

        # Genero le bombe su posizioni casuali 
        # Potrei integrare direttamente qua il calcolo dei numeri delle bombe vicine per le caselle
        # Aggiungendo gia qua +1 ad ogni casella adiacente alla bomba generata ma lo faro in futuro        
        i = 0
        while i < max_bombs:
            column_bomb = randint(0, self.row_count - 1)            # Randint genera un numero casuale da 0 a numero righe -1
            row_bomb = randint(0, self.column_count - 1)            # Da 0 a numero colonne -1
            if self.grid[column_bomb][row_bomb].is_bomb is False:   # Se è gia una bomba non faccio nulla
                self.grid[column_bomb][row_bomb].is_bomb = True     # Se non è una bomba la aggiungo
                i += 1                                              # E aggiungo uno a iu che conta il numero di bombe 

    # Rivela la cella corrente e ricorsivamente va a cercare le cella vicine rivelandole finche
    # non trova celle con bombe adiacenti
    def reveal_cell(self, column, row):     
        # Rivelo la cella                        
        self.grid[column][row].revealed = True      

        # Se la cella è una bomba esco
        if self.grid[column][row].is_bomb:
            return False

        # Se la cella non ha bombe adiacenti continuo con la ricosione
        if self.grid[column][row].neighboring_bombs == 0:
            
            # Cella a sinistra 
            pos_x = column - 1
            pos_y = row
            if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            # Cella a destra
            pos_x = column + 1
            pos_y = row
            if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            # Cella sotto
            pos_x = column
            pos_y = row - 1
            if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)
            
            # Cella sopra
            pos_x = column
            pos_y = row + 1
            if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            # Cella sopra a sinistra
            pos_x = column - 1
            pos_y = row + 1
            if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            # Cella sotto a sinistra
            pos_x = column - 1
            pos_y = row - 1
            if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            # Cella sotto a destra
            pos_x = column + 1
            pos_y = row - 1
            if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

            # Cella sopra a destra
            pos_x = column + 1
            pos_y = row + 1
            if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                if self.grid[pos_x][pos_y].revealed is False:
                    self.reveal_cell(pos_x, pos_y)

    # Conta i vicini
    def count_neighbours(self, column, row):
        # Se la cella stessa è una bomba restituisco falso
        if self.grid[column][row].is_bomb is True:
            return None

        # Conto le bombe adiacenti alla casella
        total = 0
        for i in range(-1, 2):
            for k in range(-1, 2):
                pos_x = column + i
                pos_y = row + k
                if 0 <= pos_x < self.column_count and 0 <= pos_y < self.row_count:
                    if self.grid[pos_x][pos_y].is_bomb is True:
                        total += 1

        # Assegno il valore di bombe adiacenti al parametro
        self.grid[column][row].neighboring_bombs = total
    
    # Rivela tutte le celle 
    def reveal_all(self):
        for i in self.grid:
            for k in i:
                k.revealed = True
        return True
