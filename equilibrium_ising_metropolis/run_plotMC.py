from pylab import *
import os as os

"""
------------------------------------------------------------------------------------------
"""

def read_file(filename):
    infile = open(filename, "r")
    all_lines = infile.readlines()
    infile.close()

    nr_of_cycles = zeros(len(all_lines)/10)
    nr_of_accepted_config = zeros(len(all_lines)/10)
    mean_E = zeros(len(all_lines)/10)
    mean_E2 = zeros(len(all_lines)/10)
    C_v = zeros(len(all_lines)/10)
    mean_absM = zeros(len(all_lines)/10)
    mean_M2 = zeros(len(all_lines)/10)
    chi = zeros(len(all_lines)/10)

    i = 0
    j = 0
    while j < len(all_lines)/10:
        nr_of_cycles[j] = all_lines[0+i].split()[1]
        nr_of_accepted_config[j] = all_lines[1+i].split()[1]

        mean_E[j] = all_lines[2+i].split()[1]
        mean_E2[j] = all_lines[3+i].split()[1]
        C_v[j] = all_lines[4+i].split()[1]

        mean_absM[j] = all_lines[5+i].split()[1]
        mean_M2[j] = all_lines[6+i].split()[1]
        chi[j] = all_lines[7+i].split()[1]
        #T = all_lines[8+i].split()[1]
        #--- on all_lines[9+i].split()[1]
        i += 10
        j += 1

    return nr_of_cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi

"""
------------------------------------------------------------------------------------------
"""

T = 1.0

L = 20
N = L**2
max_nr_of_cycles = 500000 #must delelig 10
initial = 1

#compiling once:
#os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include -O3 -std=c++11')

Tcount = 100
#os.system('./main %s %s %s %s %s' %(T, L, max_nr_of_cycles, initial, Tcount))
filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)

#plot against MC cycles:

figure(1)
suptitle('L= %s, $k_bT=$ %s' %(L, T), fontsize=20)
subplot(2,2,1)
semilogx(cycles, mean_E, 'b')
title('Ordered initial state', fontsize=16)
ylabel('$<E>/J$', fontsize=18)

subplot(2,2,3)
semilogx(cycles, mean_absM, 'r')
ylabel('$<|\mathcal{M}|>$', fontsize=18)
xlabel('$t$', fontsize=18)

figure(2)
grid('on')
subplot(2,1,1)
semilogx(cycles, nr_of_accepted_config/(cycles*N))
title('T=%s' %T, fontsize=20)
legend(['Ordered initial state'], fontsize=14, loc='middle right')
ylabel('Accepted per spin', fontsize=14)

initial = -1
#os.system('./main %s %s %s %s %s' %(T, L, max_nr_of_cycles, initial, Tcount))
filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)

figure(1)
subplot(2,2,2)
semilogx(cycles, mean_E, 'k')
title('Random initial state', fontsize=16)

subplot(2,2,4)
semilogx(cycles, mean_absM, 'g')
xlabel('$t$', fontsize=18)

figure(2)
subplot(2,1,2)
semilogx(cycles, nr_of_accepted_config/(cycles*N))
legend(['Random initial state'], fontsize=14)
xlabel('$t$', fontsize=18)
ylabel('Accepted per spin', fontsize=14)

#tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
tight_layout()

show()








