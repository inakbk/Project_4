#ifndef METROPOLIS_H
#define METROPOLIS_H
#include <armadillo>
#include "random.h"

using namespace arma;

//periodic bond. cond.
inline int periodic(int i, int limit, int add)
{ return (i+limit+add) % (limit);}

void oneFlip(Random &random_nr, mat &spin_state, int &energy, int &magnetization, double T, int L, int &number_of_accepted_cycles);

void allMCcycles(mat &spin_state, int &E, int &M, double T, int L, int maximum_nr_of_cycles);

//theoretical values for L=2:
void theoreticalValues(double T);

#endif // METROPOLIS_H
