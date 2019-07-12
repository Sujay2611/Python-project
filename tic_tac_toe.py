import random

#player makes a turn
def player(a):
    okay = False
    while okay == False:
        okay = True
        play = input("\nPlayer " + str(a) + " make your move (row,column): ").replace(".",",")
        play = play.split(",")          
        row = int(play[0]) - 1
        col = int(play[1]) - 1
        if 0 <= row <= 2 and 0 <= col <= 2 and game[row][col] == " ":
            if a == 1:
                game[row][col] = "X"
            elif a ==2:
                game[row][col] = "O"
        else:
            print("Sorry, you can't play this move.")
            okay = False
 
# computer checks if there is a decisive move that (a) is a direct win for the computer or (b) prevents a player from winning next turn           
def win_next_turn(piece, make_piece):
    global win
    col_check = []
    diag_check1 = [game[0][0], game[1][1], game[2][2]]
    diag_check2 = [game[0][2], game[1][1], game[2][0]]
    for i in range(0,3):    
        for j in range(0,3):
            col_check.append(game[j][i])
        if col_check.count(" ") == 1 and col_check.count(piece) == 2 and win != True:
            col_check = [make_piece if x==" " else x for x in col_check]
            game[0][i] = col_check[0]
            game[1][i] = col_check[1]
            game[2][i] = col_check[2]
            win = True
        elif game[i].count(" ") == 1 and game[i].count(piece) == 2 and win != True:
            game[i]=[make_piece if x==" " else x for x in game[i]]
            win = True
        col_check=[]
    if diag_check1.count(" ") == 1 and diag_check1.count(piece) == 2 and win != True:
        diag_check1 = [make_piece if x == " " else x for x in diag_check1]
        game[0][0] = diag_check1[0]
        game[1][1] = diag_check1[1]
        game[2][2] = diag_check1[2]
        win = True
    elif diag_check2.count(" ") == 1 and diag_check2.count(piece) == 2 and win != True:
        diag_check2 = [make_piece if x == " " else x for x in diag_check2]
        game[0][2] = diag_check2[0]
        game[1][1] = diag_check2[1]
        game[2][0] = diag_check2[2]
        win = True

#computer makes a rational move and reacts to player
def rational_comp2():
    global rand
    global turn
    if turn == 1 and game[1][1] == "X":
        i = random.choice([0,2])
        j = random.choice([0,2])
        game[i][j] = "O"
        rand = True
    elif turn == 1 and (game[1][0] == "X" or game[0][1] == "X" or game[2][1] == "X" or game[1][2] == "X"):
        game[1][1] = "O"
    elif turn == 2 and (game[1][0] == "X" or game[0][1] == "X" or game[2][1] == "X" or game[1][2] == "X") and game[1][1] == "O":
        if game[0][1] == game[2][0] == "X":
            var = random.choice([[0,0],[0,2],[1,2]])
            game[var[0]][var[1]] = "O"
        elif game[0][1] == game[2][2] == "X":
            var = random.choice([[0,0],[0,2],[1,0]])
            game[var[0]][var[1]] = "O" 
        elif game[1][0] == game[0][2] == "X":
            var = random.choice([[0,0],[2,0],[2,1]])
            game[var[0]][var[1]] = "O"
        elif game[1][0] == game[2][2] == "X":     
            var = random.choice([[0,0],[0,1],[2,0]])
            game[var[0]][var[1]] = "O"
        elif game[1][2] == game[0][0] == "X":
            var = random.choice([[0,2],[2,1],[2,2]])
            game[var[0]][var[1]] = "O"
        elif game[1][2] == game[2][0] == "X":     
            var = random.choice([[0,1],[0,2],[2,2]])
            game[var[0]][var[1]] = "O"
        elif game[2][1] == game[0][0] == "X":
            var = random.choice([[1,2],[2,0],[2,2]])
            game[var[0]][var[1]] = "O"
        elif game[2][1] == game[0][2] == "X":     
            var = random.choice([[1,0],[2,0],[2,2]])
            game[var[0]][var[1]] = "O"
        elif game[0][1] == game[1][0] == "X":
            var = random.choice([[0,0],[0,2],[2,0]])
            game[var[0]][var[1]] = "O"
        elif game[0][1] == game[1][2] == "X":
            var = random.choice([[0,0],[0,2],[2,2]])
            game[var[0]][var[1]] = "O"
        elif game[2][1] == game[1][0] == "X":
            var = random.choice([[0,0],[2,0],[2,2]])
            game[var[0]][var[1]] = "O"
        elif game[2][1] == game[1][2] == "X":
            var = random.choice([[0,2],[2,0],[2,2]])
            game[var[0]][var[1]] = "O"
        elif (game[0][1] == game[2][1] == "X") or (game[1][0] == game[1][2] == "X"):
            var = random.choice([[0,0],[0,2],[2,0],[2,2]])
            game[var[0]][var[1]] = "O"
        else:
            stupid_comp(2)
        rand = True
    elif turn == 1 and (game[0][0] == "X" or game[0][2] == "X" or game[2][0] == "X" or game[2][2] == "X"):
        game[1][1] = "O"
    elif turn == 2 and (game[0][0] == "X" or game[2][0] == "X" or game[0][2] == "X" or game[2][2] == "X") and game[1][1] == "O":
        if game[0][0] == game[2][2] == "X" or game[2][0] == game [0][2] == "X":
            var = random.choice([[0,1],[1,0],[1,2],[2,1]])
            game[var[0]][var[1]] = "O"
        rand = True
    else:
        stupid_comp(2)
        rand = True
        
    
