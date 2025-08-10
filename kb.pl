%  Tell prolog that known/3 and multivalued/1 will be added later
:- dynamic known/3, multivalued/1.


studyspot(cafeoreumyaksu) :-
    qualifies_distance(cafeoreumyaksu),
    qualifies_price(cafeoreumyaksu),
    qualifies_opens(yes_early),
    qualifies_closes(yes_late),
    music(yes),
    wifi(yes),
    \+outdoors(yes),
    pet_friendly(yes),
    qualifies_seating(stool).

studyspot(susannasapron) :-
    qualifies_distance(susannasapron),
    qualifies_price(susannasapron),
    qualifies_opens(yes_early),
    qualifies_closes(yes_late),
    music(yes),
    wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes),
    qualifies_seating(stool),
    qualifies_seating(booth).

studyspot(dotorigardenanguk):-
    qualifies_distance(dotorigardenanguk),
    qualifies_price(dotorigardenanguk),
    qualifies_opens(yes_early),
    qualifies_closes(yes_late),
    music(yes),
    wifi(yes),
    outdoors(yes),
    pet_friendly(yes),
    qualifies_seating(stool),
    qualifies_seating(sofa).

studyspot(langstudycafesinchon) :-
    qualifies_distance(langstudycafesinchon),
    qualifies_price(langstudycafesinchon),
    qualifies_opens(yes_early),
    qualifies_closes(yes_late),
    \+music(yes),
    wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes),
    qualifies_seating(stool),
    qualifies_seating(booth).

studyspot(cafedefessonia) :-
    qualifies_distance(cafedefessonia),
    qualifies_price(cafedefessonia),
    qualifies_opens(yes_late),
    qualifies_closes(yes_late),
    \+music(yes),
    wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes),
    qualifies_seating(stool).

studyspot(cafewildduck) :-
    qualifies_distance(cafewildduck),
    qualifies_price(cafewildduck),
    qualifies_opens(yes_late),
    qualifies_closes(yes_early),
    music(yes),
    wifi(yes),
    outdoors(yes),
    pet_friendly(yes),
    qualifies_seating(stool).

studyspot(cafegabiae) :-
    qualifies_distance(cafegabiae),
    qualifies_price(cafegabiae),
    qualifies_opens(yes_early),
    qualifies_closes(yes_late),
    music(yes),
    wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes),
    qualifies_seating(stool).

studyspot(conhas) :-
    qualifies_distance(conhas),
    qualifies_price(conhas),
    qualifies_opens(yes_late),
    qualifies_closes(yes_late),
    music(yes),
    wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes),
    qualifies_seating(stool),
    qualifies_seating(sofa).

studyspot(cafedelyonjangchung) :-
    qualifies_distance(cafedelyonjangchung),
    qualifies_price(cafedelyonjangchung),
    qualifies_opens(yes_late),
    qualifies_closes(yes_late),
    music(yes),
    wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes),
    qualifies_seating(stool).

studyspot(hauscoffeeanddessert) :-
    qualifies_distance(hauscoffeeanddessert),
    qualifies_price(hauscoffeeanddessert),
    qualifies_opens(yes_early),
    qualifies_closes(yes_late),
    \+music(yes),
    wifi(yes),
    outdoors(yes),
    pet_friendly(yes),
    qualifies_seating(stool).

studyspot(anthracitehapjung) :-
    qualifies_distance(anthracitehapjung),
    qualifies_price(anthracitehapjung),
    qualifies_opens(yes_late),
    qualifies_closes(yes_late),
    music(yes),
    wifi(yes),
    \+outdoors(yes),
    pet_friendly(yes),
    qualifies_seating(stool),
    qualifies_seating(sofa).

studyspot(sorrynotsorry) :-
    qualifies_distance(sorrynotsorry),
    qualifies_price(sorrynotsorry),
    qualifies_opens(yes_late),
    qualifies_closes(yes_early),
    \+music(yes),
    wifi(yes),
    outdoors(yes),
    \+pet_friendly(yes),
    qualifies_seating(booth),
    qualifies_seating(sofa).

studyspot(sindangmailroom) :-
    qualifies_distance(sindangmailroom),
    qualifies_price(sindangmailroom),
    qualifies_opens(yes_late),
    qualifies_closes(yes_late),
    music(yes),
    wifi(yes),
    \+outdoors(yes),
    pet_friendly(yes).

studyspot(gomango) :-
    qualifies_distance(gomango),
    qualifies_price(gomango),
    qualifies_opens(yes_late),
    qualifies_closes(yes_late),
    music(yes),
    \+wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes).

studyspot(andarcoffee) :-
    qualifies_distance(andarcoffee),
    qualifies_price(andarcoffee),
    qualifies_opens(yes_late),
    qualifies_closes(yes_late),
    \+music(yes),
    wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes),
    qualifies_seating(stool).

studyspot(cafedof) :-
    qualifies_distance(cafedof),
    qualifies_price(cafedof),
    qualifies_opens(yes_late),
    qualifies_closes(yes_early),
    music(yes),
    wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes).

