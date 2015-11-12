#include <iostream>
#include <mpi.h>
#include <vector>
#include <armadillo>

using namespace std;
using namespace arma;

int main(int numberOfArguments, char** argumentList)
{
    int numprocs, myRank;
    MPI_Init(&numberOfArguments, &argumentList);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

    cout << "numprocs " << numprocs << endl;

    double Tstart = 2.0;
    double Tend = 2.5;
    int numTemperatures = 11;
    //double Tstep = (Tend - Tstart)/(numTemperatures-1);

    vec temperatures = linspace<vec>(Tstart,Tend,numTemperatures);

    int numberOfTemperaturesPerProcessor = numTemperatures/numprocs;
    int TIndexStart = myRank*numberOfTemperaturesPerProcessor;
    int TIndexEnd = (myRank+1)*numberOfTemperaturesPerProcessor;
    if(myRank == numprocs-1) TIndexEnd = numTemperatures;

    for(int TIndex = TIndexStart; TIndex < TIndexEnd; TIndex++)
    {
        double T = temperatures[TIndex];
        cout << "index= " << TIndex << " T= " << T << endl;
        //cout << "Hello I am processor " << myRank << " of total " << numprocs << " and T is: " << T << endl;
    }

    MPI_Finalize();
    return 0;
}

