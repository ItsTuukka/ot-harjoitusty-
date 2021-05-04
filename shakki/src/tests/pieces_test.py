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
    

    def test_castle(self):
        self.assertEqual(Piece.castle("w", (4,7), (7,7)), False)
        self.assertEqual(Piece.castle("b", (4,0), (7,0)), False)
        Piece.movePiece((4,6), (4,4))
        Piece.movePiece((4,1), (4,3))
        Piece.movePiece((5,7), (4,6))
        Piece.movePiece((5,0), (4,1))
        Piece.movePiece((6,7), (5,5))
        Piece.movePiece((6,0), (5,2))
        self.assertEqual(Piece.castle("w", (4,7), (7,7)), True)
        self.assertEqual(Piece.castle("b", (4,0), (7,0)), True)
    
    # def test_enpassant(self):
    #     Piece.movePiece((4,6), (4,4))
    #     Piece.movePiece((4,1), (4,2))
    #     Piece.movePiece((4,4), (4,3))
    #     Piece.movePiece((3,1), (3,3))
    #     self.assertEqual(Piece.en_passant((4,3), (3,2)), True)



    