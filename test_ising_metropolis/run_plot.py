from pylab import *
import os as os

"""
------------------------------------------------------------------------------------------
"""
def read_file(filename):
    infile = open(filename, "r")
    all_lines = infile.readlines()
    infile.close()

    nr_of_accepted_cycles = all_lines[0].split()[1]
    mean_E = all_lines[1].split()[1]
    mean_E2 = all_lines[2].split()[1]
    C_V = all_lines[3].split()[1]

    mean_absM = all_lines[5].split()[1]
    mean_M2 = all_lines[6].split()[1]
    chi = all_lines[7].split()[1]

    return nr_of_accepted_cycles, mean_E, mean_E2, C_V, mean_absM, mean_M2, chi

def exp_E_theory(T):
    return -8*sinh(8./T)/(cosh(8./T) + 3)

def exp_E2_theory(T):
    return 64*cosh(8./T)/(cosh(8./T) + 3)

def C_v_theory(T):
    return ( 64./(T*T) )*( 1 + 3*cosh(8./T) )/( (cosh(8./T) + 3)*(cosh(8./T) + 3) )

def exp_absM_theory(T):
    return 2*(exp(8./T) + 2)/(cosh(8./T) + 3)

def exp_M2_theory(T):
    return 8*(exp(8./T) + 1)/(cosh(8./T) + 3)

def chi_theory(T):
    return (8./T)*(exp(8./T) + 1)/(cosh(8./T) + 3)

"""
------------------------------------------------------------------------------------------
"""

T = 1.0
L = 2
max_nr_of_cycles = 10000
initial = 0

os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include')

step = 10
start_cycle = 10
N = linspace(start_cycle, max_nr_of_cycles, (max_nr_of_cycles-start_cycle)/step)

nr_of_accepted_cycles = zeros(start_cycle, max_nr_of_cycles, (max_nr_of_cycles-start_cycle)/step)
mean_E = zeros(start_cycle, max_nr_of_cycles, (max_nr_of_cycles-start_cycle)/step)
mean_E2 = zeros(start_cycle, max_nr_of_cycles, (max_nr_of_cycles-start_cycle)/step)
C_V = zeros(start_cycle, max_nr_of_cycles, (max_nr_of_cycles-start_cycle)/step)
mean_absM = zeros(start_cycle, max_nr_of_cycles, (max_nr_of_cycles-start_cycle)/step)
mean_M2 = zeros(start_cycle, max_nr_of_cycles, (max_nr_of_cycles-start_cycle)/step)
chi = zeros(start_cycle, max_nr_of_cycles, (max_nr_of_cycles-start_cycle)/step)

for i in range(len(N)):
    os.system('./main %s %s %s %s' %(T, L, N[i], initial))
    filename = 'metropolis_L%s_T%s_initial%s_MC%s.txt' %(L, int(T), initial, N[i])
    nr_of_accepted_cycles[i], mean_E[i], mean_E2[i], C_V[i], mean_absM[i], mean_M2[i], chi[i] = read_file(filename)









