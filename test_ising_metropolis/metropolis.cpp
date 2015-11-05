#include "metropolis.h"

void oneFlop(mat &state, int &E )
{

    //finding index of one random spin
    int ix=0; //make random later
    int iy=0;
    int e_init = -1*state(iy,ix)*( state(iy,periodic(ix, L, 1)) + state(periodic(iy, L, 1),ix) );
    //flopping spin
    mat new_state = state;
    new_state(iy,ix) = state(iy,ix)*-1;
    int e_new = -1*new_state(iy,ix)*( new_state(iy,periodic(ix, L, 1)) + new_state(periodic(iy, L, 1),ix) );
    //computing trial(new) energy
    int E_t = E - e_init + e_new;
    //computing diff. in energy
    int dE = E_t - E;
    if(dE<=0)
    {
        state = new_state;
    }
    if(dE>0)
    {

    }


}
