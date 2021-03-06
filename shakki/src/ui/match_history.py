from tkinter import Tk, ttk, constants
from repositories.match_history_repository import MatchHistoryRepository
Repository = MatchHistoryRepository()


class MatchHistory:

    """Class for the match history screen.
    """

    def __init__(self):
        """Constructor for the class, calls the function
        to initialize the screen.
        """

        self._root = Tk()
        self._root.title("Match History")
        self._frame = None

        self.initialize()

    def pack(self):
        """For showing the screen.
        """

        self._frame.pack(fill=constants.X)

    def initialize(self):
        """Initializes all the objects to be shown.
        """

        self._frame = ttk.Frame(master=self._root)
        scores = Repository.find_all()
        for i in range(len(scores)-1, -1, -1):
            result = ""
            if scores[i][2] == 1:
                result = "1 - 0"
            elif scores[i][2] == 3:
                result = "0 - 1"
            else:
                result = "1/2 - 1/2"
            game = f'(W) {scores[i][0]} {result} {scores[i][1]} (B)'
            label = ttk.Label(master=self._frame, text=game,
                              font="italic 13 bold")
            label.grid(pady=10)

        self._frame.grid_columnconfigure(0, weight=1, minsize=550)

    def start_up(self):
        """Starts to main loop for tkinter.
        """

        self._root.mainloop()
