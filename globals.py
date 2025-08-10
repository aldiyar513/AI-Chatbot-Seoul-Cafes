"""
Global, thread‑safe “mailbox” + constants shared by GUI and Prolog thread.
"""

from __future__ import annotations
import threading
from typing import Dict, List

#: single condition object used everywhere
COND = threading.Condition()

#: mutable dict that both threads read/write
SHARED_STATE: Dict[str, object | None] = dict(
    prompt=None,       # current question from Prolog (string)
    answer=None,       # user answer returned to Prolog (string/int)
    vibe=None,         # chosen vibe → lets PrologEngine assert facts
    final_result=None  # final text to show once Prolog is done
)

#: What each “vibe” contributes to the KB (plain Prolog terms as strings)
VIBES: Dict[str, List[str]] = {
    "Classes": [
        "known(no, music,   yes)",   # “Music = N”
        "known(yes, wifi,    yes)",   # “Wi‑Fi = Y”
    ],
    "Grind": [
        "known(yes, max_price, 5000)",   # user’s max price
        "known(no,  user_closes, early)" # closes **late**, so answer “No” to ‘closes early?’
    ],
    "Chill": [
        "known(yes, music, yes)",        # “Music = Y”
        # no outdoors restriction: leave it unasserted
    ],
    "Friends": [
        "known(yes, user_seating_booth, booth)",  # want booth seats
        "known(yes, user_seating_stool, stool)",  # want tables/stools
    ],
    "Nothing Specific":[

    ]
}

attribute_to_question = {
    'user_opens': 'Do you prefer places that open early (before 9:00 AM)?',
    'user_closes': 'Do you prefer places that close early (before 9:00 PM)?',
    'user_seating_stool': 'Do you prefer stool seating?',
    'user_seating_booth': 'Do you prefer booth seating?',
    'user_seating_sofa': 'Do you prefer sofa seating?',
    'music': 'Do you want music?',
    'wifi': 'Do you need WiFi?',
    'outdoors': 'Do you prefer outdoor seating?',
    'pet_friendly': 'Do you need a pet-friendly place?',
    'min_price': "What is your minimum price (in KRW)? ",
    'max_price': "What is your maximum price (in KRW)? ",
    'min_distance': 'What is your minimum acceptable distance (in meters)?',
    'max_distance': 'What is your maximum acceptable distance (in meters)?',
}


