#include <iostream>
#include <mpi.h>

using namespace std;

int main(int numberOfArguments, char** argumentList)
{
    int numprocs, myRank;
    MPI_Init(&numberOfArguments, &argumentList);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

    cout << "Hello I am processor " << myRank << " of total " << numprocs << endl;

    MPI_Finalize();
    return 0;
}

