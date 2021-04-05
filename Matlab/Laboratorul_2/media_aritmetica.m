function [m] = media_aritmetica(x)
% function m = media_aritmetica(x);
%   Calculează media aritmetică a numerelor din cadrul vectorului de intrare.
%
%   Variabilă de intrare: x - vector conținând numere
%   Variabilă de ieșire: m - media aritmetică
%
% funcție scrisă de Alexandru Frunză (alexandru.frunza@mta.ro)

%% Verificarea datelor de intrare
if ~isnumeric(x)
error("Variabila de intrare trebuie să fie de tip numeric.")
end
if sum(size(x)==1)~=1
error("Variabila de intrare trebuie să fie vector.")
end
if length(x)<5
error("Variabila de intrare trebuie să conțină cel puțin 5 elemente.")
end
%% Calculul mediei aritmetice
m = sum(x)/length(x);

