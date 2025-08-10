"""
Entry‑point: create PrologEngine (must be main thread for SWI), start a
worker that runs the query, then launch the Tk GUI.
"""

import threading
import tkinter as tk

from engine import PrologEngine
from globals import SHARED_STATE, COND
from UI import ChatBotGUI


def main() -> None:
    # 1. initialise Prolog (+ foreign predicates)
    engine = PrologEngine("kb.pl")

    # 2. run the query in a separate thread
    threading.Thread(target=engine.solve_problem, daemon=True).start()

    # 3. start the GUI (still on the main thread)
    root = tk.Tk()
    ChatBotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
