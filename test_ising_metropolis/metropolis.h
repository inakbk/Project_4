#ifndef METROPOLIS_H
#define METROPOLIS_H
#include <armadillo>
#include "random.h"

using namespace arma;

void oneFlip(Random &random_nr, mat &spin_state, int &energy, int &magnetization, double beta_tilde, int L, int &number_of_accepted_cycles);

//periodic bond. cond.
inline int periodic(int i, int limit, int add)
{ return (i+limit+add) % (limit);}



#endif // METROPOLIS_H
