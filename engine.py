"""
Thin wrapper around SWI‑Prolog (PySWIP) that:

1. Exposes read_py/3 as a foreign predicate (asks the GUI a question).
2. Waits for the GUI to supply a *vibe* and asserts the corresponding
   facts before running the main `studyspot/1` query.
"""

from __future__ import annotations
import threading
from typing import Dict
from pyswip import Prolog, Atom, Variable, registerForeign
from globals import *


class PrologEngine:
    """Owns one SWI‑Prolog instance and runs the café‑finder query."""

    def __init__(self, kb_file: str) -> None:
        self._prolog = Prolog()           # calls PL_initialise()
        self._register_foreign_predicates()
        self._prolog.consult(kb_file)
        list(self._prolog.query("retractall(known(_,_,_))."))

    # ────────────────────────────────────────────────────────────────────
    # Helpers
    # ────────────────────────────────────────────────────────────────────
    def _num_fact(self, functor: str, cafe: str, var: str = "V") -> int | None:
        """Return a single numeric fact such as distance/price/opens/closes."""
        q = f"{functor}(studyspot({cafe}), {var})."
        res = list(self._prolog.query(q))
        return int(res[0][var]) if res else None


    def _seat_types(self, cafe: str) -> list[str]:
        """Collect seat types (stool/booth/sofa) available at a cafe."""
        types = []
        for st in ("stool", "booth", "sofa"):
            if list(self._prolog.query(f"seat_types(studyspot({cafe}), {st}).")):
                types.append(st.capitalize())
        return types
    
    def _amenities(self, cafe: str) -> list[str]:
            has_wifi = len(list(self._prolog.query(f"wifi(yes), studyspot({cafe})."))) > 0
            has_music = len(list(self._prolog.query(f"music(yes), studyspot({cafe})."))) > 0
            is_pet_friendly = len(list(self._prolog.query(f"pet_friendly(yes), studyspot({cafe})."))) > 0
            has_outdoors = len(list(self._prolog.query(f"outdoors(yes), studyspot({cafe})."))) > 0

            amenities = []
            if has_wifi: amenities.append("WiFi")
            if has_music: amenities.append("Music")
            if is_pet_friendly: amenities.append("Pet Friendly")
            if has_outdoors: amenities.append("Outdoor Seating")

            return amenities

    def solve_problem(self) -> None:
        """Blocks until GUI chooses a vibe, then lists matching study spots
        with distance, price, hours and seating."""
        self._wait_and_assert_vibe()
        
        result = self._prolog.query("studyspot(X).")
        cafes = {d["X"] for d in result}
        if not cafes:
            msg = "Sorry, nothing matched your preferences."
        else:
            lines = ["Here are your matching study spots:"]
            for name in sorted(cafes):
                dist   = self._num_fact("distance", name)   # metres
                price  = self._num_fact("price",    name)   # KRW
                opens  = self._num_fact("opens",    name)   # HHMM ints
                closes = self._num_fact("closes",   name)
                seats  = ", ".join(self._seat_types(name)) or "—"
                amenities = self._amenities(name)

                hhmm = lambda t: f"{t:04d}"[:2] + ":" + f"{t:04d}"[2:]
                spot_info = [
                    f"\n• {name.capitalize()}",
                    f"    ├ Distance : {dist} m",
                    f"    ├ Price    : ₩{price:,}",
                    f"    ├ Hours    : {hhmm(opens)}–{hhmm(closes)}"
                ]

                if amenities:
                    spot_info.append(f"    ├ Amenities: {', '.join(amenities)}")

                spot_info.append(f"    └ Seating  : {seats}")
                lines.extend(spot_info)

            msg = "\n".join(lines)

        with COND:
            SHARED_STATE["final_result"] = msg
            COND.notify_all()

    # ------------------------------------------------------------------ helpers
    def _wait_and_assert_vibe(self) -> None:
        """Wait until GUI sets SHARED_STATE['vibe']; then assert facts."""
        with COND:
            if SHARED_STATE["vibe"] is None:
                COND.wait()

            vibe = str(SHARED_STATE["vibe"])
            for fact in VIBES.get(vibe, []):
                self._prolog.assertz(fact)

    # ---------------------------------------------------------------- foreign
    def _register_foreign_predicates(self) -> None:
        """Expose read_py/3 to Prolog so it can ask questions."""
        def read_py(attr, val, ReplyVar) -> bool:
            with COND:
                question = attribute_to_question.get(str(attr), f"{attr} is {val}")
                SHARED_STATE.update(
                    prompt=question,
                    answer=None,
                )
                COND.notify_all()

                if SHARED_STATE["answer"] is None:
                    COND.wait()

                if isinstance(ReplyVar, Variable):
                    ReplyVar.unify(Atom(str(SHARED_STATE["answer"]).lower()))
                return True

        read_py.arity = 3
        registerForeign(read_py)
