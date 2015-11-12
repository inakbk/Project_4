#include <iostream>
#include <math.h>
#include <armadillo>
#include "metropolis.h"
#include "random.h"

using namespace std;
using namespace arma;

int main(int argc, char *argv[])
{
    if(argc < 6)
    {
        cout << "Not enough command line arguments given. "
                "Give 3, in the following order: T, L, number_of_cycles, chosen_initial_state, Tcount, on command line. (chosen_initial_state takes the values -1, 0, 1)" << endl;
        cout << "Eks: >> ./main 1 2 10000 -1 0" << endl;
        exit(1);
    }

    vec T = {2.0, 2.1, 2.2, 2.3, 2.4};
    vec Tcount = {0,1,2,3,4}; //to separate files w. respect to temperature
    int L = 20;
    int nr_of_cycles = 100000;
    int chosen_initial_state = 1; //integer; -1 for random state, 0 for L=2 highest energy and 1 for all spins up.

    //bool production = false;
    //if(argc>=7) production = atoi(argv[6]);
//----------------------------------------------------------------

//    cout << chosen_initial_state << endl;
//    std::vector<Random*> randoms;
//    randoms.push_back(new Random(-omp_get_thread_number()));
//    randoms[omp_get_thread_number()].nextRandom()

//----------------------------------------------------------------
    for(i=0; i<sizeof(T);++i)
    {
        int E = 0; //in unist of J=1
        int M = 0;
        mat state = 1*ones<mat>(L,L);
        long seed = -1;
        //if(production) seed = -time(NULL); //time in the core in seconds to give new random number each run
        Random random_nr(seed);

        initialState(random_nr, state, E, M, L, chosen_initial_state);

        vec dE = {4, 8}; //w is only used when dE>0
        vec w = exp(-dE/T);
        allMCcycles(random_nr, state, E, M, T, L, w, nr_of_cycles, chosen_initial_state, Tcount);
    }



    return 0;
}
