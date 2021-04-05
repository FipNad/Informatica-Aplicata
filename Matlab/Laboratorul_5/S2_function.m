function [M_out] = S2_function(M_in)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

M_out = zeros(4,3);

[nr_lin,nr_col]=size(M_in);
M1 = M_in(1:3,1:3);
M_out(1,:) = diag(rot90(M1));
M2 = M_in(1:3,nr_col-2:nr_col);
M_out(2,:) = diag(M2);
M3 = M_in(nr_lin-2:nr_lin,1:3);
M_out(3,:) = diag(M3);
M4= M_in(nr_lin-2:nr_lin,nr_col-2:nr_col);
M_out(4,:) = diag(rot90(M4));

close(1)


end

