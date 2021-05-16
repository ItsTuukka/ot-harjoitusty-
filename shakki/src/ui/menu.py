from tkinter import ttk, constants
import sys


class Menu:

    """Class for the menu screen.

    Attributes:
        root: Root for tkinter. 
        handle_username_select. Function for username select.
        handle_game_history: Function for game history.
        frame: Initializing the frame object.
    """

    def __init__(self, root, handle_username_select, handle_game_history):
        """Constructor for the class, calls the function
        to initialize the screen. 

        Args:
            root: Root for tkinter. 
            handle_username_select. Function for username select.
            handle_game_history: Function for game history.
        """

        self._root = root
        self.handle_username_select = handle_username_select
        self.handle_game_history = handle_game_history
        self._frame = None

        self.initialize()

    def pack(self):
        """For showing the screen.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """For hiding the screen.
        """

        self._frame.destroy()

    def initialize(self):
        """Initializes all the objects to be shown.
        """

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Main Menu", font="italic 22 bold")
        username_select = ttk.Button(
            master=self._frame,
            text="Start Game",
            command=self.handle_username_select,
        )
        game_history = ttk.Button(
            master=self._frame,
            text="Match History",
            command=self.handle_game_history
        )
        exit_game = ttk.Button(
            master=self._frame,
            text="Exit",
            command=sys.exit
        )

        label.grid(pady=10)
        username_select.grid(pady=10)
        game_history.grid(pady=10)
        exit_game.grid(pady=10)

        self._frame.grid_columnconfigure(0, weight=1, minsize=550)
