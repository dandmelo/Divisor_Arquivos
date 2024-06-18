# main.py

import tkinter as tk
from view import View
from controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    view = View(root)
    controller = Controller(root, view)
    view.configurar_eventos(controller)
    root.mainloop()
