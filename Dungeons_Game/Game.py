# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:52:05 2016

@author: kunalmalik
"""

import random
import os


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
         

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 
        


def get_locations():
    return random.sample(CELLS,3)
    
    
def get_moves(player):
    moves = ["LEFT","RIGHT","UP","DOWN"]
    x,y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y ==0:
        moves.remove("UP")
    if y==4:
        moves.remove("DOWN")
    return moves    
    
def move_player(player, move):
    x,y = player 
    # get the player's location
    if move == "RIGHT":
        x = x + 1
    if move == "LEFT":  
        x = x - 1
    if move == "DOWN":  
        y = y+1
    if move == "UP":    
        y = y - 1
        
    player = x,y
    return player
    
    


def drawmap(player):
    print(' _'*5)
    tile = "|{}"
    for cell in CELLS:
        x,y = cell
        if x < 4:
            line = ""
            if cell == player:
                out = tile.format("X")
            else:
                out = tile.format("_")
        else:
            line = "\n"
            if cell == player:
                out = tile.format("X|")
            else:
                out = tile.format("_|")
        print(out, end = line )            



def gameLoop():
 
    monster, door , player = get_locations()

    while True:
        drawmap(player)
        
        valid_moves = get_moves(player)
        print('Player current location {}'.format(player))
        print('Current Available Moves {}'.format(",".join(valid_moves)))
        move = input("> ").upper()
        
        if move == 'QUIT':
            break
        
        if move in valid_moves:
            player = move_player(player,move)
        else:
            print("Invalid Move or wall bumpp")
            continue
            
        if player == door:
            print("WIN")
        if player == monster:
            print("Monster ate you")
            
            
gameLoop()         
    
