#include "metropolis.h"
#include <string>

using namespace std;

void initialState(Random &random_init_nr, mat &state, int &E, int &M, int &L, int chosen_initial_state)
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
        for(int i=0; i<L;++i)
        {
            for(int j=0; j<L; ++j)
            {
                if(random_init_nr.nextDouble() < 0.5) // changing elements randomly, same prob. to be < og > 0.5?
                {
                    state(i,j) = -1;
                    //cout << "hello!!! random elem. (" << i << ", " << j << ")" << endl;
                }
            }
        }
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
//    state.print();
//    cout << M << endl;
}

void oneFlip(Random &random_nr, mat &state, int &E, int &M, double T, int L, vec w, int &number_of_accepted_cycles)
{
    //finding index of one random spin
    int ix=L*random_nr.nextDouble();
    int iy=L*random_nr.nextDouble();

    //computing diff. in energy and deciding to change spin or not
    int dE = 2*state(iy,ix)*( state(iy, periodic(ix, L, 1)) + state(periodic(iy, L, 1), ix)
                            + state(iy, periodic(ix, L, -1)) + state(periodic(iy, L, -1), ix) );  //e_init - e_new;    2*s_l^1
    //cout << "dE: " << dE << endl;
    if(dE<=0) //could also have let the positive values go to the metropolis test as exp(-dE/T) > r when dE<=0, then we would not need this if test
    {
        state(iy,ix) = -1*state(iy,ix);
        E += dE;
        M += 2*state(iy,ix);
        ++number_of_accepted_cycles;
    }
    if(dE>0)
    {
        //metropolis test
        double r = random_nr.nextDouble();
        if(r<=w[(dE-4)/4])
        {
            state(iy,ix) = -1*state(iy,ix);
            E += dE;
            M += 2*state(iy,ix);
            ++number_of_accepted_cycles;
            //cout << "Hello, unlikely state chosen. dE:" << dE << " w: " << w[(dE-4)/4] << endl;
        }
    }
}

void allMCcycles(Random &random_nr, mat &state, int &E, int &M, double T, int L, vec w, int maximum_nr_of_cycles, int chosen_initial_state)
{
    double N = L*L;
    // Random random_nr(-5);
    double mean_E = 0;
    double mean_E2 = 0;
    //double mean_M = 0;
    double mean_absM = 0;
    double mean_M2 = 0;
    //double C_v = 0;
    //double chi = 0;
    int number_of_accepted_cycles = 0;

    string filename = "metropolis_L" + to_string(L) + "_T" + to_string(int(T)) + "_initial" + to_string(chosen_initial_state) + "_MC" + to_string(maximum_nr_of_cycles) + ".txt";
    ofstream myfile;
    myfile.open(filename);

    for(int i=1; i<=maximum_nr_of_cycles;++i)
    {
        //one MC cycle:
        for(int n=0; n<N; ++n)
        {
            oneFlip(random_nr, state, E, M, T, L, w, number_of_accepted_cycles);
        }

        mean_E += E;
        mean_E2 += E*E;
        mean_absM += fabs(M);
        //mean_M += M;
        mean_M2 += M*M;

//----------------------------------------------------------------
//        //calculating mean values (normalizing):
//        mean_E = mean_E/i;
//        mean_E2 = mean_E2/i;
//        C_v = (mean_E2 - mean_E*mean_E)/(T*T); // divide by N in theoretical values

//        mean_absM = mean_absM/i;
//        mean_M = mean_M/i;
//        mean_M2 = mean_M2/i;
//        chi = (mean_M2 - mean_absM*mean_absM)/T;

//----------------------------------------------------------------
        //normalizing mean values and printing to file
        double norm = 1./i;
        //cout << norm << endl;
        myfile << "nr_of_cycles= " << i << endl;
        myfile << "nr_of_accepted_cycles= " << number_of_accepted_cycles << endl;

        myfile << "mean_E= "<< mean_E*norm << endl;
        myfile << "mean_E2= " << mean_E2*norm << endl;
        myfile << "C_V= " << ( mean_E2*norm - (mean_E*norm)*(mean_E*norm) )/(T*T) << endl;

        myfile << "mean_absM= " << mean_absM*norm << endl;
        myfile << "mean_M2= " << mean_M2*norm << endl;
        myfile << "chi= " << ( mean_M2*norm - (mean_absM*norm)*(mean_absM*norm) )/T << endl;
        myfile << "T= " << T << endl;
        myfile << "--------------" << endl;
    }

    myfile.close();
}

void theoreticalValues(double T, int chosen_initial_state)
{
    double exp_E = -8*sinh(8./T)/(cosh(8./T) + 3);
    double exp_E2 = 64*cosh(8./T)/(cosh(8./T) + 3);
    double C_v = ( 64./(T*T) )*( 1 + 3*cosh(8./T) )/( (cosh(8./T) + 3)*(cosh(8./T) + 3) );
    double exp_absM = 2*(exp(8./T) + 2)/(cosh(8./T) + 3);
    double exp_M2 = 8*(exp(8./T) + 1)/(cosh(8./T) + 3);
    double chi = 0;// (8./T)*(exp(8./T) + 1)/(cosh(8./T) + 3); this is wrong?

    cout << "Here comes theoretical values:" << endl;
    cout << "exp_E: "<< exp_E << endl;
    cout << "exp_E2: " << exp_E2 << endl;
    cout << "C_V = " << C_v << endl;
    cout << "----" << endl;
    cout << "exp_absM: " << exp_absM << endl;
    cout << "exp_M2: " << exp_M2 << endl;
    cout << "chi: " << chi << endl;
}

