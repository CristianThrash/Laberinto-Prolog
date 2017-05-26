conecta(21,22).
conecta(22,23).
conecta(23,24).
conecta(24,25).
conecta(25,26).
conecta(26,27).
conecta(47,48).
conecta(48,49).
conecta(71,72).
conecta(72,73).
conecta(73,74).
conecta(74,75).
conecta(76,77).
conecta(74,84).
conecta(x,25).
conecta(27,37).
conecta(37,47).
conecta(47,57).
conecta(57,67).
conecta(67,77).
conecta(77,y).
conecta(19,29).
conecta(29,39).
conecta(39,49).

conectado(X,Y):-conecta(X,Y).
conectado(X,Y):-conecta(Y,X).

miembro(X,[X|_]).
miembro(X,[_|Y]):- miembro(X,Y).

tiene_solucion():-hay_camino([x],_).

hay_camino([y|L],[y|L]).
hay_camino([X|L],Y):-conectado(X,S),\+miembro(S,L),hay_camino([S,X|L],Y).
