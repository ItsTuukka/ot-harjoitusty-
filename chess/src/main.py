import pygame as p
import sys
import os
from gamestate.boardstate import BoardState
from pieces import Piece
clock = p.time.Clock()
fps = 30
BS = BoardState()
Piece = Piece()
width = height = 512
square = height // 8
dirname = os.path.dirname(__file__)
p.init()
screen = p.display.set_mode((width, height))

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
                if BS.boardstate[pos_sq[1]][pos_sq[0]] != "" or len(player_clicks) > 0:
                    if pos_sq in player_clicks:
                        player_clicks = []
                    else:
                        player_clicks.append(pos_sq)
                if len(player_clicks) == 2:
                    movePiece(player_clicks[0],player_clicks[1], BS.boardstate)
                    player_clicks = []
        drawBoard(BS.boardstate)
        clock.tick(fps)
        p.display.flip()

def drawBoard(boardstate):
    colors = [(235, 235, 208), (119, 148, 85)]
    for row in range(8):
        for colum in range(8):
            color = colors[((row+colum) % 2)]
            p.draw.rect(screen, color, p.Rect(colum*square, row*square, square, square))
            piece = boardstate[row][colum]
            if piece != "":
                screen.blit(Piece.images[piece], p.Rect(colum*square, row*square, square, square))

def movePiece(s_pos, d_pos, boardstate):
    piece = boardstate[s_pos[1]][s_pos[0]]
    if boardstate[d_pos[1]][d_pos[0]] != "":
        capture = boardstate[d_pos[1]][d_pos[0]]
    else:
        capture = ""
    valid = Piece.isValid(piece, s_pos, d_pos, capture)
    if valid:
        BS.changeBoardState(piece, s_pos, d_pos)
    else:
        return




    



main()