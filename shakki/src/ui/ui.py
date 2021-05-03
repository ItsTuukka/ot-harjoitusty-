from ui.menu import Menu
from ui.username_select import UsernameSelect
from ui.white_wins import WhiteWins
from ui.black_wins import BlackWins
from ui.draw import Draw

class UI:
    def __init__(self, root, run_game):
        self._root = root
        self.run_game = run_game
        self._current_view = None

    def start(self):
        self.show_menu()
    
    def end(self, result):
        if result == 1:
            self.show_white_wins()
        if result == 2:
            self.show_draw()
        else:
            self.show_black_wins()
    
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
    
    def handle_game_start(self):
        self.show_game_start()

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
    
    def show_game_start(self):
        self.hide_current_view()
        self._root.destroy()
        self.run_game()
    
    def show_white_wins(self):
        self.hide_current_view()
        self._current_view = WhiteWins(
            self._root,
            self.hand_start
        )
        self._current_view.pack()
    
    def show_black_wins(self):
        self.hide_current_view()
        self._current_view = BlackWins(
            self._root,
            self.hand_start
        )
        self._current_view.pack()
    
    def show_draw(self):
        self.hide_current_view()
        self._current_view = Draw(
            self._root,
            self.hand_start
        )
        self._current_view.pack()
