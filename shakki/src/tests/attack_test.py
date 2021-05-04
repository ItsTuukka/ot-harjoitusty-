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
    def setUp(self,):
        self.starting_attack = [[0]*8 for _ in range(8)]

    def test_attack(self):
        self.assertEqual(A.whiteAttacks, self.starting_attack)
        self.assertEqual(A.blackAttacks, self.starting_attack)
        Piece.movePiece((6,6), (6,5))
        white = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,1], [1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,0]]
        self.assertEqual(A.whiteAttacks, white)
        Piece.movePiece((6,1), (6,2))
        black = [[0,1,1,1,1,1,1,0], [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], [0,0,0,0,0,1,0,1],
                [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
        self.assertEqual(A.blackAttacks, black)