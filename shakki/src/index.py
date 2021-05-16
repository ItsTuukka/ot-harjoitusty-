from tkinter import Tk
from ui.ui import UI
from main import main

window = Tk()
window.title("Chess")

ui = UI(window, main)
ui.start()

if __name__ == "__main__":
    window.mainloop()
