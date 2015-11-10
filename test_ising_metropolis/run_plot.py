from pylab import *
import os as os

"""
------------------------------------------------------------------------------------------
"""
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
    #return (8./T)*(exp(8./T) + 1)/(cosh(8./T) + 3)
    return (4./T)*( ( 2*(exp(8./T) + 2) - (exp(8./T) + 2)**2 )/( cosh(8./T) + 3 )**2 )

def read_file(filename):
    infile = open(filename, "r")
    all_lines = infile.readlines()
    infile.close()

    nr_of_accepted_config = all_lines[0].split()[1]
    mean_E = all_lines[1].split()[1]
    mean_E2 = all_lines[2].split()[1]
    C_V = all_lines[3].split()[1]

    mean_absM = all_lines[4].split()[1]
    mean_M2 = all_lines[5].split()[1]
    chi = all_lines[6].split()[1]

    return nr_of_accepted_config, mean_E, mean_E2, C_V, mean_absM, mean_M2, chi

"""
------------------------------------------------------------------------------------------
"""

T = 1.0
L = 2
max_nr_of_cycles = 10000
initial = -1

#compiling once:
os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include -O3 -std=c++11')


step = max_nr_of_cycles/100
cycles = linspace(step, max_nr_of_cycles, max_nr_of_cycles/step)

nr_of_accepted_config = zeros(len(cycles))
mean_E = zeros(len(cycles))
mean_E2 = zeros(len(cycles))
C_v = zeros(len(cycles))
mean_absM = zeros(len(cycles))
mean_M2 = zeros(len(cycles))
chi = zeros(len(cycles))

for i in range(len(cycles)):
    os.system('./main %s %s %s %s' %(T, L, cycles[i], initial))
    filename = 'metropolis_L%s_T%s_initial%s_MC%s.txt' %(L, int(T), initial, int(cycles[i]))
    nr_of_accepted_config[i], mean_E[i], mean_E2[i], C_v[i], mean_absM[i], mean_M2[i], chi[i] = read_file(filename)



figure(1)
plot(cycles, mean_E)
hold('on')
plot(cycles, exp_E_theory(T)*ones(len(cycles)))
title('mean_E')

figure(2)
plot(cycles, mean_E2)
hold('on')
plot(cycles, exp_E2_theory(T)*ones(len(cycles)))
title('mean_E2')

figure(3)
plot(cycles, C_v)
hold('on')
plot(cycles, C_v_theory(T)*ones(len(cycles)))
title('C_v')

figure(4)
plot(cycles, mean_absM)
hold('on')
plot(cycles, exp_absM_theory(T)*ones(len(cycles)))
title('mean_absM')

figure(5)
plot(cycles, mean_M2)
hold('on')
plot(cycles, exp_M2_theory(T)*ones(len(cycles)))
title('mean_M2')

figure(6)
plot(cycles, chi)
hold('on')
plot(cycles, chi_theory(T)*ones(len(cycles)))
title('chi')
"""


figure(1)
plot(cycles, abs(mean_E - exp_E_theory(T)))
title('error mean_E')

figure(2)
plot(cycles, abs(mean_E2 - exp_E2_theory(T)*ones(len(cycles))))
title('error mean_E2')

figure(3)
plot(cycles, abs(C_v - C_v_theory(T)*ones(len(cycles))))
title('error C_v')

figure(4)
plot(cycles, abs(mean_absM - exp_absM_theory(T)*ones(len(cycles))))
title('error mean_absM')

figure(5)
plot(cycles, abs(mean_M2 - exp_M2_theory(T)*ones(len(cycles))))
title('error mean_M2')

figure(6)
plot(cycles, abs(chi - chi_theory(T)*ones(len(cycles))))
title('error chi')
"""

show()








