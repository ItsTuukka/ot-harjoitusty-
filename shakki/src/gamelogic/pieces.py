import os
import pygame
dirname = os.path.dirname(__file__)
square = 64


class Piece:

    """This class is responsible for all things considering pieces.

    Attributes:
        GS: GameState class.
        gs: boardstate from the GameState class.
        A: Attack class.
        Result: Result class.
        images: Dictionary containing pictures of the pieces.
        castle: Boolean for is the player trying to castle.
        enpassant: Boolean for is the player trying to enpassant.

    Source for the images used: https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent,
    author: Cburnett
    """

    def __init__(self, GS, Attack, Result):
        """Constructor for the class, calls the function that 
        loads images of the pieces to a dictionary.

        Args:
            GS: GameState class.
            Attack: Attack class.
            Result: Result class.
        """

        self.GS = GS
        self.gs = GS.boardstate
        self.A = Attack
        self.Result = Result
        self.images = self.loadimages()
        self.castle = False
        self.enpassant = False

    def loadimages(self):
        """Loads the images for all pieces to a dictionary.

        Returns:
            Dictionary containing images of the pieces.
        """

        pieces = {}
        for row in self.gs:
            for column in row:
                if column != "":
                    pieces[column] = pygame.transform.scale(pygame.image.load(
                        os.path.join(dirname, "../assets/" + column + ".png")), (square, square))
        return pieces

    def movePiece(self, s_pos, d_pos):
        """Takes the relevant information considering a move, and gives them forward
        if the move is valid.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.
        """
        self.castle = False
        self.enpassant = False
        piece = self.gs[s_pos[1]][s_pos[0]]
        capture = self.gs[d_pos[1]][d_pos[0]]
        valid = self.isValid(piece, s_pos, d_pos, capture)
        copy = [i[:] for i in self.gs]
        if valid:
            if not self.A.check_after(piece, s_pos, d_pos, copy):
                self.GS.changeBoardState(
                    piece, s_pos, d_pos, self.castle, self.enpassant)
                self.Result.move(s_pos, d_pos)
            else:
                return
        else:
            return
        self.after_move()

    def after_move(self):
        """Runs the functions that are needed after a valid move.
        """

        self.A.white_threatens(self.gs)
        self.A.black_threatens(self.gs)
        self.A.check()
        self.Result.check_stalemate()
        self.Result.insufficient_material()
        self.Result.fivefold_repetition()

    def isValid(self, piece, s_pos, d_pos, capture):
        """Checks the rank of the piece, gives the information to that ranks
        move validation function.

        Args:
            piece: Piece that is trying to move.
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.
            capture: Piece that is being captured, can also be an empty square.

        Returns:
            True, if the move is valid, otherwise False
        """

        color = piece[0]
        rank = piece[1]
        if self.GS.move_white:
            if color == "b":
                return False
        else:
            if color == "w":
                return False
        if capture != "":
            if capture[0] == color and piece[1] == "K" and capture[1] == "R":
                if self.castling(piece[0], s_pos, d_pos):
                    self.castle = True
                    return True
            if capture[0] == color or capture[1] == "K":
                return False
        if rank == "P":
            if self.pawn_move(color, s_pos, d_pos, capture):
                return True
        if rank == "N":
            if self.knight_move(s_pos, d_pos):
                return True
        if rank == "B":
            if self.bishop_move(s_pos, d_pos):
                return True
        if rank == "R":
            if self.rook_move(s_pos, d_pos):
                return True
        if rank == "Q":
            if self.queen_move(s_pos, d_pos):
                return True
        if rank == "K":
            if self.king_move(s_pos, d_pos):
                return True
        return False

    def pawn_move(self, color, s_pos, d_pos, capture):
        """Move validation function for pawns.

        Args:
            color: Color of the piece.
            s_pos: Starting postion of thece.
            d_pos: Position where to piece is trying to move.
            capture: Piece that is being captured, can also be an empty square.

        Returns:
            True if the move is valid, otherwise False.
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

    def rook_move(self, s_pos, d_pos):
        """Move validation function for rooks.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True if the move is valid, otherwise False.
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

    def knight_move(self, s_pos, d_pos):
        """Move validation function for knights.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True if the move is valid, otherwise False.
        """

        if abs(s_pos[0]-d_pos[0]) == 2 and abs(s_pos[1]-d_pos[1]) == 1:
            return True
        if abs(s_pos[0]-d_pos[0]) == 1 and abs(s_pos[1]-d_pos[1]) == 2:
            return True
        return False

    def bishop_move(self, s_pos, d_pos):
        """Move validation function for bishop.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True if the move is valid, otherwise False.
        """

        if abs(s_pos[0]-d_pos[0]) == abs(s_pos[1]-d_pos[1]):
            if self.GS.betweenDiagonally(s_pos, d_pos):
                return False
            return True
        return False

    def queen_move(self, s_pos, d_pos):
        """Move validation function for queens.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True if the move is valid, otherwise False.
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

    def king_move(self, s_pos, d_pos):
        """Move validation function for kings.

        Args:
            s_pos: Starting postion of the piece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True if the move is valid, otherwise False.
        """

        if abs(s_pos[0]-d_pos[0]) <= 1 and abs(s_pos[1]-d_pos[1]) <= 1:
            return True
        return False

    def castling(self, color, s_pos, d_pos):
        """If the player is trying to castle, this function checks 
        if it is possible.

        Args:
            color: Color of the piece.
            s_pos: Starting postion of thece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True if castling is possible, otherwise False.
        """

        if self.GS.betweenHorizontally(s_pos, d_pos):
            return False
        if color == "w":
            if self.GS.white_in_check:
                return False
            if not self.GS.white_king_moved:
                if d_pos[0] > s_pos[0]:
                    for x in range(s_pos[0], d_pos[0]):
                        if self.A.black_attacks[s_pos[1]][x] == 1:
                            return False
                else:
                    for x in range(d_pos[0]+1, s_pos[0]+1):
                        if self.A.black_attacks[s_pos[1]][x] == 1:
                            return False
                if d_pos == (0, 7):
                    if not self.GS.lw_rook_moved:
                        return True
                if d_pos == (7, 7):
                    if not self.GS.rw_rook_moved:
                        return True
        else:
            if self.GS.black_in_check:
                return False
            if not self.GS.black_king_moved:
                if d_pos[0] > s_pos[0]:
                    for x in range(s_pos[0], d_pos[0]):
                        if self.A.white_attacks[s_pos[1]][x] == 1:
                            return False
                else:
                    for x in range(d_pos[0]+1, s_pos[0]+1):
                        if self.A.white_attacks[s_pos[1]][x] == 1:
                            return False
                if d_pos == (0, 0):
                    if not self.GS.lb_rook_moved:
                        return True
                if d_pos == (7, 0):
                    if not self.GS.rb_rook_moved:
                        return True
        return False

    def en_passant(self, s_pos, d_pos):
        """If the player is trying to en passant, this function checks 
        if it is possible.

        Args:
            s_pos: Starting postion of thece.
            d_pos: Position where to piece is trying to move.

        Returns:
            True if enpassant is possible, otherwise False.
        """

        lastmove = self.GS.move_log[-1]
        if abs(lastmove[0][1] - lastmove[1][1]) == 2 and "P" in lastmove[2]:
            if s_pos[1] == lastmove[1][1] and abs(s_pos[0]-lastmove[1][0]) == 1 and abs(d_pos[1]-lastmove[1][1]) == 1 and d_pos[0] == lastmove[1][0]:
                self.enpassant = True
                return True
        return False
