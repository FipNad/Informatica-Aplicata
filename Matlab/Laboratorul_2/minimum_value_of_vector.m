function min_value = minimum_value_of_vector(X)
% function min_value = minimum_value_of_vector(X);
%   Returnează cea mai mică valoare din vectorul de intrare.
%   Folosește funcția de sortare din MatLab pentru această sarcină.
%   
%   Variabilă de intrare: X - vector conținând numere
%   Variabilă de ieșire: min_value - valoarea minimă
%
%funcție creată de Filip-Ioan Ceară (filip.ceara@mta.ro)

%% Verificarea datelor de intrare
if ~isnumeric(X)
    error("Variabila de intrare trebuie să fie de tip numeric")
end
if sum(size(X)==1)~=1
    error("Variabila de intrare trebuie să fie vector.")
end

%% Aflarea valorii minime
X = sort(X,'descend');
min_value = X(end);



