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
    int maximum_nr_of_cycles = 100;//100000;
    int N = L*L;


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

    Random random_nr(-2);
    double mean_E = 0;
    double mean_E2 = 0;
    double mean_M = 0;
    double mean_M2 = 0;
    int number_of_accepted_cycles = 0;
    //open file here
    for(int i=0; i<maximum_nr_of_cycles;++i)
    {
        //one MC cycle:
        for(int n=0; n<N; ++n)
        {
            oneFlip(random_nr, state, E, M, beta_tilde, L, number_of_accepted_cycles);
        }
        mean_E += E;
        mean_E2 += E*E;
        mean_M += abs(M);
        mean_M2 += M*M;

        //print E and stuff to file here
    }

    //calculating mean values:
    mean_E = mean_E/maximum_nr_of_cycles;
    mean_E2 = mean_E2/maximum_nr_of_cycles;
    double C_v = mean_E2 - mean_E*mean_E; // in units of [1/(k_b T**2)]

    mean_M = mean_M/maximum_nr_of_cycles;
    mean_M2 = mean_M2/maximum_nr_of_cycles;
    double chi = mean_M2 - mean_M*mean_M; // in units of [1/(k_b T**2)]

    //print mean_E and mean_E2 and stuff to file here
    //close file here

//----------------------------------------------------------------
    cout << mean_E*mean_E << endl;
    cout << mean_E2 << endl;
    cout << C_v << endl;
    cout << "----" << endl;
    cout << mean_M*mean_M << endl;
    cout << mean_M2 << endl;
    cout << chi << endl;

    state.print();
    cout << "nr of accepted cycles: " << number_of_accepted_cycles << endl;

    return 0;
}

