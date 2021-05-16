from tkinter import ttk, constants


class EndScreen:

    """Class for the end screen.

    Attributes:
        root: Root for tkinter.
        handle_start: Function for starting the menu.
        result: Result of the game.
        frame: Initializing the frame object.
    """

    def __init__(self, root, handle_start, result):
        """Constructor for the class, calls the function
        to initialize the screen. 

        Args:
            root: Root for tkinter.
            handle_start: Function for starting the menu.
            result: Result of the game.
        """

        self._root = root
        self.handle_start = handle_start
        self._result = result
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
        head_label = ttk.Label(
            master=self._frame, text=self._result, font="none 20 bold")
        start_button = ttk.Button(
            master=self._frame,
            text="Back to main menu",
            command=self.handle_start
        )

        head_label.grid(pady=10)
        start_button.grid(pady=10)

        self._frame.grid_columnconfigure(0, weight=1, minsize=550)
