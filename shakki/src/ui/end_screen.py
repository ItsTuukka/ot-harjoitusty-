from tkinter import ttk, constants

class EndScreen:
    def __init__(self, root, handle_start, result):
        self._root = root
        self.handle_start = handle_start
        self._result = result
        self._frame = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        head_label = ttk.Label(master=self._frame, text=self._result, font="none 20 bold")
        start_button = ttk.Button(
            master=self._frame,
            text="Back to main menu",
            command=self.handle_start
            )

        head_label.grid(pady=10)
        start_button.grid(pady=10)

        self._frame.grid_columnconfigure(0, weight=1, minsize=550)
