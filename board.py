class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
         # by " " strings

        self.sign = " "
        self.winner = ""
        self.size = 3
        self.indexes = {"A1":0, "B1":1, "C1":2, 
                        "A2":3, "B2":4, "C2":5,
                        "A3":6, "B3":7, "C3":8}

        self.squares = {0:"A1", 1:"A2", 2:"A3",
                        3:"B1", 4:"B2", 5:"B3",
                        6:"C1", 7:"C2", 8:"C3"}

        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        
        

    def get_size(self): 
        # optional, return the board size (an instance size)
        return self.size 

    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        return self.winner

    def set(self, cell, sign):
         # mark the cell on the board with the sign X or O
        cell = str(cell)
        if cell.isdigit():
            cell = int(cell)
            self.board[cell] = sign
        else: 
            index = self.indexes[cell]
            self.board[index] = sign
       

    def isempty(self, cell):
        # return True if the cell is empty (not marked with X or O)
        cell = str(cell)
        if cell.isdigit():
            cell = int(cell)
            return self.board[cell] == " "
        else:
            return self.board[self.indexes[cell]] == " "

            

    def isdone(self):
        done = False
        self.winner = ''
        board = self.board
        # check all game terminating conditions, if one of them is present, assign the var done to True
        count = 0
        for i in board:
            if i != " ":
                count += 1
        if count > 4:
            #check rows
            if board[0] == board[1] and board[1] == board[2] and board[0] != " ":
                done = True
                self.winner = board[0]
            elif board[3] == board[4] and board[4] == board[5] and board[3] != " ":
                done = True
                self.winner = board[3]
            elif board[6] == board[7] and board[7] == board[8] and board[6] != " ":
                done = True
                self.winner = board[6]
            #check columns
            elif board[0] == board[3] and board[3] == board[6] and board[0] != " ":
                done = True
                self.winner = board[0]
            elif board[1] == board[4] and board[4] == board[7] and board[1] != " ":
                done = True
                self.winner = board[1]
            elif board[2] == board[5] and board[5] == board[8] and board[2] != " ":
                done = True
                self.winner = board[2]
            #check diagonals
            elif board[0] == board[4] and board[4] == board[8] and board[0] != " ":
                done = True
                self.winner = board[0]
            elif board[2] == board[4] and board[4] == board[6] and board[2] != " ":
                done = True
                self.winner = board[2]
            #check if board is empty
            elif count == 9:
                done = True
        
        return done

    def show(self):
        print("   A   B   C  ")
        print(" +---+---+---+")
        print(f"1| {self.board[0]} | {self.board[1]} | {self.board[2]} |")
        print(" +---+---+---+")
        print(f"2| {self.board[3]} | {self.board[4]} | {self.board[5]} |")
        print(" +---+---+---+")
        print(f"3| {self.board[6]} | {self.board[7]} | {self.board[8]} |")
        print(" +---+---+---+")


