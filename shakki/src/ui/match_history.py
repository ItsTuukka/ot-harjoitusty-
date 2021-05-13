from tkinter import Tk, ttk, constants
from repositories.match_history_repository import MatchHistoryRepository
Repository = MatchHistoryRepository()


class MatchHistory:
    def __init__(self, handle_start):
        self._root = Tk()
        self._root.title("Match History")
        self.handle_start = handle_start
        self._frame = None

        self.initialize()
    
    def pack(self):
        self._frame.pack(fill = constants.X)

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        scores = Repository.find_all()
        for score in scores:
            result = ""
            if score[2] == 1:
                result = "1 - 0"
            elif score[2] == 2:
                result = "0 - 1"
            else:
                result = "1/2 - 1/2"
            game = f'{score[0]} {result} {score[1]}'
            label = ttk.Label(master=self._frame, text=game, font="italic 13 bold")
            label.grid(pady=10)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=550)
    
    def start_up(self):
        self._root.mainloop()
