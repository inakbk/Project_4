#include "metropolis.h"

void initialState(mat state, int &E, int &M, int &L, int chosen_initial_state)
{
    if(abs(chosen_initial_state) > 1)
    {
        cout << "Wrong input!" << endl;
        cout << "Function to initiate state must have last argument chosen_initial_state as a integer, -1 for random state, 0 for L=2 highest energy and 1 for all spins up. "  << endl;
    }

    //highest energy state for test case, L=2
    if(chosen_initial_state == 0)
    {
        if(L!=2)
        {
            cout << "Wrong input! Set chosen_initial_state=0 only when L=0! Aborting, L is: " << L << endl;
            exit(1);
        }
        state(0,1) = -1;
        state(1,0) = -1;
    }

    //random state:
    if(chosen_initial_state == -1)
    {
        //create random state
        cout << "Code to generate random state not ready!" << endl;
    }

    //energy and magnetization of initial state:
    for(int i=0; i<L;++i)
    {
        for(int j=0; j<L; ++j)
        {
            E += -1*state(i,j)*( state(i,periodic(j, L, 1)) + state(periodic(i, L, 1),j) );
            M += state(i,j);
        }
    }
}

void oneFlip(Random &random_nr, mat &state, int &E, int &M, double T, int L, int &number_of_accepted_cycles)
{
    //finding index of one random spin
    int ix=L*random_nr.nextDouble();
    int iy=L*random_nr.nextDouble();

    //the energy caused by the one chosen spin before flip
    int e_init = state(iy,ix)*( state(iy,periodic(ix, L, 1)) + state(periodic(iy, L, 1),ix) )
        + state(iy,periodic(ix,L,1))*( state(iy,periodic(ix, L, 2)) + state(periodic(iy, L, 1),periodic(ix,L,1)) )
        + state(periodic(iy,L,1),ix)*( state(iy,periodic(ix, L, 2)) + state(periodic(iy, L, 1),periodic(ix,L,1)) );
    int m_init = state(iy,ix);

    //flipping spin, trial state:
    mat new_state = state;
    new_state(iy,ix) = -1*state(iy,ix);

    //the energy caused by the one chosen spin if flip accepted
    int e_new = new_state(iy,ix)*( new_state(iy,periodic(ix, L, 1)) + new_state(periodic(iy, L, 1),ix) )
        + new_state(iy,periodic(ix,L,1))*( new_state(iy,periodic(ix, L, 2)) + new_state(periodic(iy, L, 1),periodic(ix,L,1)) )
        + new_state(periodic(iy,L,1),ix)*( new_state(iy,periodic(ix, L, 2)) + new_state(periodic(iy, L, 1),periodic(ix,L,1)) );
    int m_new = new_state(iy,ix);

    //computing diff. in energy and deciding to change spin or not
    int dE = e_init - e_new;
    //cout << "dE: " << dE << endl;
    if(dE<=0)
    {
        state = new_state;
        E = E + dE;
        M = M - m_init + m_new;
        ++number_of_accepted_cycles;
    }
    if(dE>0)
    {
        double w = exp(-dE/T);
        double r = random_nr.nextDouble();
        if(r<=w)
        {
            state = new_state;
            E = E + dE;
            M = M - m_init + m_new;
            ++number_of_accepted_cycles;
            cout << "Hello, unlikely state chosen. " << endl;
        }
    }
}

void allMCcycles(mat &state, int &E, int &M, double T, int L, int maximum_nr_of_cycles)
{
    int N = L*L;
    Random random_nr(-2);
    double mean_E = 0;
    double mean_E2 = 0;
    double mean_M = 0;
    double mean_absM = 0;
    double mean_M2 = 0;
    int number_of_accepted_cycles = 0;

    //open file here
    for(int i=0; i<maximum_nr_of_cycles;++i)
    {
        //one MC cycle:
        for(int n=0; n<N; ++n)
        {
            oneFlip(random_nr, state, E, M, T, L, number_of_accepted_cycles);
        }
        mean_E += E;
        mean_E2 += E*E;
        mean_absM += abs(M);
        mean_M += M;
        mean_M2 += M*M;

        //print E and stuff to file here
    }

    //calculating mean values:
    mean_E = mean_E/maximum_nr_of_cycles;
    mean_E2 = mean_E2/maximum_nr_of_cycles;
    double C_v = (mean_E2 - mean_E*mean_E)/(T*T); // in units of

    mean_absM = mean_absM/maximum_nr_of_cycles;
    mean_M = mean_M/maximum_nr_of_cycles;
    mean_M2 = mean_M2/maximum_nr_of_cycles;
    double chi = (mean_M2 - mean_M*mean_M)/T; // in units of

    //print mean_E and mean_E2 and stuff to file here
    //close file here

//----------------------------------------------------------------
    cout << "mean_E: "<< mean_E << endl;
    cout << "mean_E2: " << mean_E2 << endl;
    cout << "C_V = " << C_v << endl;
    cout << "----" << endl;
    cout << "mean_absM: " << mean_absM << endl;
    cout << "mean_M2: " << mean_M2 << endl;
    cout << "chi: " << chi << endl;

    state.print();
    cout << "nr of accepted cycles: " << number_of_accepted_cycles << endl;
}

void theoreticalValues(double T, int chosen_initial_state)
{
    double exp_E = -8*sinh(8./T)/(cosh(8./T) + 3);
    double exp_E2 = 64*cosh(8./T)/(cosh(8./T) + 3);
    double C_v = ( 64./(T*T) )*( 1 + 3*cosh(8./T) )/( (cosh(8./T) + 3)*(cosh(8./T) + 3) );
    double exp_absM = 2*(exp(8./T) + 2)/(cosh(8./T) + 3);
    double exp_M2 = 8*(exp(8./T) + 1)/(cosh(8./T) + 3);
    double chi = (8./T)*(exp(8./T) + 1)/(cosh(8./T) + 3);

    //print to file
    cout << "Here comes theoretical values:" << endl;
    cout << "exp_E: "<< exp_E << endl;
    cout << "exp_E2: " << exp_E2 << endl;
    cout << "C_V = " << C_v << endl;
    cout << "----" << endl;
    cout << "exp_absM: " << exp_absM << endl;
    cout << "exp_M2: " << exp_M2 << endl;
    cout << "chi: " << chi << endl;
}

