from menu import Menu
from username_select import UsernameSelect

class UI:
    def __init__(self, root, run_game):
        self._root = root
        self.run_game = run_game
        self._current_view = None

    def start(self):
        self.show_menu()
    
    def hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

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
        self.hide_current_view
        self.run_game()
    
