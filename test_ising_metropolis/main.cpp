#include <iostream>
#include <armadillo>
#include "metropolis.h"

using namespace std;
using namespace arma;

//periodic bond. cond.
inline int periodic(int i, int limit, int add)
{ return (i+limit+add) % (limit);}

int main()
{
    double T = 1.0;
    int L = 2.0;

    int maximum_nr_of_cycles = 100000;

    //this can be calculated when needed
    int N = L*L;
    //microstates

    //initial state goes here, random or ordered
    mat state = 1*ones<mat>(L,L);
    state(0,0) = -1;
    //state(0,1) = 1;


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



    return 0;
}

