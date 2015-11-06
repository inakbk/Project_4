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
    int L = 2.0;
    int maximum_nr_of_cycles = 10000;//100000;

    //Random random_nr(-2);
//    std::vector<Random*> randoms;
//    randoms.push_back(new Random(-omp_get_thread_number()));
//    randoms[omp_get_thread_number()].nextRandom()

//----------------------------------------------------------------
    //initial state goes here, random or ordered
    mat state = 1*ones<mat>(L,L);
    state(0,1) = -1;
    state(1,0) = -1; //highest energy to test

    //energy and magnetization of initial state:
    int E = 0; //in unist of J? J=1
    int M = 0;
    for(int i=0; i<L;++i)
    {
        for(int j=0; j<L; ++j)
        {
            E += -1*state(i,j)*( state(i,periodic(j, L, 1)) + state(periodic(i, L, 1),j) );
            M += state(i,j);
        }
    }
    cout << E << endl;
    state.print();
    cout << "---" << endl;

//----------------------------------------------------------------
    allMCcycles(state, E, M, T, L, maximum_nr_of_cycles);

    cout << "------" << endl;
    theoreticalValues(T);

    return 0;
}

