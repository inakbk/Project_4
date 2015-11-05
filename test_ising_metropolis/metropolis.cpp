#include "metropolis.h"

void oneFlop(mat &state, int &E, double T, int L)
{
    //finding index of one random spin
    int ix=0; //make random later
    int iy=0;

    //flopping spin
    mat new_state = state;
    new_state(iy,ix) = state(iy,ix)*-1;

    //the amount of energy that will change if accepted
    int e_new = new_state(iy,ix)*( new_state(iy,periodic(ix, L, 1)) + new_state(periodic(iy, L, 1),ix) )
        + new_state(iy,periodic(ix,L,1))*( new_state(iy,periodic(ix, L, 2)) + new_state(periodic(iy, L, 1),periodic(ix,L,1)) )
        + new_state(periodic(iy,L,1),ix)*( new_state(iy,periodic(ix, L, 2)) + new_state(periodic(iy, L, 1),periodic(ix,L,1)) );
    //cout << "e_new = " << e_new << endl;

    //the amount of energy that was changed from
    int e_init = state(iy,ix)*( state(iy,periodic(ix, L, 1)) + state(periodic(iy, L, 1),ix) )
        + state(iy,periodic(ix,L,1))*( state(iy,periodic(ix, L, 2)) + state(periodic(iy, L, 1),periodic(ix,L,1)) )
        + state(periodic(iy,L,1),ix)*( state(iy,periodic(ix, L, 2)) + state(periodic(iy, L, 1),periodic(ix,L,1)) );
    //cout << "e_init = " << e_init << endl;

    //computing diff. in energy and deciding to change spin or not
    int dE = e_init - e_new;
    //cout << "dE: " << dE << endl;
    if(dE<=0)
    {
        state = new_state;
        E = E + dE;
    }
    if(dE>0)
    {
        double w = exp(-T*dE);
        double r = 0; //random nr. really
        if(r<=w)
        {
            state = new_state;
            E = E + dE;
            cout << "hello" << endl;
        }
    }
    cout << E << endl;
    state.print();
}
