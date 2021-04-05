function [X] = aplica_mod_3(X)
% function aplica_mod = aplica_mod(X);
%   Modifică elementele din vectorul X, aplicand modulo 3 pentru fiecare
%   
%   Variabilă de intrare: X - vector conținând numere
%   Variabilă de ieșire: X - vector cu valorile modificate
%
%funcție creată de Filip-Ioan Ceară (filip.ceara@mta.ro)


%% Verificarea datelor de intrare
if ~isnumeric(X)
    error("Variabila de intrare trebuie să fie de tip numeric")
end
if sum(size(X)==1)~=1
    error("Variabila de intrare trebuie să fie vector.")
end

%% Rezolvarea cerintei
X = mod(X,4);
X(4:6) = X(4:6) + 1;

