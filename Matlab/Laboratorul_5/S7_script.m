clear
[~,~,M] = S7_function();

figure(1)
for i =2:2:50
    hold on
    subplot(2,1,1)
    plot(M(i,:))
    title('liniile pare')
end
hold off

for i =1:2:50
    hold on
    subplot(2,1,2)
    plot(M(i,:))
    title('liniile impare')
end
hold off
