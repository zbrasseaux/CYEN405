function [t] = lab1h(np,nd, nw)
if (nargin < 1), np = 1e1; nd = 10; nw=1; end

	hp = gcp('nocreate');
	if isempty(hp), hp=parpool(nw); end
	
	A = distributed(randn(np, nd)); B = distributed(randn(np,nd));
	d = distributed(zeros(np,1));

	tic;

	parfor i = 1:np
    		for j = 1:nd
        		d(i) = d(i) + (B(i,j)-A(i,j)).^2;
    		end
    		d(i) = sqrt(d(i));
	end
	t = toc;

delete(hp);
