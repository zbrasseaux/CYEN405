  
#include <stdio.h>
#include <time.h>
#include "mpi.h"

int main (int argc, char *argv[]) {
	int rank;
	int size;
	double start, end;

	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	
	start = MPI_Wtime();
	
	printf("Hello, Zach from #%d of %d!\n",rank,size);
	
	MPI_Barrier(MPI_COMM_WORLD);

	end = MPI_Wtime();

	if (rank == 0) {
		double t = (end-start);
		printf("Time elapsed is %f secs.\n",t);
	}

	MPI_Finalize();

	return 0;
}