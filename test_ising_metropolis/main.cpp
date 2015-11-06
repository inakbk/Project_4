#include <iostream>
#include <math.h>
#include <armadillo>
#include "metropolis.h"
#include "random.h"

using namespace std;
using namespace arma;

int main()
{
    double T = 1.0;
    int L = 2;
    int maximum_nr_of_cycles = 10000;//100000;

    //Random random_nr(-2);
//    std::vector<Random*> randoms;
//    randoms.push_back(new Random(-omp_get_thread_number()));
//    randoms[omp_get_thread_number()].nextRandom()

//----------------------------------------------------------------

    int E = 0; //in unist of J=1
    int M = 0;
    mat state = 1*ones<mat>(L,L);
    int chosen_initial_state = 0;
    initialState(state, E, M, L, chosen_initial_state);

    allMCcycles(state, E, M, T, L, maximum_nr_of_cycles);

    cout << "------" << endl;
    theoreticalValues(T, chosen_initial_state);

    return 0;
}

