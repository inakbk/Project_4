#include <iostream>
#include <armadillo>
#include "metropolis.h"
#include "random.h"

using namespace std;
using namespace arma;

int main()
{
    double beta_tilde = 1.0;
    int L = 2.0;


    Random random_nr(-1);
//    std::vector<Random*> randoms;
//    randoms.push_back(new Random(-omp_get_thread_number()));
//    randoms[omp_get_thread_number()].nextRandom()

    cout << random_nr.nextDouble() << endl;

    int maximum_nr_of_cycles = 10;//100000;

    //this can be calculated when needed
    int N = L*L;
    //microstates

    //initial state goes here, random or ordered
    mat state = 1*ones<mat>(L,L);
    state(0,1) = -1;
    state(1,0) = -1; //highest energy to test

    //energy of state:
    int E = 0; //in unist of J? J=1
    for(int i=0; i<L;++i)
    {
        for(int j=0; j<L; ++j)
        {
            E += -1*state(i,j)*( state(i,periodic(j, L, 1)) + state(periodic(i, L, 1),j) );
        }
    }

    cout << E << endl;
    state.print();
    cout << "---" << endl;

    int number_of_accepted_cycles = 0;
    for(int i=0; i<maximum_nr_of_cycles;++i)
    {
        oneFlip(random_nr, state, E, beta_tilde, L, number_of_accepted_cycles);
        state.print();
        cout << "---" << endl;
    }

    cout << E << endl;


    cout << "nr of accepted cycles: " << number_of_accepted_cycles << endl;

    return 0;
}

