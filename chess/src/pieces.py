import pygame
import os
dirname = os.path.dirname(__file__)
square = 64

class Piece:

    """
    This class is responsible for all things considering pieces.
    Source for the images used: https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent,
    author: Cburnett
    """
    


    def __init__(self, GS):
        self.GS = GS
        self.gs = GS.boardstate
        self.images = self.loadimages()



    def loadimages(self):
        pieces = {}
        for row in self.gs:
            for colum in row:
                if colum != "":
                    pieces[colum] = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "assets/" + colum + ".png")), (square, square))
        return pieces
    

    def movePiece(self, s_pos, d_pos):
        piece = self.gs[s_pos[1]][s_pos[0]]
        capture = self.gs[d_pos[1]][d_pos[0]]
        valid = self.isValid(piece, s_pos, d_pos, capture)
        if valid:
            self.GS.changeBoardState(piece, s_pos, d_pos)
        else:
            return


    def isValid(self, piece, s_pos, d_pos, capture):
        color = piece[0]
        rank = piece[1]
        if capture != "":
            if capture[0] == color or capture[1] == "K":
                return
        if rank == "P":
            if self.pawn(color, s_pos, d_pos, capture):
                return True
        if rank == "N":
            if self.knight(s_pos, d_pos):
                return True
        if rank == "B":
            if self.bishop(s_pos, d_pos):
                return True
        if rank == "R":
            if self.rook(s_pos, d_pos):
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

    
    def rook(self, s_pos, d_pos):
        if s_pos[0] == d_pos[0]:
            if self.GS.betweenVertically(s_pos, d_pos):
                return False
            return True
        if s_pos[1] == d_pos[1]:
            if self.GS.betweenHorizontally(s_pos, d_pos):
                return False
            return True
        return False


    def knight(self, s_pos, d_pos):
        if abs(s_pos[0]-d_pos[0]) == 2 and abs(s_pos[1]-d_pos[1]) == 1:
            return True
        if abs(s_pos[0]-d_pos[0]) == 1 and abs(s_pos[1]-d_pos[1]) == 2:
            return True
        return False
        
    
    def bishop(self, s_pos, d_pos):
        if abs(s_pos[0]-d_pos[0]) == abs(s_pos[1]-d_pos[1]):
            if self.GS.betweenDiagonally(s_pos, d_pos):
                return False
            return True
        return False  


                    


        
