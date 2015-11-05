#ifndef METROPOLIS_H
#define METROPOLIS_H
#include <armadillo>

using namespace arma;

void oneFlop(mat &spin_state, int &energy, double T, int L);

//periodic bond. cond.
inline int periodic(int i, int limit, int add)
{ return (i+limit+add) % (limit);}



#endif // METROPOLIS_H
