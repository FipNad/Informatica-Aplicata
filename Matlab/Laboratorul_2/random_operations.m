function [random_matrix,random_number] = random_operations(nr_lin,nr_col)
% function [random_matrix,random_number]= random_operations(nr_lin,nr_col)
%   Returnează o matrice de (nr_lin)x(nr_col) ce conține numere generate prin
%    funcția randn înmulțită cu un număar generat aleator (prin random). Se
%    va returna și acel număr.
%   
%   Variabile de intrare:  
%       * nr_lin = numărul de linii din matrice
%       * nr_col = numărul de coloane din matrice
%   Variabile de ieșire:
%       * random_matrix = matricea generata random inmulțită cu un număar
%       generat aleator
%       * random_number = număr generat aleator
% 
%
%funcție creată de Filip-Ioan Ceară (filip.ceara@mta.ro)

%% Verificarea dimensiunilor matricei
if(~isnumeric(nr_lin) || ~isnumeric(nr_col))
    error("Dimensiunile trebuie să fie de tip numeric")
end
if(nr_lin <=0 || nr_col <= 0)
    error("Dimensiunile trebuie să fie numere pozitive")
end
if(isinf(nr_lin) || isinf(nr_col) || isnan(nr_lin) || isnan(nr_col))
    error("Dimensiunile trebuie să fie numere valide")
end
if(floor(nr_lin) ~= nr_lin || floor(nr_col) ~= nr_col)
    error("Dimensiunile trebuie să fie numere întregi")
end

%% Rezolvarea efectivă

random_matrix = randn(nr_lin,nr_col);
random_number = rand;
random_matrix = random_matrix*random_number;
end

