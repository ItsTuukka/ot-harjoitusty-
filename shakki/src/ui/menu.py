from tkinter import ttk, constants
import sys

class Menu:
    def __init__(self, root, handle_username_select, handle_game_history):
        self._root = root
        self.handle_username_select = handle_username_select
        self.handle_game_history = handle_game_history
        self._frame = None

        self.initialize()
    
    def pack(self):
        self._frame.pack(fill = constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Menu", font="italic 22 bold")
        username_select = ttk.Button(
            master=self._frame,
            text="Start Game",
            command=self.handle_username_select,
        )
        game_history = ttk.Button(
            master=self._frame,
            text="Game History (coming soon)",
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
