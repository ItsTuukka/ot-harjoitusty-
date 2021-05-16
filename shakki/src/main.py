import sys
import pygame as p
from tkinter import Tk
from gamelogic.gamestate import GameState
from gamelogic.pieces import Piece
from gamelogic.attack import Attack
from gamelogic.chesslib import Result
from ui.ui import UI
from repositories.match_history_repository import MatchHistoryRepository
FPS = 30
WIDTH = HEIGHT = 512
SQUARE = HEIGHT // 8


def main(player1, player2):
    """This is the main function that starts the game and goes through user inputs.

    Args:
        player1: Username for player1.
        player2: Username for player2.
    """

    clock = p.time.Clock()
    GS = GameState()
    result = Result(GS)
    A = Attack(GS, result)
    piece = Piece(GS, A, result)
    match_history = MatchHistoryRepository()
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    player_clicks = []
    while True:
        for e in p.event.get():
            if e.type == p.QUIT:
                sys.exit()
            if e.type == p.MOUSEBUTTONDOWN:
                position = p.mouse.get_pos()
                pos_sq = (position[0]//SQUARE, position[1]//SQUARE)
                if GS.boardstate[pos_sq[1]][pos_sq[0]] != "" or len(player_clicks) > 0:
                    if pos_sq in player_clicks:
                        player_clicks = []
                    else:
                        player_clicks.append(pos_sq)
                if len(player_clicks) == 2:
                    piece.movePiece(player_clicks[0], player_clicks[1])
                    player_clicks = []
        draw_board(screen, GS, piece)
        clock.tick(FPS)
        p.display.flip()
        if GS.game_result:
            end_game(player1, player2, match_history, GS)
            break


def end_game(player1, player2, match_history, GS):
    """Sends game information to be saved and calls end game screen.

    Args:
        player1: Username for player1.
        player2: Username for player2.
        match_history: Match history class.
        GS: GameState class.
    """

    match_history.add_score(player1, player2, GS.game_result)
    p.quit()
    window = Tk()
    window.title("Chess")
    ui = UI(window, main, player1, player2)
    ui.end(GS.game_result)
    window.mainloop()


def draw_board(screen, GS, piece_class):
    """Draws the board, squares and pieces.

    Args:
        screen: Pygame display.
        GS: GameState class.
        piece_class: Piece class.
    """

    colors = [(235, 235, 208), (119, 148, 85)]
    for row in range(8):
        for colum in range(8):
            color = colors[((row+colum) % 2)]
            p.draw.rect(screen, color, p.Rect(
                colum*SQUARE, row*SQUARE, SQUARE, SQUARE))
            piece = GS.boardstate[row][colum]
            if piece != "":
                screen.blit(piece_class.images[piece], p.Rect(
                    colum*SQUARE, row*SQUARE, SQUARE, SQUARE))
