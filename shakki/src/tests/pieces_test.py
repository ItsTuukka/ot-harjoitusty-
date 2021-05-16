import unittest
from gamelogic.attack import Attack
from gamelogic.gamestate import GameState
from gamelogic.pieces import Piece
from gamelogic.chesslib import Result
GS = GameState()
Result = Result(GS)
A = Attack(GS, Result)
Piece = Piece(GS, A, Result)

class TestPieces(unittest.TestCase):
    

    def test_castling(self):
        self.assertEqual(Piece.castling("w", (4,7), (7,7)), False)
        self.assertEqual(Piece.castling("b", (4,0), (7,0)), False)
        Piece.movePiece((4,6), (4,4))
        Piece.movePiece((4,1), (4,3))
        Piece.movePiece((5,7), (4,6))
        Piece.movePiece((5,0), (4,1))
        Piece.movePiece((6,7), (5,5))
        Piece.movePiece((6,0), (5,2))
        self.assertEqual(Piece.castling("w", (4,7), (7,7)), True)
        self.assertEqual(Piece.castling("b", (4,0), (7,0)), True)
    
    def test_enpassant(self):
        Piece.movePiece((4,6), (4,4))
        Piece.movePiece((4,1), (4,2))
        Piece.movePiece((4,4), (4,3))
        Piece.movePiece((3,1), (3,3))
        GS.move_log[-1] = ((3,1), (3,3), 'bP')
        self.assertEqual(Piece.en_passant((4,3), (3,2)), True)
    
    def test_if_valid(self):
        self.assertEqual(Piece.isValid("wP", (4,6), (4,3), ""), False)
        self.assertEqual(Piece.isValid("wP", (4,6), (4,5), ""), True)
        self.assertEqual(Piece.isValid("wK", (4,6), (4,3), ""), False)
        self.assertEqual(Piece.isValid("wK", (4,6), (4,5), ""), True)
        self.assertEqual(Piece.isValid("bQ", (4,6), (1,3), ""), False)



    