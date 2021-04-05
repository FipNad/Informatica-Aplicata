clear
nr = 100;
num = 1:100;
v1 = cumsum(num);
v2 = cumprod(num);

v = v1./v2;

figure(1)
plot(v)
hold on
stem(v,"g")
stairs(v,"r-*")
hold off


