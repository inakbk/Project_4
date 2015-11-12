#include <iostream>
#include <math.h>
#include <armadillo>
#include "metropolis.h"
#include "random.h"

using namespace std;
using namespace arma;

int main(int numberOfArguments, char** argumentList)
{

    //vec T = {2.0, 2.1, 2.2, 2.3, 2.4};
    //vec Tcount = {0,1,2,3,4}; //to separate files w. respect to temperature
    int L = 20;
    int nr_of_cycles = 100000;
    int chosen_initial_state = 1; //integer; -1 for random state, 0 for L=2 highest energy and 1 for all spins up.
    vec dE = {4, 8}; //w is only used when dE>0

    int numprocs, myRank;
    MPI_Init(&numberOfArguments, &argumentList);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

    //T=(2,..,2.4);
    double Tstart = myRank*N_T/N_p;
    double Tend = (myRank+1)*N_T/N_p;
    double dT = 0.05;

    for(double T=Tstart; T < Tend-1; T+=dT)
    {
        int E = 0; //in unist of J=1
        int M = 0;
        mat state = 1*ones<mat>(L,L);
        long seed = -1;
        //if(production) seed = -time(NULL); //time in the core in seconds to give new random number each run
        Random random_nr(seed);

        initialState(random_nr, state, E, M, L, chosen_initial_state);

        vec w = exp(-dE/T);
        allMCcycles(random_nr, state, E, M, T, L, w, nr_of_cycles, chosen_initial_state, Tcount);
    }


    MPI_Finalize();



    //bool production = false;
    //if(argc>=7) production = atoi(argv[6]);
//----------------------------------------------------------------

//    cout << chosen_initial_state << endl;
//    std::vector<Random*> randoms;
//    randoms.push_back(new Random(-omp_get_thread_number()));
//    randoms[omp_get_thread_number()].nextRandom()

//----------------------------------------------------------------


    return 0;
}


