import os
import pygame
dirname = os.path.dirname(__file__)
square = 64


class Piece:

    """
    This class is responsible for all things considering pieces.
    Source for the images used: https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent,
    author: Cburnett
    """

    def __init__(self, GS, Attack, Result):
        self.GS = GS
        self.gs = GS.boardstate
        self.A = Attack
        self.Result = Result
        self.images = self.loadimages()
        self.Castle = False
        self.enpassant = False

    def loadimages(self):
        """Loads the images for all pieces to a dictionary.
        """
        pieces = {}
        for row in self.gs:
            for colum in row:
                if colum != "":
                    pieces[colum] = pygame.transform.scale(pygame.image.load(
                        os.path.join(dirname, "../assets/" + colum + ".png")), (square, square))
        return pieces

    def movePiece(self, s_pos, d_pos):
        """Takes the relevant information considering a move, and gives them forward
        if the move is valid.
        """
        self.Castle = False
        self.enpassant = False
        piece = self.gs[s_pos[1]][s_pos[0]]
        capture = self.gs[d_pos[1]][d_pos[0]]
        valid = self.isValid(piece, s_pos, d_pos, capture)
        copy = [i[:] for i in self.gs]
        if valid:
            if not self.A.check_after(piece, s_pos, d_pos, copy):
                self.GS.changeBoardState(
                    piece, s_pos, d_pos, self.Castle, self.enpassant)
                self.Result.move(s_pos, d_pos)
            else:
                return
        else:
            return
        self.after_move()

    def after_move(self):
        """Runs the functions that are needed after a valid move.
        """
        self.A.whiteThreatens(self.gs)
        self.A.blackThreatens(self.gs)
        self.A.check()
        self.Result.check_stalemate()
        self.Result.insufficient_material()

    def isValid(self, piece, s_pos, d_pos, capture):
        """Checks the rank of the piece, gives the information to that ranks
        move validation function and returns if the move is valid.
        """
        color = piece[0]
        rank = piece[1]
        if self.GS.moveWhite:
            if color == "b":
                return False
        else:
            if color == "w":
                return False
        if capture != "":
            if capture[0] == color and piece[1] == "K" and capture[1] == "R":
                if self.castle(piece[0], s_pos, d_pos):
                    self.Castle = True
                    return True
            if capture[0] == color or capture[1] == "K":
                return False
        if rank == "P":
            if self.pawnMove(color, s_pos, d_pos, capture):
                return True
        if rank == "N":
            if self.knightMove(s_pos, d_pos):
                return True
        if rank == "B":
            if self.bishopMove(s_pos, d_pos):
                return True
        if rank == "R":
            if self.rookMove(s_pos, d_pos):
                return True
        if rank == "Q":
            if self.queenMove(s_pos, d_pos):
                return True
        if rank == "K":
            if self.kingMove(s_pos, d_pos):
                return True

    def pawnMove(self, color, s_pos, d_pos, capture):
        """Move validation function for pawns, returns True if valid.
        """
        if color == "w":
            if capture != "":
                if s_pos[1] - d_pos[1] == 1 and abs(s_pos[0]-d_pos[0]) == 1:
                    return True
            else:
                if s_pos[1] - d_pos[1] == 1 and abs(s_pos[0]-d_pos[0]) == 1:
                    if self.en_passant(s_pos, d_pos):
                        return True
                if s_pos[1] == 6:
                    if s_pos[1] - d_pos[1] == 2 and d_pos[0] == s_pos[0]:
                        return True
                if s_pos[1] - d_pos[1] == 1 and d_pos[0] == s_pos[0]:
                    return True
        else:
            if capture != "":
                if d_pos[1] - s_pos[1] == 1 and abs(s_pos[0]-d_pos[0]) == 1:
                    return True
            else:
                if d_pos[1] - s_pos[1] == 1 and abs(s_pos[0]-d_pos[0]) == 1:
                    if self.en_passant(s_pos, d_pos):
                        return True
                if s_pos[1] == 1:
                    if d_pos[1] - s_pos[1] == 2 and d_pos[0] == s_pos[0]:
                        return True
                if d_pos[1] - s_pos[1] == 1 and d_pos[0] == s_pos[0]:
                    return True
        return False

    def rookMove(self, s_pos, d_pos):
        """Move validation function for rooks, returns True if valid.
        """
        if s_pos[0] == d_pos[0]:
            if self.GS.betweenVertically(s_pos, d_pos):
                return False
            return True
        if s_pos[1] == d_pos[1]:
            if self.GS.betweenHorizontally(s_pos, d_pos):
                return False
            return True
        return False

    def knightMove(self, s_pos, d_pos):
        """Move validation function for knights, returns True if valid.
        """
        if abs(s_pos[0]-d_pos[0]) == 2 and abs(s_pos[1]-d_pos[1]) == 1:
            return True
        if abs(s_pos[0]-d_pos[0]) == 1 and abs(s_pos[1]-d_pos[1]) == 2:
            return True
        return False

    def bishopMove(self, s_pos, d_pos):
        """Move validation function for bishop, returns True if valid.
        """
        if abs(s_pos[0]-d_pos[0]) == abs(s_pos[1]-d_pos[1]):
            if self.GS.betweenDiagonally(s_pos, d_pos):
                return False
            return True
        return False

    def queenMove(self, s_pos, d_pos):
        """Move validation function for queens, returns True if valid.
        """
        if abs(s_pos[0]-d_pos[0]) == abs(s_pos[1]-d_pos[1]):
            if self.GS.betweenDiagonally(s_pos, d_pos):
                return False
            return True
        if s_pos[0] == d_pos[0]:
            if self.GS.betweenVertically(s_pos, d_pos):
                return False
            return True
        if s_pos[1] == d_pos[1]:
            if self.GS.betweenHorizontally(s_pos, d_pos):
                return False
            return True
        return False

    def kingMove(self, s_pos, d_pos):
        """Move validation function for kings, returns True if valid.
        """
        if abs(s_pos[0]-d_pos[0]) <= 1 and abs(s_pos[1]-d_pos[1]) <= 1:
            return True
        return False

    def castle(self, color, s_pos, d_pos):
        """If the player is trying to castle, this function checks 
        if it is possible.
        """
        if self.GS.betweenHorizontally(s_pos, d_pos):
            return False
        if color == "w":
            if self.GS.white_in_check:
                return False
            if not self.GS.wKmove:
                if d_pos[0] > s_pos[0]:
                    for x in range(s_pos[0], d_pos[0]):
                        if self.A.blackAttacks[s_pos[1]][x] == 1:
                            return False
                else:
                    for x in range(d_pos[0]+1, s_pos[0]+1):
                        if self.A.blackAttacks[s_pos[1]][x] == 1:
                            return False
                if d_pos == (0, 7):
                    if not self.GS.LwRmove:
                        return True
                if d_pos == (7, 7):
                    if not self.GS.RwRmove:
                        return True
        else:
            if self.GS.black_in_check:
                return False
            if not self.GS.bKmove:
                if d_pos[0] > s_pos[0]:
                    for x in range(s_pos[0], d_pos[0]):
                        if self.A.whiteAttacks[s_pos[1]][x] == 1:
                            return False
                else:
                    for x in range(d_pos[0]+1, s_pos[0]+1):
                        if self.A.whiteAttacks[s_pos[1]][x] == 1:
                            return False
                if d_pos == (0, 0):
                    if not self.GS.LbRmove:
                        return True
                if d_pos == (7, 0):
                    if not self.GS.RwRmove:
                        return True
        return False

    def en_passant(self, s_pos, d_pos):
        """If the player is trying to en passant, this function checks 
        if it is possible.
        """
        lastmove = self.GS.move_log[-1]
        if abs(lastmove[0][1] - lastmove[1][1]) == 2 and "P" in lastmove[2]:
            if s_pos[1] == lastmove[1][1] and abs(s_pos[0]-lastmove[1][0]) == 1 and abs(d_pos[1]-lastmove[1][1]) == 1 and d_pos[0] == lastmove[1][0]:
                self.enpassant = True
                return True
        return False
