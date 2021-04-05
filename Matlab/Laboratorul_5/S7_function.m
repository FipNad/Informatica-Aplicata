function [v1,v2,M] = S7_function()
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here

m = 100;
phi = 0:(2*pi)/m:2*pi;
phi = phi(1:end-1);
v1 = cos(phi);
v2 = sin(phi);

M = zeros(m,50);
for i =1:m
    M(i,:) = linspace(v1(i),v2(i),50);
end

end

