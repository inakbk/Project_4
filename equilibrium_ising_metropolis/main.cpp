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

    double T = atof(argv[1]);//1.0;
    int L = atoi(argv[2]);//2;
    int nr_of_cycles = atoi(argv[3]);//100000;
    int chosen_initial_state = atoi(argv[4]);; //integer; -1 for random state, 0 for L=2 highest energy and 1 for all spins up.
    int Tcount = atoi(argv[5]); //to separate files w. respect to temperature
    bool production = false;
    if(argc>=7) production = atoi(argv[6]);

//    cout << chosen_initial_state << endl;
//    std::vector<Random*> randoms;
//    randoms.push_back(new Random(-omp_get_thread_number()));
//    randoms[omp_get_thread_number()].nextRandom()

//----------------------------------------------------------------
    // initial state:
    int E = 0; //in unist of J=1
    int M = 0;
    mat state = 1*ones<mat>(L,L);
    long seed = -1;
    if(production) seed = -time(NULL); //time in the core in seconds to give new random number each run

    Random random_nr(seed); //-1, -2, -3, -4 reserved for MPI (4 cores)
    initialState(random_nr, state, E, M, L, chosen_initial_state);

//    state.print();
//    cout << "after initializing " << E << endl;

//----------------------------------------------------------------
    vec dE = {4, 8}; //w is only used when dE>0
    vec w = exp(-dE/T);
    allMCcycles(random_nr, state, E, M, T, L, w, nr_of_cycles, chosen_initial_state, Tcount);

    //cout << Tcount << endl;
    //cout << "------" << endl;
    //theoreticalValues(T, chosen_initial_state);

//    state.print();
//    cout << E << endl;

    return 0;
}
