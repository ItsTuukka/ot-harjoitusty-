from ui.menu import Menu
from ui.username_select import UsernameSelect
from ui.someone_wins import SomeoneWins
from ui.draw import Draw

class UI:
    def __init__(self, root, run_game, player1=None, player2=None):
        self._root = root
        self.run_game = run_game
        self._current_view = None
        self._player1 = player1
        self._player2 = player2

    def start(self):
        self.show_menu()
    
    def end(self, result):
        if result == 1:
            self.show_someone_wins(self._player1)
        elif result == 2:
            self.show_draw()
        else:
            self.show_someone_wins(self._player2)
    
    def hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
    
    def hand_start(self):
        self.start()

    def handle_username_select(self):
        self.show_username_select()

    def handle_game_history(self):
        self.show_game_history()
    
    def handle_game_start(self, player1, player2):
        self.show_game_start(player1, player2)

    def show_menu(self):
        self.hide_current_view()
        self._current_view = Menu(
            self._root,
            self.handle_username_select,
            self.handle_game_history,
        )
        self._current_view.pack()
    
    def show_username_select(self):
        self.hide_current_view()
        self._current_view = UsernameSelect(
            self._root,
            self.handle_game_start
        )
        self._current_view.pack()
    
    def show_game_start(self, player1, player2):
        self.hide_current_view()
        self._root.destroy()
        self.run_game(player1, player2)
    
    def show_someone_wins(self, winner):
        self.hide_current_view()
        self._current_view = SomeoneWins(
            self._root,
            self.hand_start,
            winner
        )
        self._current_view.pack()
    
    def show_draw(self):
        self.hide_current_view()
        self._current_view = Draw(
            self._root,
            self.hand_start
        )
        self._current_view.pack()
