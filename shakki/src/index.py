from tkinter import Tk
from ui.ui import UI
from main import run

window = Tk()
window.title("Chess")

ui = UI(window, run)
ui.start()

if __name__ == "__main__":
    window.mainloop()