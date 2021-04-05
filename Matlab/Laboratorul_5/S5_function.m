function [M_out] = S5_function(M)
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here

figure(1)
sgtitle('Matricea M')

subplot(7,3, [1,4])
plot(M(1,:))
title('linia 1')

subplot(7,3, [2,5])
plot(M(2,:))
title('linia 2')

subplot(7,3, [3,6])
plot(M(3,:))
title('linia 3')

subplot(7,3, [7,10])
plot(M(4,:))
title('linia 4')

subplot(7,3, [8,11])
plot(M(5,:))
title('linia 5')

subplot(7,3, [9,12])
plot(M(6,:))
title('linia 6')

subplot(7,3,13)
plot(M(7,:))
title('linia 7')

subplot(7,3,16)
plot(M(8,:))
title('linia 8')

subplot(7,3,19)
plot(M(9,:))
title('linia 9')

subplot(7,3,15)
plot(M(10,:))
title('linia 10')

subplot(7,3,18)
plot(M(11,:))
title('linia 11')

subplot(7,3,21)
plot(M(12,:))
title('linia 12')

subplot(7,3,[14,20])
plot(M(13,:))
title('linia 13')

M_out = [7,3,1,4;
        7,3,2,5;
        7,3,3,6;
        7,3,7,10;
        7,3,8,11;
        7,3,9,12;
        7,3,13,13;
        7,7,16,16;
        7,3,19,19;
        7,3,15,15;
        7,3,18,18;
        7,3,21,21;
        7,3,14,20];
end

