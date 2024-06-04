tech(backend, 'Python').
tech(backend, 'Java').
tech(backend, 'Node.js').
tech(frontend, 'JavaScript').
tech(frontend, 'React').
tech(frontend, 'Angular').
tech(mobile, 'Flutter').
tech(mobile, 'React Native').
tech(mobile, 'Swift').
tech(data_science, 'Python').
tech(data_science, 'R').
tech(data_science, 'Julia').

recommend(Preference, Tech) :-
    tech(Preference, Tech).
