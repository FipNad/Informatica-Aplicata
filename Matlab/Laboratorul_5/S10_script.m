clear
M = S10_function();
[nr_lin,nr_col] = size(M);

j = 1;
figure(1)
for i=1:nr_lin
    subplot(1,4,j)
    if(j == 1)
        hold on
        plot(M(i,:))
    elseif(j == 2)
        hold on
        stem(M(i,:))
    elseif(j == 3)
        hold on
        stairs(M(i,:))
    elseif(j == 4)
        hold on
        plot(M(i,:),"-*")
    end
    j = j+1;
    if(j>4)
        j = 1;
    end
    
end


%  if(mod(numel(M),4)==0)
%      M = reshape(M,[numel(M)/4,4]);
%      figure(1)
%      for i = 1:numel(M)/4
%          subplot(numel(M)/4,4,i)
%          if(mod(i,3)==0)
%              plot(M(i,:))
%              title("Linia " + num2str(i))
%          elseif(mod(i,3)==1)
%              stem(M(i,:))
%              title("Linia " + num2str(i))
%          elseif(mod(i,3)==2)
%              stairs(M(i,:))
%              title("Linia " + num2str(i))
%          end
%          
%      end
%     
%  else
%      disp("nu")
%  end
 