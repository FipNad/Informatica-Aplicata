clear
nr_lin = 13;
nr_col = 50;

M = 10+10*rand(nr_lin,nr_col);
k = 0;

 while(length(unique(M(:,nr_col))) - length(M(:,nr_col)) ~= 0 )
     M = 10+10*rand(nr_lin,nr_col);
 end


