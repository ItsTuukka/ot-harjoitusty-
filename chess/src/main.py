import pygame as p
import sys
import os
from gamestate import GameState
from pieces import Piece
from attack import Attack
clock = p.time.Clock()
fps = 30
GS = GameState()
A = Attack(GS)
Piece = Piece(GS, A)
width = height = 512
square = height // 8
p.init()
screen = p.display.set_mode((width, height))

"""
This is the main function that starts the game and goes through user inputs
"""

def main():
    screen.fill((0,0,0))
    player_clicks = []
    while True:
        for e in p.event.get():
            if e.type == p.QUIT:
                sys.exit()
            if e.type == p.MOUSEBUTTONDOWN:
                position = p.mouse.get_pos()
                pos_sq = (position[0]//square, position[1]//square)
                if GS.boardstate[pos_sq[1]][pos_sq[0]] != "" or len(player_clicks) > 0:
                    if pos_sq in player_clicks:
                        player_clicks = []
                    else:
                        player_clicks.append(pos_sq)
                if len(player_clicks) == 2:
                    Piece.movePiece(player_clicks[0],player_clicks[1])
                    player_clicks = []
        drawBoard()
        A.whiteThreatens()
        A.blackThreatens()
        clock.tick(fps)
        p.display.flip()

def drawBoard():
    colors = [(235, 235, 208), (119, 148, 85)]
    for row in range(8):
        for colum in range(8):
            color = colors[((row+colum) % 2)]
            p.draw.rect(screen, color, p.Rect(colum*square, row*square, square, square))
            piece = GS.boardstate[row][colum]
            if piece != "":
                screen.blit(Piece.images[piece], p.Rect(colum*square, row*square, square, square))





    



main()