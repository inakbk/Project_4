#ifndef METROPOLIS_H
#define METROPOLIS_H
#include <armadillo>
#include "random.h"
#include <string>

using namespace arma;

//periodic bondary conditions
inline int periodic(int i, int limit, int add)
{ return (i+limit+add) % (limit);}

void initialState(Random &random_init_nr, mat &initial_state, int &energy, int &magnetization, int &L, int chosen_initial_state);

void oneFlip(Random &random_nr, mat &spin_state, int &energy, int &magnetization, double T, int L, vec w, int &number_of_accepted_cycles);

void allMCcycles(Random &random_nr, mat &spin_state, int &E, int &M, double T, int L, vec w, int maximum_nr_of_cycles, int chosen_initial_state, int Tcount);

#endif // METROPOLIS_H