studyspot(cafeann) :-
    qualifies_distance(cafeann),
    qualifies_price(cafeann),
    qualifies_opens(yes_early),
    qualifies_closes(yes_late),
    music(yes),
    \+wifi(yes),
    \+outdoors(yes),
    \+pet_friendly(yes).

studyspot(undebt) :-
    qualifies_distance(undebt),
    qualifies_price(undebt),
    qualifies_opens(yes_late),
    qualifies_closes(yes_early),
    music(yes),
    \+wifi(yes),
    outdoors(yes),
    pet_friendly(yes),
    qualifies_seating(stool).

studyspot(coffee) :-
    qualifies_distance(coffee),
    qualifies_price(coffee),
    qualifies_opens(yes_late),
    qualifies_closes(yes_early),
    music(yes),
    \+wifi(yes),
    outdoors(yes),
    pet_friendly(yes),
    qualifies_seating(stool).

% Rules for qualifying cafes based on user preferences
% Rules for opening and closing times
qualifies_opens(yes_early):- user_opens(early).
qualifies_opens(yes_late):- \+user_opens(early).

qualifies_closes(yes_early):- user_closes(early).
qualifies_closes(yes_late):- \+user_closes(early).

% Rules for seating preferences
qualifies_seating(stool):- seat_types(studyspot(_), stool), user_seating_stool(stool).
qualifies_seating(booth):- seat_types(studyspot(_), booth), user_seating_booth(booth).
qualifies_seating(sofa):- seat_types(studyspot(_), sofa), user_seating_sofa(sofa).

% Price qualification now works with min_price and max_price
qualifies_price(Cafe) :-
    price(studyspot(Cafe), P),
    get_min_price(Min),
    get_max_price(Max),
    P >= Min,
    P =< Max.

% Distance qualification now works with min_distance and max_distance
qualifies_distance(Cafe) :-
    distance(studyspot(Cafe), D),
    get_min_distance(Min),
    get_max_distance(Max),
    D >= Min,
    D =< Max.

% Helper predicates to get price/distance values with appropriate defaults if not specified
get_min_price(Min) :-
    (   min_price(Min)            % will call ask/3 → GUI the first time
    ->  true
    ;   Min = 0                   % default KRW 0
    ).

get_max_price(Max) :-
    (   max_price(Max)
    ->  true
    ;   Max = 10000               % default ceiling
    ).

get_min_distance(Min) :-
    (   min_distance(Min)
    ->  true
    ;   Min = 0                   % meters
    ).

get_max_distance(Max) :-
    (   max_distance(Max)
    ->  true
    ;   Max = 10000               % meters
    ).

% Dynamic distance classification
distance(short):- distance(studyspot(_), D), D =< 1000.
distance(long):- distance(studyspot(_), D), D > 1000.

% Dynamic price classification
price(cheap):- price(studyspot(_), P), P =< 4780.

% Dynamic opening time classification
opens(early):- opens(studyspot(_), TE), TE < 0900.
opens(late):- opens(studyspot(_), TE), TE >= 0900.

% Dynamic closing time classification
closes(early):- closes(studyspot(_), TL), TL < 2100.
closes(late):- closes(studyspot(_), TL), TL >= 2100.

% Dynamic seat types classification
seat_types(stool):- seat_types(studyspot(_), stool).
seat_types(booth):- seat_types(studyspot(_), booth).
seat_types(sofa):- seat_types(studyspot(_), sofa).

% Cafe-Oreum Yaksu
distance(studyspot(cafeoreumyaksu), 1000).
price(studyspot(cafeoreumyaksu), 3800).
opens(studyspot(cafeoreumyaksu), 830).
closes(studyspot(cafeoreumyaksu), 2400).
seat_types(studyspot(cafeoreumyaksu), stool).

% SUSANNAS APRON
distance(studyspot(susannasapron), 900).
price(studyspot(susannasapron), 4500).
opens(studyspot(susannasapron), 0700).
closes(studyspot(susannasapron), 2200).
seat_types(studyspot(susannasapron), stool).
seat_types(studyspot(susannasapron), booth).

% Dotori Garden Anguk
distance(studyspot(dotorigardenanguk), 3100).
price(studyspot(dotorigardenanguk), 5500).
opens(studyspot(dotorigardenanguk), 0800).
closes(studyspot(dotorigardenanguk), 2300).
seat_types(studyspot(dotorigardenanguk), stool).
seat_types(studyspot(dotorigardenanguk), sofa).

% Langstudy Cafe Sinchon
distance(studyspot(langstudycafesinchon), 2000).
price(studyspot(langstudycafesinchon), 1800).
opens(studyspot(langstudycafesinchon), 1000).
closes(studyspot(langstudycafesinchon), 2400).
seat_types(studyspot(langstudycafesinchon), stool).
seat_types(studyspot(langstudycafesinchon), booth).

% Cafe De Fessonia
distance(studyspot(cafedefessonia), 300).
price(studyspot(cafedefessonia), 4000).
opens(studyspot(cafedefessonia), 0900).
closes(studyspot(cafedefessonia), 2300).
seat_types(studyspot(cafedefessonia), stool).

