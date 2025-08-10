# Café‑Finder ChatBot  
A tiny **Tkinter + SWI‑Prolog** desktop app that asks you a few
preferences (vibe, Wi‑Fi, distance, price, …) and recommends the best
study café from the built‑in knowledge‑base.

---

## Folder layout

```
.
├── kb.pl            Prolog knowledge‑base (cafés & rules)
├── engine.py        Python wrapper around SWI‑Prolog
├── UI.py            Tkinter front‑end (chat‑style)
├── globals.py       Shared condition‑variable + constants
├── main.py          Entry‑point (wires everything together)
└── README.md        <— you are here
```

---

## Quick start

1. **Install prerequisites**

```bash
# SWI‑Prolog (Linux: apt, Mac: brew, Windows: installer)
sudo apt install swi-prolog           # example for Debian/Ubuntu

# Python deps
pip install pyswip ttkbootstrap       # ttkbootstrap pulls modern ttk styles
```

Tkinter ships with every standard CPython build.

2. **Run**

```bash
python main.py
```

A chat window pops up.  
Pick a **vibe** (Classes / Grind / Chill / Friends), answer the follow‑up
questions, and the bot prints its café recommendation.

---

## How it works (high‑level)

| Layer | File(s) | Responsibility |
|-------|---------|----------------|
| **GUI** | `UI.py` | Draw chat window, ask questions (Yes/No, slider, text), animate bot messages. |
| **Sync bridge** | `globals.py` | One `threading.Condition` (`COND`) and a `SHARED_STATE` dict act as a mailbox between threads. |
| **Logic** | `engine.py`, `kb.pl` | `engine.py` hosts a SWI‑Prolog instance, registers `read_py/3`<br>as a foreign predicate, waits for answers, then queries `studyspot/1`. |
| **Bootstrap** | `main.py` | Creates `PrologEngine`, starts its worker thread, launches Tk mainloop. |

The Prolog thread blocks inside `read_py/3` waiting for the GUI to place
`answer` into `SHARED_STATE`.  Communication is fully thread‑safe thanks
to the shared `COND`.

---

## Customising

### 1. Add / edit cafés  
Open **`kb.pl`**, scroll to the bottom where each café is declared:

```prolog
% Café‑Name
distance(studyspot(mynewcafe), 850).
price(studyspot(mynewcafe),    5000).
opens(studyspot(mynewcafe),    0830).
closes(studyspot(mynewcafe),   2200).
seat_types(studyspot(mynewcafe), stool).
```

### 2. Change vibe presets  
In **`globals.py`** tweak the `VIBES` dict.  
Each entry is a list of `known/3` facts that get asserted up‑front when
that vibe is chosen.

```python
VIBES["Grind"] = [
    "known(yes, max_price, 4500)",
    "known(no,  user_closes, early)",
]
```

### 3. Rephrase questions  
Edit `attribute_to_question` in **`globals.py`** to change prompt
wording without touching Prolog or Python logic.

---

## Known limitations

* Single recommendation only (`maxresult=1`).
* Slider range is hard‑coded 0 – 9 999.
* No persistence; every run starts a fresh Prolog session.

Contributions are welcome—open a PR! 🎉