%Acest script are rolul de a genera o matrice cu dimensiuni random ce
%conține numere întregi de la 0 la 10.
%Script creat de Filip-Ioan Ceară(filip.ceara@mta.ro)

%% Generarea dimensiunilor matricei în mod aleator
lin = randi(20);
col = randi(20);

%% Generarea matricei
mat = randi([0,10],lin,col);

%% Aflarea numarului de elemente ale matricei
[num_linii,num_coloane] = size(mat);
nr_of_elements = numel(mat);
if(num_linii*num_coloane == nr_of_elements)
    disp(["Este bine. Matricea are " + nr_of_elements + " elemente."]);
end
