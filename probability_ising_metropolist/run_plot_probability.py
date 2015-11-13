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

L = 20
N = L**2
max_nr_of_cycles = 500000 #must delelig 10
initial = 1

#compiling once:
#os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include -O3 -std=c++11')

T = 1.0
Tcount = 0
#os.system('./main %s %s %s %s %s' %(T, L, max_nr_of_cycles, initial, Tcount))
filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
filename2 = 'metropolis_energies_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)
E = read_file2(filename2)
E = E/N #per spin

figure(1)
subplot(3,1,1)
#title('cdw', fontsize=16)
number_of_bins = 5
count, Energy_bins = histogram(E, bins=number_of_bins)
probability = count/float(sum(count))
bar(left=Energy_bins[:-1], height=probability, width=abs(Energy_bins[0] - Energy_bins[1]), color='b')
legend(['$T=$ %s, $\sigma_E$= %.2f' %(T, sqrt(C_v[-1]*T**2))], fontsize=16)
ylabel('$P(E)$', fontsize=16)


T = 2.0
Tcount = 1
#os.system('./main %s %s %s %s %s' %(T, L, max_nr_of_cycles, initial, Tcount))
filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
filename2 = 'metropolis_energies_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)
E = read_file2(filename2)
E = E/N

subplot(3,1,2)

number_of_bins = 77
count, Energy_bins = histogram(E, bins=number_of_bins)
probability = count/float(sum(count))
bar(left=Energy_bins[:-1], height=probability, width=abs(Energy_bins[0] - Energy_bins[1]), color='g')
legend(['$T=$ %s, $\sigma_E$= %.2f' %(T, sqrt(C_v[-1]*T**2))], fontsize=16)
ylabel('$P(E)$', fontsize=16)

T = 2.4
Tcount = 2
#os.system('./main %s %s %s %s %s' %(T, L, max_nr_of_cycles, initial, Tcount))
filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
filename2 = 'metropolis_energies_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)
E = read_file2(filename2)
E = E/N

subplot(3,1,3)

number_of_bins = 116
count, Energy_bins = histogram(E, bins=number_of_bins)
probability = count/float(sum(count))
bar(left=Energy_bins[:-1], height=probability, width=abs(Energy_bins[0] - Energy_bins[1]), color='r')

legend(['$T=$ %s, $\sigma_E$= %.1f' %(T, sqrt(C_v[-1]*T**2))], fontsize=16, loc='upper left')
xlabel('Energy per spin', fontsize=16)
ylabel('$P(E)$', fontsize=16)

show()








