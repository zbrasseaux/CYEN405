function [d,t] = part1(np, nd)

    A = randn(np,nd);
    B = randn(np,nd);
    d = zeros(np,1);

    tic;

    for i=1:np
    	for j=1:nd
    		d(i) = part2(B(i,j) - A(i,j));
    	end
    end
end