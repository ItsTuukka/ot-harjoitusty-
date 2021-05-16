from ui.menu import Menu
from ui.username_select import UsernameSelect
from ui.end_screen import EndScreen
from ui.match_history import MatchHistory

class UI:

    """Class that handles the UI. Handles all the different screens
    and shows/hides views according to player input.

    Attributes:
        root: Root for tkinter.
        run_game: Function that calls the main function of the game.
        player1: Username for player1.
        player1: Username for player2.
    """

    def __init__(self, root, run_game, player1=None, player2=None):
        """Constructor for the class.

        Args:
            root: Root for tkinter.
            run_game: Function that calls the main function of the game.
            player1: Username for player1. Value is None before user input.
            player1: Username for player2. Value is None before user input.
        """

        self._root = root
        self.run_game = run_game
        self._current_view = None
        self._player1 = player1
        self._player2 = player2

    def start(self):
        """Calls the function to show the main manu.
        """

        self.show_menu()
    
    def end(self, result):
        """Calls the end screen, based on the result.

        Args:
            result: Result of the game.
        """

        if result == 1:
            self.show_end(self._player1 + " wins!")
        elif result == 2:
            self.show_end("Draw!")
        elif result == 3:
            self.show_end(self._player2 + " wins!")
    
    def hide_current_view(self):
        """Hides the current screen.
        """

        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
    
    def handle_start(self):
        """Calls the start function, used for a button command.
        """

        self.start()

    def handle_username_select(self):
        """Calls the fucntion to show username select, used for a button command.
        """

        self.show_username_select()

    def handle_game_history(self):
        """Calls the fucntion to show match history, used for a button command.
        """

        self.show_game_history()
    
    def handle_game_start(self, player1, player2):
        """Calls the fucntion to show the game screen, used for a button command.

        Args:
            player1: Username for player1. 
            player2: Username for player2. 
        """

        self.show_game_start(player1, player2)

    def show_menu(self):
        """Shows the menu screen.
        """

        self.hide_current_view()
        self._current_view = Menu(
            self._root,
            self.handle_username_select,
            self.handle_game_history,
        )
        self._current_view.pack()
    
    def show_username_select(self):
        """Shows the username select screen.
        """

        self.hide_current_view()
        self._current_view = UsernameSelect(
            self._root,
            self.handle_game_start
        )
        self._current_view.pack()
    
    def show_game_start(self, player1, player2):
        """Shows the game view and destroyes the current tkinter root.

        Args:
            player1: Username for player1. 
            player2: Username for player2.
        """
        
        self.hide_current_view()
        self._root.destroy()
        self.run_game(player1, player2)
    
    def show_game_history(self):
        history = MatchHistory(
            self.handle_start
        )
        history.pack()
        history.start_up()
        
    
    def show_end(self, result):
        self.hide_current_view()
        self._current_view = EndScreen(
            self._root,
            self.handle_start,
            result
        )
        self._current_view.pack()
    
