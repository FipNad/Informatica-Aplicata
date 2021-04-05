% Acest script are rolul de sorta valorile unui vector și de a afișa
% valoarea medianului acestuia.
% Script realizat de Alexandru Frunza (alexandru.frunza@mta.ro)

%% Ștergerea variabilelor din Workspace
clear;

%% Generarea unui vector coloană cu valori aleator generate
N = input("Introduceți un număr întreg care să reprezinte numărul de valori conținute în vector: ");
vec = randn(N,1)

%% Sortarea vectorului
vec_sort = sort(vec)

%% Găsirea indicelui medianului
index = round(N/2);

%% Afișarea valorii medianului
disp( vec_sort(index) );