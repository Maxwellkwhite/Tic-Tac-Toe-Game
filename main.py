board = [[" "," "," "], 
         [" "," "," "], 
         [" "," "," "]]

def game_board():
    print(f"\n    1    2    3\n1 {board[0]}\n2 {board[1]}\n3 {board[2]}\n")

def player(letter):
    place_row = int(input(f"Where would you like to place your {letter}? Row: "))
    place_column = int(input(f"Where would you like to place your {letter}? Column: "))
    if board[place_row -1][place_column - 1] == " ":
        board[place_row -1][place_column - 1] = letter
    else:
        print(f"\nNope can't do that")
        player(letter)

def Extract0(x):
        return [item[0] for item in x]

def Extract1(x):
        return [item[1] for item in x]

def Extract2(x):
        return [item[2] for item in x]

def winner(letter):
    Extract0(board)
    if all(x == letter for x in board[0]) or all(x == letter for x in board[1]) or all(x == letter for x in board[2]):
        return True
    elif all (x==letter for x in Extract0(board)):
        return True
    elif all (x==letter for x in Extract1(board)):
        return True
    elif all (x==letter for x in Extract2(board)):
        return True
    elif board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        return True
    elif board[2][0] == letter and board[1][1] == letter and board[0][2] == letter:
         return True
    else:
        pass

game_board()
end_of_game = False
while not end_of_game:
    # X player plays
    player("X")
    game_board()
    winner("X")
    if winner("X") == True:
        end_of_game = True
        print ("X wins!")
    else:
    # Y player plays
        if " " not in board[0] and " " not in board[1] and " " not in board[2]:
            end_of_game = True
            print("No winners")
        else:
            player("O")
            game_board()
            winner("O")
            if winner("O") == True:
                end_of_game = True
                print("O wins!")