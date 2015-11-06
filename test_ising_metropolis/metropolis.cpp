#include "metropolis.h"

void oneFlip(Random &random_nr, mat &state, int &E, double beta_tilde, int L, int &number_of_accepted_cycles)
{
    //finding index of one random spin
    int ix=L*random_nr.nextDouble();
    int iy=L*random_nr.nextDouble();

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
        ++number_of_accepted_cycles;
        //cout << "hello you" << endl;
        //cout << "dE: " << dE << endl;
    }
    if(dE>0)
    {
        double w = exp(-beta_tilde*dE);
        //cout << w << endl;
        double r = random_nr.nextDouble();
        //cout << r << endl;
        if(r<=w)
        {
            state = new_state;
            E = E + dE;
            ++number_of_accepted_cycles;
            cout << "hello" << endl;
        }
    }

}
