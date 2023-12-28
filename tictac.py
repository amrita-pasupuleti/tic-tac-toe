from board import Board
from player import Player, AI, MiniMax

# main program
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    #choosing players
    playerName = input("Input your name here: ")
    player1 = Player(playerName, "X")
    print("Who would you like to play against?")
    enemy = (input("Type [player 2] or [AI]: ")).lower()
    if enemy == "ai":
        diff = (input("Choose your difficulty level (easy or hard): ")).lower()
        if diff=="easy":
             player2 = AI("Easy AI", "O", board)
        else:
             player2 = MiniMax("Hard AI", "O", board)
    else:
        playerTwo = input("Input name of player 2 here: ")
        player2 = Player(playerTwo, "O")

    turn = True
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")
    else:
        print("It is a tie!")
    ans = input("Would you like to play again? [Y/N]\n").upper()
    if (ans != "Y"):
        break
print("Goodbye!")