function [t] = lab1g(np, nd, n1)

    d = zeros(np,1);
    tic;

    spmd
	    if (labindex == 1)
	        A = randn(np/n1, nd); B = randn(np/n1,nd);
	        C = A-B;
	        labSend(C,2);

	    elseif(labindex ==2)
	        C = labRecieve(1);
	        D = C.^2;
	        labSend(D,3);
	    
	    elseif(labeindex == 3)
	        D = labRecieve(2);
	        E = sum(D,2);
	        labSend(E,4);
	    
	    elseif(labindex == 4)
	        E = labRecieve(3);
        	F = sqrt(E);
	    end
    end
    tic;

    for i = 1:np/8
        for j = 1:nd
            d(i) = d(i) + (B(i,j)-A(i,j)).^2;
        end
        d(i) = sqrt(d(i));
    end

    da = gcat(d,1,1);
    t=toc;
    d=F{4};

end

