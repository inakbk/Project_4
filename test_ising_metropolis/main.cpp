#include <iostream>
#include <math.h>
#include <armadillo>
#include "metropolis.h"
#include "random.h"

using namespace std;
using namespace arma;

int main(int argc, char *argv[])
{
    if(argc < 5)
    {
        cout << "Not enough command line arguments given. "
                "Give 3, in the following order: T, L, number_of_cycles, on command line." << endl;
        cout << "Eks: >> ./main 1 2 10000" << endl;
        exit(1);
    }
    double T = atof(argv[1]);//1.0;
    int L = atoi(argv[2]);//2;
    int nr_of_cycles = atoi(argv[3]);//10000;//100000;
    int chosen_initial_state = atoi(argv[4]);; //integer; -1 for random state, 0 for L=2 highest energy and 1 for all spins up.


    //Random random_nr(-2);
//    std::vector<Random*> randoms;
//    randoms.push_back(new Random(-omp_get_thread_number()));
//    randoms[omp_get_thread_number()].nextRandom()

//----------------------------------------------------------------
    // initial state:
    int E = 0; //in unist of J=1
    int M = 0;
    mat state = 1*ones<mat>(L,L);
    initialState(state, E, M, L, chosen_initial_state);

//    state.print();
//    cout << "2" << E << endl;

//----------------------------------------------------------------
    allMCcycles(state, E, M, T, L, nr_of_cycles, chosen_initial_state);

    //cout << "------" << endl;
    //theoreticalValues(T, chosen_initial_state);

//    state.print();
//    cout << E << endl;

    return 0;
}




//ofstream myfile;
//string filename = "EigenValVecSolver_" + FileName + "_pMax" + to_string(index) + "_nStep" + to_string(n_step) + ".txt";
//myfile.open (filename);
//myfile << "Equations solved with the " << FileName << " algorithm." << endl;
//myfile << "Dimention of matrix + 1, n_step = " << n_step << endl;
//myfile << "Index of p_max: " << index << endl;
//myfile << "Execution time: " << time << endl;

//myfile << "Number of iterations for jacobi algoritm: " << number_of_iterations << endl;

//myfile.close();
