from pylab import *
import os as os
import matplotlib.pyplot as plt


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

T = linspace(1,9,20)

L = 20
N = L**2
max_nr_of_cycles = 500000 #must delelig 10
initial = -1


#compiling once:
#os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include -O3 -std=c++11')

nr_of_accepted_config_plot = zeros(len(T))
mean_E_plot = zeros(len(T))
mean_E2_plot = zeros(len(T))
C_v_plot = zeros(len(T))
mean_absM_plot = zeros(len(T))
mean_M2_plot = zeros(len(T))
chi_plot = zeros(len(T))

Tcount = 0
for i in range(len(T)):
    os.system('./main %s %s %s %s %s' %(T[i], L, max_nr_of_cycles, initial, Tcount))
    filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
    cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)
    Tcount += 1    

    nr_of_accepted_config_plot[i] = nr_of_accepted_config[-1]
    mean_E_plot[i] = mean_E[-1]
    mean_E2_plot[i] = mean_E2[-1]
    C_v_plot[i] = C_v[-1]
    mean_absM_plot[i] = mean_absM[-1]
    mean_M2_plot[i] = mean_M2[-1]
    chi_plot[i] = chi[-1]

figure(1)
plot(T, nr_of_accepted_config_plot/(max_nr_of_cycles*N))
title('#MC cycles= %g, L= %s, initial_state= %s' %(max_nr_of_cycles, L, initial), fontsize=16)
xlabel('$T$', fontsize=18)
ylabel('Accepted per spin', fontsize=16)

show()








