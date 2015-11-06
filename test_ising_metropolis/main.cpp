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

    int maximum_nr_of_cycles = 100;//100000;
    int N = L*L;

    //initial state goes here, random or ordered
    mat state = 1*ones<mat>(L,L);
    state(0,1) = -1;
    state(1,0) = -1; //highest energy to test

    //energy of initial state:
    int E = 0; //in unist of J? J=1
    for(int i=0; i<L;++i)
    {
        for(int j=0; j<L; ++j)
        {
            E += -1*state(i,j)*( state(i,periodic(j, L, 1)) + state(periodic(i, L, 1),j) );
        }
    }
//----------------------------------------------------------------
    cout << E << endl;
    state.print();
    cout << "---" << endl;

    double mean_E = 0;
    double mean_E2 = 0;
    int number_of_accepted_cycles = 0;
    //open file here
    for(int i=0; i<maximum_nr_of_cycles;++i)
    {
        //one MC cycle:
        for(int n=0; n<N; ++n)
        {
            oneFlip(random_nr, state, E, beta_tilde, L, number_of_accepted_cycles);
        }
        mean_E += E;
        mean_E2 += E*E;

        //print E to file here
    }
    mean_E = mean_E/maximum_nr_of_cycles;
    mean_E = mean_E2/maximum_nr_of_cycles;
    C_v = mean_E2 - mean_E*mean_E; // in units of [1/(k_b T**2)]


    //print mean_E and mean_E2 to file here
    //close file here

//----------------------------------------------------------------
    cout << mean_E << endl;
    state.print();
    cout << "nr of accepted cycles: " << number_of_accepted_cycles << endl;

    return 0;
}

