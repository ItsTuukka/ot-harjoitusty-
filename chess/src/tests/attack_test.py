import unittest
from attack import Attack
from gamestate import GameState
from pieces import Piece
GS = GameState()
A = Attack(GS)
Piece = Piece(GS, A)


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