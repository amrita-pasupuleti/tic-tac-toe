from board import Board
from random import choice

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign 
      def get_name(self):
            # return an instance name
            return self.name
      def choose(self,board):
            check = True
            while check:
                  print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
                  cell = input()
                  cell = cell.upper()
      
                  if "A1" not in cell and "A2" not in cell and "A3" not in cell and "B1" not in cell and "B2" not in cell and "B3" not in cell and "C1" not in cell and "C2" not in cell and "C3" not in cell:
                        print("You did not choose correctly.")
                  elif board.isempty(cell):
                        check = False
                  else:
                        print("You did not choose correctly.")
                        

            board.set(cell,self.sign)

#random choice AI
class AI(Player):
      def __init__ (self,name, sign, board = None):
            self.name = name
            self.sign = sign
            self.moves = self.moves(board)

      def moves(self, board=None):
            if board != None:
                  n = board.get_size()
            else:
                  n = 3
            cells = []
            for char in range(65, 65+n):
                  for i in range(1, 1+n):
                        cells.append(chr(char)+str(i))
            return cells
            
      def choose(self, board = None):
            print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            while True:
                  cell = choice(self.moves)
                  self.moves.remove(cell)
                  if board.isempty(cell):
                        break
            print(cell)
            board.set(cell,self.sign)
#minimax     
class MiniMax(AI):
      def __init__ (self, name, sign, board = None):
            self.name = name
            self.sign = sign
            self.board = board
      
      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            

            bestscore = -100
            bestmove = 0

            #get best move based on best score
            for i in range(9):
                  if board.isempty(i):
                        board.set(i, self.sign)
                        score = self.minimax(board, False, 0)
                        board.set(i, " ")
                        if score > bestscore:
                              bestscore = score
                              bestmove = i
            cell = board.squares[bestmove]
            print(cell)
            board.set(bestmove, self.sign)


      
      def minimax(self, board, self_player, start):
            #check the base conditions
            if board.isdone():
                  #win
                  if board.get_winner() == self.sign:
                        return 1
                  #tie
                  elif board.get_winner() == "":
                        return 0
                  #lose
                  else:
                        return -1

            sign1 = self.sign
            if sign1 == "X":
                  sign2 = "O"
            else:
                  sign2 = "X"

            # get bets score
            if self_player:
                  maxscore = -100
                  for i in range(9):
                        if board.isempty(i):
                              board.set(i,sign1)
                              score = self.minimax(board, False, start+1)
                              board.set(i, " ")
                              if score > maxscore:
                                    maxscore = score
                  return maxscore
            
            else:
                  minscore = 100
                  for i in range(9):
                        if board.isempty(i):
                              board.set(i, sign2)
                              score = self.minimax(board, True, start+1)
                              board.set(i, " ")
                              if score < minscore:
                                    minscore = score
                  return minscore
                  

     
                  

