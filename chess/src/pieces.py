import pygame
import os
from gamestate.boardstate import BoardState
dirname = os.path.dirname(__file__)
square = 64

class Piece:

    def __init__(self):
        self.images = self.loadimages(BoardState().boardstate)


    def loadimages(self, boardstate):
        pieces = {}
        for row in boardstate:
            for colum in row:
                if colum != "":
                    pieces[colum] = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "assets/" + colum + ".png")), (square, square))
        return pieces

    def isValid(self, piece, s_pos, d_pos, capture):
        color = piece[0]
        rank = piece[1]
        if capture != "" and color == capture[0]:
            return
        if color == "w":
            if rank == "P":
                if self.pawn(color, s_pos, d_pos, capture):
                    return True
        else:
            if rank == "P":
                if self.pawn(color, s_pos, d_pos, capture):
                    return True
        return False

    def pawn(self, color, s_pos, d_pos, capture):
        if color == "w":
            if capture != "":
                if s_pos[1] - d_pos[1] == 1 and abs(s_pos[0]-d_pos[0]):
                    return True
            else:
                if s_pos[1] == 6:
                    if s_pos[1] - d_pos[1] == 2 and d_pos[0] == s_pos[0]:
                        return True
                if s_pos[1] - d_pos[1] == 1 and d_pos[0] == s_pos[0]:
                    return True
        else:
            if capture != "":
                if d_pos[1] - s_pos[1] == 1 and abs(s_pos[0]-d_pos[0]):
                    return True
            else:
                if s_pos[1] == 1:
                    if d_pos[1] - s_pos[1] == 2 and d_pos[0] == s_pos[0]:
                        return True
                if d_pos[1] - s_pos[1] == 1 and d_pos[0] == s_pos[0]:
                    return True
        return False

