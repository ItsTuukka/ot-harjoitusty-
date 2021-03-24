import pygame as p
import sys
import os
from gamestate.boardstate import BoardState
BS = BoardState()
width = height = 512
square = height // 8
dirname = os.path.dirname(__file__)
p.init()
screen = p.display.set_mode((width, height))

def main():
    screen.fill((0,0,0))
    pieces = loadPieces(BS.boardstate)
    drawBoard()
    drawPieces(pieces, BS.boardstate)
    player_clicks = []
    while True:
        for e in p.event.get():
            if e.type == p.QUIT:
                sys.exit()
            if e.type == p.MOUSEBUTTONDOWN:
                position = p.mouse.get_pos()
                pos_sq = (position[0]//64, position[1]//64)
                if BS.boardstate[pos_sq[1]][pos_sq[0]] != "":
                    player_clicks.append((pos_sq[0],pos_sq[1]))
                if len(player_clicks) == 2:
                    movePiece(player_clicks[0],player_clicks[1], BS.boardstate)
                    player_clicks = []
        p.display.flip()

def drawBoard():
    colors = [(235, 235, 208), (119, 148, 85)]
    for row in range(8):
        for colum in range(8):
            color = colors[((row+colum) % 2)]
            p.draw.rect(screen, color, p.Rect(row*square, colum*square, square, square))

def loadPieces(boardstate):
    pieces = {}
    for row in boardstate:
        for colum in row:
            if colum != "":
                pieces[colum] = p.transform.scale(p.image.load(os.path.join(dirname, "assets/" + colum + ".png")), (square, square))
    return pieces

def drawPieces(pieces, boardstate):
    for row in range(8):
        for colum in range(8):
            piece = boardstate[row][colum]
            if piece != "":
                screen.blit(pieces[piece], (colum*square, row*square))

def movePiece(s_pos, d_pos, boardstate):
    piece = boardstate[s_pos[1]][s_pos[0]]
    changeBoardState(piece, s_pos, d_pos)




    



main()