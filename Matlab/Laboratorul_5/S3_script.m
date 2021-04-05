clear;
nr_lin = 3;
nr_col = 4;

M = randn(nr_lin,nr_col);
M = floor(abs(M));

figure(1)
surf(M)
colormap([0,1,0;1,0,0])
colorbar
view(90,0)
xlabel("x")
ylabel("y")
zlabel("z")
