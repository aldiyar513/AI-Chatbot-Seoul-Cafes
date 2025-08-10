"""
Tk‑based front‑end.  Presents:
  1) a one‑time “choose your vibe” menu
  2) follow‑up questions from Prolog (yes/no, slider, or free‑text)
"""

from __future__ import annotations
import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import Optional

from globals import *


class ChatBotGUI:
    BG = "#FAFAFA"
    BOT_BG = "#E3F2FD"
    USR_BG = "#C8E6C9"
    FONT = ("Segoe UI", 11)
    POLL_MS = 500

    def __init__(self, root: tk.Tk) -> None:
        self._root = root
        self._last_prompt: Optional[str] = None

        self._build_layout()
        self._msg("Hey! Let’s hook you up with a study place. \nWhat vibe are you looking for?")
        self._ask_vibe()
        self._poll_loop()

    def _build_layout(self) -> None:
        root = self._root
        root.title("Café Finder")
        root.geometry("650x650")
        root.configure(bg=self.BG)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # chat log
        self._log = scrolledtext.ScrolledText(
            root, state="disabled", wrap="word", relief="flat",
            font=self.FONT, bg="white", padx=6, pady=6
        )
        self._log.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
        self._log.tag_config("bot",  background=self.BOT_BG,
                             lmargin1=8, lmargin2=8, spacing3=6)
        self._log.tag_config("user", background=self.USR_BG,
                             justify="right", rmargin=8, spacing3=6)
        self._log.tag_config("name", foreground="#424242",
                             font=("Segoe UI", 9, "bold"))

        # input frame
        self._input = ttk.Frame(root, padding=10)
        self._input.grid(row=1, column=0, sticky="ew")

        style = ttk.Style(root)
        style.configure("TButton", font=self.FONT, padding=6)
        style.configure("TRadiobutton", font=self.FONT)
        style.configure("Horizontal.TScale", troughcolor="#EEE")

    # ------------------------------------------------ chat helpers --
    def _msg(self, txt: str, sender: str = "Bot") -> None:
        """
        Public wrapper: for Bot messages we stream characters gradually;
        for user messages we post the full line immediately.
        """
        if sender == "Bot":
            self._stream(txt, tag="bot")
        else:
            self._post_msg(txt, tag="user")

    # ----------------------------------------------------------------
    def _stream(self, txt: str, tag: str, idx: int = 0) -> None:
        """Type‑writer effect: post 1 char, then schedule the next."""
        if idx == 0:                                 # first call → write name
            self._log.config(state="normal")
            self._log.insert(tk.END, f"Bot: ", ("name", tag))
            self._log.config(state="disabled")

        if idx < len(txt):
            self._log.config(state="normal")
            self._log.insert(tk.END, txt[idx], tag)
            self._log.config(state="disabled")
            self._log.yview(tk.END)
            self._root.after(2, self._stream, txt, tag, idx + 1)  # speed (ms)
        else:                                          # finished line
            self._log.config(state="normal")
            self._log.insert(tk.END, "\n", tag)
            self._log.config(state="disabled")
            self._log.yview(tk.END)

    # ----------------------------------------------------------------
    def _post_msg(self, txt: str, tag: str) -> None:
        """Immediate one‑shot insert (used by user or helper calls)."""
        self._log.config(state="normal")
        if tag in ("bot", "user"):                    # second arg is style tag
            sender = "Bot" if tag == "bot" else "You"
            self._log.insert(tk.END, f"{sender}: ", ("name", tag))
        self._log.insert(tk.END, f"{txt}\n", tag)
        self._log.config(state="disabled")
        self._log.yview(tk.END)

    # ----------------------------------------------------------------
    def _clear_input(self) -> None:
        for w in self._input.winfo_children():
            w.destroy()

    # ------------------------------------------------------- vibe chooser
    def _ask_vibe(self, ) -> None:
        wrap = ttk.Frame(self._input)
        wrap.grid(row=0, column=0, sticky="ew", pady=6)
        wrap.columnconfigure(tuple(range(len(VIBES))), weight=1)  # every col = 1

        for col, vibe in enumerate(VIBES):
            ttk.Button(
                wrap,
                text=vibe,
                command=lambda v=vibe: self._choose_vibe(v),
                style="Accent.TButton"
            ).grid(row=0, column=col, padx=4, sticky="ew")

    def _choose_vibe(self, vibe: str) -> None:
        with COND:
            SHARED_STATE["vibe"] = vibe
            COND.notify_all()
        self._msg(vibe, sender="You")
        self._clear_input()

    # ------------------------------------------------------- poll / render
    def _poll_loop(self) -> None:
        with COND:
            prompt = SHARED_STATE.get("prompt")

            # new Prolog question?
            if prompt and prompt != self._last_prompt:
                self._show_question(prompt)
                self._last_prompt = prompt

            # final answer?
            if (ans := SHARED_STATE.get("final_result")) and not hasattr(self, "_done"):
                self._msg(ans)
                self._done = True

        self._root.after(self.POLL_MS, self._poll_loop)

    # ------------------------------------------------------- question types
    def _show_question(self, text: str) -> None:
        self._clear_input()
        self._msg(text)

        t = text.lower()
        if any(word in t for word in ("distance", "price")):
            self._slider()
        else:
            self._yes_no()


    # ------------------------------------------------------- yes / no
    def _yes_no(self) -> None:
        """Two radio buttons (Yes / No) centered in a mini‑frame."""
        self._clear_input()                      # wipe previous widgets

        # Make the single column of _input expand, so its children can centre.
        self._input.columnconfigure(0, weight=1)

        # Inner frame that itself expands to fill available space
        wrap = ttk.Frame(self._input)
        wrap.grid(row=0, column=0, pady=6, sticky="n")
        wrap.columnconfigure((0, 1), weight=1)   # two equal columns for radios

        self._choice = tk.StringVar(value="yes")

        ttk.Radiobutton(
            wrap, text="Yes", variable=self._choice, value="Yes",
            style="Option.TRadiobutton"
        ).grid(row=0, column=0, padx=12, pady=(0, 4), sticky="e")

        ttk.Radiobutton(
            wrap, text="No", variable=self._choice, value="No",
            style="Option.TRadiobutton"
        ).grid(row=0, column=1, padx=12, pady=(0, 4), sticky="w")

        ttk.Button(
            wrap, text="Submit", command=self._submit, style="Accent.TButton"
        ).grid(row=1, column=0, columnspan=2, pady=8)


    # ------------------------------------------------------- slider
    def _slider(self) -> None:
        """Full‑width slider with live value badge; value stored in self._choice."""

        self._clear_input()

        # Make the single column of the input frame expand
        self._input.columnconfigure(0, weight=1)

        # Wrapper frame
        wrap = ttk.Frame(self._input)
        wrap.grid(row=0, column=0, sticky="ew", pady=6)
        wrap.columnconfigure(1, weight=1)        # slider column stretches

        # Live badge
        self._value_lbl = ttk.Label(wrap, text="0", style="Value.TLabel")
        self._value_lbl.grid(row=0, column=0, columnspan=3, pady=(0, 4))

        # Tk variable that both slider and submit will read
        self._choice = tk.DoubleVar(value=0)

        # Row with min label – slider – max label
        ttk.Label(wrap, text="0").grid(row=1, column=0, sticky="w", padx=(0, 6))

        self._range = ttk.Scale(
            wrap,
            from_=0, to=9999,
            orient="horizontal",
            variable=self._choice,       # ← bind variable
            command=self._on_slide       # keep badge updating
        )
        self._range.grid(row=1, column=1, sticky="ew")

        ttk.Label(wrap, text="9 999").grid(row=1, column=2, sticky="e", padx=(6, 0))

        ttk.Button(
            wrap, text="Confirm", command=self._submit, style="Accent.TButton"
        ).grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")

        # Inject badge style once
        if not hasattr(self, "_value_style_injected"):
            style = ttk.Style(self._root)
            style.configure("Value.TLabel", font=("Segoe UI", 12, "bold"),
                            foreground="#0078D4")
            self._value_style_injected = True


    def _on_slide(self, val: str) -> None:
        """Update badge; variable is already synced via self._choice."""
        self._value_lbl.configure(text=str(int(float(val))))


    def _submit(self) -> None:
        answer = self._choice.get()
        self._msg(str(answer), sender="You")
        self._clear_input()

        with COND:
            SHARED_STATE["answer"] = answer
            COND.notify_all()
