from tkinter import ttk, constants

class UsernameSelect:
    def __init__(self, root, handle_game_start):
        self._root = root
        self.handle_game_start = handle_game_start
        self._frame = None

        self.initialize()
    
    def pack(self):
        self._frame.pack(fill = constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        head_label = ttk.Label(master=self._frame, text="Input player names", font="none 18 bold")
        player1_label = ttk.Label(master=self._frame, text="Player 1 (white pieces)", font="none 11")
        player1_entry = ttk.Entry(master=self._frame)
        player2_label = ttk.Label(master=self._frame, text="Player 2 (black pieces)", font="none 11")
        player2_entry = ttk.Entry(master=self._frame)
        start_button = ttk.Button(
            master=self._frame,
            text="Start",
            command=self.handle_game_start
            )

        head_label.grid(pady=5)
        player1_label.grid(pady=5)
        player1_entry.grid(pady=5)
        player2_label.grid(pady=5)
        player2_entry.grid(pady=5)
        start_button.grid(pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=550)