#computer takes a random turn   
def stupid_comp(a):
    print("\nThe computer playes:")
    zeroes = 0
    rowcol = []
    for i in range(0,3):
        for j in range(0,3):
            if game[i][j] == " ":
                zeroes += 1
                rowcol.append([i,j])
    place_piece = random.randint(0,zeroes-1)
    rowcol = rowcol[place_piece]
    if a == 1:
        game[rowcol[0]][rowcol[1]] = "X"
    elif a == 2:
        game[rowcol[0]][rowcol[1]]  = "O"


#draws game board including pieces  
def draw(x):
    print("\n       1   2   3")
    for i in range (0,3):
        print("     "+ " ---"*3)
        print("    " + str(i+1) + "| " + str(x[i][0]) + " | " + str(x[i][1]) + " | " + str(x[i][2]) + " |")
    print("     " + " ---"*3 + "\n")

#checks if a player / the computer has won or the game ended in a draw   
def check_win(a):
    winner = False

    for i in range(0,3):
        if a[0][i] == a[1][i] == a[2][i] != " ":
            print("Player " + str(a[0][i]) + " wins!")
            winner = True
        elif a[i][0] == a[i][1] == a[i][2] != " ":
            print("Player " + str(a[i][0]) + " wins!")
            winner = True
    if winner == False:
        if a[0][0] == a[1][1] == a[2][2] != " ":
            print("Player " + str(a[1][1]) + " wins!")
            winner = True
        elif a[0][2] == a[1][1] == a[2][0] != " ":
            print("Player " + str(a[1][1]) + " wins!")
            winner = True
    if winner == False:
        if (not " " in a[0]) and (not " " in a[1]) and (not " " in a[2]):
            print("There is no winner")
    return winner

#draw empty game board   
game = [[" "," "," "], [" "," "," "], [" "," "," "]]
draw(game)

#main
mode = input("Do you want to play against another player or the computer?\nEnter 'player' or 'computer': ")
if mode == "player" or mode == "p":
    
    i = 0
    winner = False

    while (" " in game[0] or " " in game[1] or " " in game[2]) and winner == False:
        if i == 0:
            player(1)
            i += 1
        elif i == 1:
            player(2)
            i -= 1
        draw(game)
        winner = check_win(game)

elif mode == "computer" or mode == "c":
    mode2 = input("Do you want to play on the level of easy, medium or hard?\nEnter level:")
    
    if mode2 == "easy":
        i = 0
        winner = False

        while (" " in game[0] or " " in game[1] or " " in game[2]) and winner == False:
            if i == 0:
                player(1)
                i += 1
            elif i == 1:
                stupid_comp(2)
                i -= 1
            draw(game)
            winner = check_win(game)
            
    elif mode2 == "medium":
        i = 0
        winner = False

        while (" " in game[0] or " " in game[1] or " " in game[2]) and winner == False:
            win = False
            if i == 0:
                player(1)
                i += 1
            elif i == 1:
                win_next_turn("O","O")
                if win == False:
                    win_next_turn("X","O")
                if win == False:
                    stupid_comp(2)
                i -= 1
            draw(game)
            winner = check_win(game)

    elif mode2 == "hard":
        turn = 0
        i = 0
        winner = False
        while (" " in game[0] or " " in game[1] or " " in game[2]) and winner == False:
            win = False
            rand = False
            if i == 0:
                player(1)
                i += 1
                turn += 1
            elif i == 1:
                win_next_turn("O","O")
                if win == False:
                    win_next_turn("X","O")
                if win == False:
                    if rand == False:
                        rational_comp2()
                    else:
                        stupid_comp(2)
                i -= 1
            draw(game)
            winner = check_win(game)
    else:
        print("invalid input")
else:
    print("invalid input")
    
        

   
