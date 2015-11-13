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
                if(random_init_nr.nextDouble() < 0.5)
                {
                    state(i,j) = -1;
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
}

void oneFlip(Random &random_nr, mat &state, int &E, int &M, double T, int L, vec w, int &number_of_accepted_cycles)
{
    //finding index of one random spin
    int ix=L*random_nr.nextDouble();
    int iy=L*random_nr.nextDouble();

    //computing diff. in energy and deciding to change spin or not
    int dE = 2*state(iy,ix)*( state(iy, periodic(ix, L, 1)) + state(periodic(iy, L, 1), ix)
                            + state(iy, periodic(ix, L, -1)) + state(periodic(iy, L, -1), ix) );
    if(dE<=0)
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
        }
    }
}

void allMCcycles(Random &random_nr, mat &state, int &E, int &M, double T, int L, vec w, int maximum_nr_of_cycles, int chosen_initial_state, int Tcount)
{
    double N = L*L;
    double mean_E = 0;
    double mean_E2 = 0;
    double mean_absM = 0;
    double mean_M2 = 0;
    int number_of_accepted_cycles = 0;

    //reaching equilibrium state first:
    for(int i=1; i<=20000;++i)
    {
        //one MC cycle:
        for(int n=0; n<N; ++n)
        {
            oneFlip(random_nr, state, E, M, T, L, w, number_of_accepted_cycles);
        }
    }

    //string filename = "metropolis_L" + to_string(L) + "_Tcount" + to_string(Tcount) + "_initial" + to_string(chosen_initial_state) + "_MC" + to_string(maximum_nr_of_cycles) + ".txt";
    string filename = "metropolis_energies_L" + to_string(L) + "_Tcount" + to_string(Tcount) + "_initial" + to_string(chosen_initial_state) + "_MC" + to_string(maximum_nr_of_cycles) + ".txt";
    ofstream myfile;
    myfile.open(filename);

    for(int i=1; i<=maximum_nr_of_cycles;++i)
    {
        //one MC cycle:
        for(int n=0; n<N; ++n)
        {
            oneFlip(random_nr, state, E, M, T, L, w, number_of_accepted_cycles);
        }

        //calculating mean values now that equilibrium is reached
//        mean_E += E;
//        mean_E2 += E*E;
//        mean_absM += fabs(M);
//        mean_M2 += M*M;
    }

    //writing energies to file:
    myfile2 << "E= " << E << endl;

//    //normalizing mean values and printing to file when done (values per spin, deviding by N)
//    double norm = 1./maximum_nr_of_cycles;
//    myfile << "nr_of_cycles= " << maximum_nr_of_cycles << endl;
//    myfile << "nr_of_accepted_cycles= " << number_of_accepted_cycles << endl;

//    myfile << "mean_E= "<< mean_E*norm/N << endl;
//    myfile << "mean_E2= " << mean_E2*norm/N << endl;
//    myfile << "C_V= " << ( mean_E2*norm - (mean_E*norm)*(mean_E*norm) )/(T*T)/N << endl;

//    myfile << "mean_absM= " << mean_absM*norm/N << endl;
//    myfile << "mean_M2= " << mean_M2*norm/N << endl;
//    myfile << "chi= " << ( mean_M2*norm - (mean_absM*norm)*(mean_absM*norm) )/T/N << endl;
//    myfile << "T= " << T << endl;
//    myfile << "--------------" << endl;

    myfile.close();
}


