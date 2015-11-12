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

T = 2.0

L = 80
N = L**2
max_nr_of_cycles = 100000 #must delelig 10
initial = 1

#compiling once:
#os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include -O3 -std=c++11')

Tcount = 50
os.system('./main %s %s %s %s %s' %(T, L, max_nr_of_cycles, initial, Tcount))
filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)

"""
------------------------------------------------------------------------------------------
"""
#plot against MC cycles, accepted:

figure(0)
plot(cycles, nr_of_accepted_config)
title('Number of accepted cycles, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
xlabel('MC cycles')
ylabel('nr of accepted config')

#plot against MC cycles:

figure(1)
plot(cycles, mean_E)
title('mean_E, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
xlabel('MC cycles')
ylabel('mean_E')
"""
figure(2)
plot(cycles, mean_E2)
title('mean_E2, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
xlabel('MC cycles')
ylabel('mean_E2')

figure(3)
plot(cycles, C_v)
title('C_v, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
xlabel('MC cycles')
ylabel('C_v')
"""
figure(4)
plot(cycles, mean_absM)
title('mean_absM, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
xlabel('MC cycles')
ylabel('mean_absM')
"""
figure(5)
plot(cycles, mean_M2)
title('mean_M2, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
xlabel('MC cycles')
ylabel('mean_M2')

figure(6)
plot(cycles, chi)
title('chi, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
xlabel('MC cycles')
ylabel('chi')
"""
show()








