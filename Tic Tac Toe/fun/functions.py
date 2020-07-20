# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:44:32 2020

@author: Muesgen

functions for playing Tic Tac Toe
"""
from IPython.display import clear_output
def playground (field):
    
    clear_output()
    print("|",field[0],"|",field[1],"|",field[2],"|")
    print("-------")
    print("|",field[3],"|",field[4],"|",field[5],"|")
    print("-------")
    print("|",field[6],"|",field[7],"|",field[8],"|")

def choosing_x_o():
    
    marker = None 
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: do you want to be x or o?").upper()
    
    if marker == "X":
        print("Player 1 is X")
        print("Player 2 is O")
        return ["X","O","X","O","X","O","X","O","X"]
    else:
        print("Player 1 is O")
        print("Player 2 is X")
        return ["O","X","O","X","O","X","O","X","O"]
    
def placing(select, player,i,field):
    
    place = 99
    while not (place >= 0 and place <= 8 and field[place] != "X" and field[place] != "O"):
        if i % 2 == 1:
            place = int(input("Player 1: Which field do you choose?").upper())
        else:
            place = int(input("Player 2: Which field do you choose?").upper())
            
        if place >= 0 and place <= 8 and field[place] != "X" and field[place] != "O":
            field[place] = select[i-1]
            return print("Player", player, "placed his marker on Field: ", place)
        else:
            print("Player",player,"Your placement is incorrect, please choose an other field")
            
def win_control(select, field, player, i):
    
    if field[0] == select[i-1] and field[1] == select[i-1] and field[2] == select[i-1]: #top row
        print("Congratulations Player",player, "you WON!")
        return True
    elif field[3] == select[i-1] and field[4] == select[i-1] and field[5] == select[i-1]: #mid row
        print("Congratulations Player",player, "you WON!")
        return True
    elif field[6] == select[i-1] and field[7] == select[i-1] and field[8] == select[i-1]: #bottom row
        print("Congratulations Player",player, "you WON!")
        return True
    elif field[0] == select[i-1] and field[3] == select[i-1] and field[6] == select[i-1]: #left row
        print("Congratulations Player",player, "you WON!")
        return True
    elif field[1] == select[i-1] and field[4] == select[i-1] and field[7] == select[i-1]: #mid row
        print("Congratulations Player",player, "you WON!")
        return True
    elif field[2] == select[i-1] and field[5] == select[i-1] and field[8] == select[i-1]: #right row
        print("Congratulations Player",player, "you WON!")
        return True
    elif field[0] == select[i-1] and field[4] == select[i-1] and field[8] == select[i-1]: #cross row left up to down right
        print("Congratulations Player",player, "you WON!")
        return True
    elif field[6] == select[i-1] and field[4] == select[i-1] and field[2] == select[i-1]: #cross row left bottom to up right
        print("Congratulations Player",player, "you WON!")
        return True
    else:
        return False
    
def draw_control(field,win):
    
   gesvalue = field.count("O") + field.count("X")
   if win == True:
       pass
   elif gesvalue == 9 and win == False:
        print("It's a DRAW")
        return True
   else:
        pass
        
def new_game(win,draw):
    
    a = 99
    if win == True or draw == True:
        while not (a == 1 or a == 0):
            a = int(input("Do you want to play a new game? Press 1 for Yes and 0 for No").upper())
            if a == 1:
                return True
            elif a == 0:
                return False
    else:
        pass
        

def TicTacToe():
    start = True       
    while start == True:
        print("WELCOME TO TIC TAC TOE")
        field = [0,1,2,3,4,5,6,7,8]
        select = choosing_x_o()
        for i in range(1,(len(field)+1)):
            if i % 2 == 1:
                player = 1
            else:
                player = 2
            
            playground(field)
            placing(select,player,i,field)
            if i == 9:
                clear_output()
                print("|",field[0],"|",field[1],"|",field[2],"|")
                print("-------")
                print("|",field[3],"|",field[4],"|",field[5],"|")
                print("-------")
                print("|",field[6],"|",field[7],"|",field[8],"|")
            win = win_control(select,field,player,i)
            draw = draw_control(field,win)
            if win == True or draw == True:
                break
        start = new_game(win,draw)
        if start == False:
            print("Goodbye")
            break
