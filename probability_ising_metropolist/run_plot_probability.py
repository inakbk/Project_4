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

def read_file2(filename):
    infile = open(filename, "r")
    all_lines = infile.readlines()
    infile.close()

    E = zeros(len(all_lines))
    for i in range(len(all_lines)):
        E[i] = float(all_lines[i].strip('E='))
    return E

"""
------------------------------------------------------------------------------------------
"""

T = 1.0

L = 20
N = L**2
max_nr_of_cycles = 100000 #must delelig 10
initial = 1

#compiling once:
os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include -O3 -std=c++11')

Tcount = 200
os.system('./main %s %s %s %s %s' %(T, L, max_nr_of_cycles, initial, Tcount))
filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
filename2 = 'metropolis_energies_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)
E = read_file2(filename2)

print "sigma= ", sqrt(C_v[-1]*N*T**2)

if T == 1:
    print "T= ", T
    hist(E, bins=10, normed=True, facecolor='green')
else:
    print "T= ", T
    hist(E, bins=32, normed=True, facecolor='green')

show()