% Cafe Wild Duck
distance(studyspot(cafewildduck), 1400).
price(studyspot(cafewildduck), 4000).
opens(studyspot(cafewildduck), 1030).
closes(studyspot(cafewildduck), 1800).
seat_types(studyspot(cafewildduck), stool).

% Cafe Gabiae
distance(studyspot(cafegabiae), 7900).
price(studyspot(cafegabiae), 5000).
opens(studyspot(cafegabiae), 0000).
closes(studyspot(cafegabiae), 2400).
seat_types(studyspot(cafegabiae), stool).

% Cohnas
distance(studyspot(conhas), 220).
price(studyspot(conhas), 5500).
opens(studyspot(conhas), 1000).
closes(studyspot(conhas), 2300).
seat_types(studyspot(conhas), stool).
seat_types(studyspot(conhas), sofa).

% Cafe de Lyon Jangchung
distance(studyspot(cafedelyonjangchung), 570).
price(studyspot(cafedelyonjangchung), 5700).
opens(studyspot(cafedelyonjangchung), 0900).
closes(studyspot(cafedelyonjangchung), 2300).
seat_types(studyspot(cafedelyonjangchung), stool).

% Haus Coffee & Dessert
distance(studyspot(hauscoffeeanddessert), 1100).
price(studyspot(hauscoffeeanddessert), 5500).
opens(studyspot(hauscoffeeanddessert), 0800).
closes(studyspot(hauscoffeeanddessert), 2100).
seat_types(studyspot(hauscoffeeanddessert), stool).

% Anthracite Hapjung
distance(studyspot(anthracitehapjung), 9400).
price(studyspot(anthracitehapjung), 5500).
opens(studyspot(anthracitehapjung), 0900).
closes(studyspot(anthracitehapjung), 2400).
seat_types(studyspot(anthracitehapjung), stool).
seat_types(studyspot(anthracitehapjung), sofa).

% Sorry Not Sorry
distance(studyspot(sorrynotsorry), 100).
price(studyspot(sorrynotsorry), 5500).
opens(studyspot(sorrynotsorry), 0900).
closes(studyspot(sorrynotsorry), 1700).
seat_types(studyspot(sorrynotsorry), booth).
seat_types(studyspot(sorrynotsorry), sofa).

% Sindang Mailroom
distance(studyspot(sindangmailroom), 970).
price(studyspot(sindangmailroom), 6500).
opens(studyspot(sindangmailroom), 1200).
closes(studyspot(sindangmailroom), 2400).

% GoMango
distance(studyspot(gomango), 1000).
price(studyspot(gomango), 2000).
opens(studyspot(gomango), 1000).
closes(studyspot(gomango), 2100).

% Andar Coffee
distance(studyspot(andarcoffee), 250).
price(studyspot(andarcoffee), 2000).
opens(studyspot(andarcoffee), 1000).
closes(studyspot(andarcoffee), 2330).
seat_types(studyspot(andarcoffee), stool).

% Cafe dof
distance(studyspot(cafedof), 780).
price(studyspot(cafedof), 4800).
opens(studyspot(cafedof), 1000).
closes(studyspot(cafedof), 1900).

% Cafe Ann
distance(studyspot(cafeann), 7000).
price(studyspot(cafeann), 4900).
opens(studyspot(cafeann), 0000).
closes(studyspot(cafeann), 2400).

% Undebt
distance(studyspot(undebt), 4500).
price(studyspot(undebt), 5000).
opens(studyspot(undebt), 1100).
closes(studyspot(undebt), 1930).
seat_types(studyspot(undebt), stool).

% Coffee
distance(studyspot(coffee), 4500).
price(studyspot(coffee), 5000).
opens(studyspot(coffee), 1100).
closes(studyspot(coffee), 1930).
seat_types(studyspot(coffee), stool).

% The code below implements the prompting to ask the user:
user_opens(X) :- ask(user_opens, X).
user_closes(X) :- ask(user_closes, X).
user_seating_stool(X) :- ask(user_seating_stool, X).
user_seating_booth(X) :- ask(user_seating_booth, X).
user_seating_sofa(X) :- ask(user_seating_sofa, X).
min_price(X) :- ask(min_price, X).
max_price(X) :- ask(max_price, X).
min_distance(X) :- ask(min_distance, X).
max_distance(X) :- ask(max_distance, X).

music(X) :- ask(music, X).
wifi(X) :- ask(wifi, X).
outdoors(X):- ask(outdoors, X).
pet_friendly(X) :- ask(pet_friendly, X).

% Asking clauses
ask(A, V):-
    known(yes, A, V), % succeed if true
    !.	% stop looking

ask(A, V):-
    known(_, A, V), % fail if false
    !, fail.

% If not multivalued, and already known to be something else, dont ask again for a different value.
ask(A, V):-
    \+multivalued(A),
    known(yes, A, V2),
    V \== V2,
    !, fail.

ask(A, V):-
    read_py(A, V, Y), % get the answer
    assertz(known(Y, A, V)), % remember it
    Y == yes.	% succeed or fail