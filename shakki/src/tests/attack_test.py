import unittest
from gamelogic.attack import Attack
from gamelogic.gamestate import GameState
from gamelogic.pieces import Piece
from gamelogic.chesslib import Result
GS = GameState()
Result = Result(GS)
A = Attack(GS, Result)
Piece = Piece(GS, A, Result)


class TestAttack(unittest.TestCase):
    def setUp(self):
        self.starting_attack = [[0]*8 for _ in range(8)]

    def test_attack(self):
        self.assertEqual(A.white_attacks, self.starting_attack)
        self.assertEqual(A.black_attacks, self.starting_attack)
        Piece.movePiece((6,6), (6,5))
        white = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1], [1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,0]]
        self.assertEqual(A.white_attacks, white)
        Piece.movePiece((6,1), (6,2))
        black = [[0,1,1,1,1,1,1,0], [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], [0,0,0,0,0,1,0,1],
                [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
        self.assertEqual(A.black_attacks, black)
    
    def test_check_after(self):
        Piece.movePiece((4,6), (4,4))
        self.assertEqual(A.check_after('wP', (4,6), (4,4), GS.boardstate), False)
        Piece.movePiece((4,1), (4,2))
        Piece.movePiece((6,7), (5,5))
        Piece.movePiece((5,0), (1,4))
        self.assertEqual(A.check_after('wP', (3,6), (3,5), GS.boardstate), True)