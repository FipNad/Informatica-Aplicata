clear
nr_col = randi(10);
nr_lin = randi(10);

while (nr_col<5 || nr_lin<5)
    nr_col = randi(10);
    nr_lin = randi(10);
end


M = randi(10,nr_lin,nr_col);
M_out = S2_function(M);

figure(1)
subplot(4,2,[1 7])
plot(M_out)

subplot(4,2,2)
plot(M_out(1,:))

subplot(4,2,4)
plot(M_out(2,:))

subplot(4,2,6)
plot(M_out(3,:))

subplot(4,2,8)
plot(M_out(4,:))