#include <iostream>
#include <math.h>
#include <armadillo>
#include "metropolis.h"
#include "random.h"
#include <mpi.h>

using namespace std;
using namespace arma;

int main(int numberOfArguments, char** argumentList)
{
    int L = 20;
    int nr_of_cycles = 1000000;
    int chosen_initial_state = 1; //integer; -1 for random state, 0 for L=2 highest energy and 1 for all spins up.
    vec dE = {4, 8}; //w is only used when dE>0

    int numprocs, myRank;
    MPI_Init(&numberOfArguments, &argumentList);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

    double Tstart = 2.0;
    double Tend = 2.4;
    int numTemperatures = 21;
    //double Tstep = (Tend - Tstart)/(numTemperatures-1);
    vec temperatures = linspace<vec>(Tstart,Tend,numTemperatures);

    int numberOfTemperaturesPerProcessor = numTemperatures/numprocs;
    int TIndexStart = myRank*numberOfTemperaturesPerProcessor;
    int TIndexEnd = (myRank+1)*numberOfTemperaturesPerProcessor;
    if(myRank == numprocs-1) TIndexEnd = numTemperatures;

    for(int TIndex = TIndexStart; TIndex < TIndexEnd; TIndex++)
    {
        double T = temperatures[TIndex];
        int E = 0; //in unist of J=1
        int M = 0;
        mat state = 1*ones<mat>(L,L);
        long seed = -1;
        //if(production) seed = -time(NULL); //time in the core in seconds to give new random number each run
        Random random_nr(seed);

        initialState(random_nr, state, E, M, L, chosen_initial_state);

        vec w = exp(-dE/T);
        allMCcycles(random_nr, state, E, M, T, L, w, nr_of_cycles, chosen_initial_state, TIndex);
    }

    MPI_Finalize();

    return 0;
}


