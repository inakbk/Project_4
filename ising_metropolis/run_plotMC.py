from pylab import *
import os as os

"""
------------------------------------------------------------------------------------------
"""
def exp_E_theory(T, N):
    return -8.*sinh(8./T)/(cosh(8./T) + 3)/N

def exp_E2_theory(T, N):
    return 64.*cosh(8./T)/(cosh(8./T) + 3)/N

def C_v_theory(T, N):
    return ( 64./(T*T) )*( 1 + 3*cosh(8./T) )/( (cosh(8./T) + 3)*(cosh(8./T) + 3) )/N

def exp_absM_theory(T, N):
    return 2.*(exp(8./T) + 2)/(cosh(8./T) + 3)/N

def exp_M2_theory(T, N):
    return 8*(exp(8./T) + 1)/(cosh(8./T) + 3)/N

def chi_theory(T, N):
    #return (8./T)*(exp(8./T) + 1)/(cosh(8./T) + 3) #this one is only working for small L
    return (4./T)*( ( 2*(exp(8./T) + 1)*(cosh(8./T) + 3) - (exp(8./T) + 2)**2 )/( cosh(8./T) + 3 )**2 )/N

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

L = 2
N = L**2
max_nr_of_cycles = 50000 #must delelig 10
initial = -1
error_plot = True

#compiling once:
#os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include -O3 -std=c++11')

Tcount = 100
os.system('./main %s %s %s %s %s' %(T, L, max_nr_of_cycles, initial, Tcount))
filename = 'metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, Tcount, initial, max_nr_of_cycles)
cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)

#plot against MC cycles:

if error_plot == False:
    figure(1)
    plot(cycles, mean_E)
    hold('on')
    plot(cycles, exp_E_theory(T,N)*ones(len(cycles)))
    title('mean_E, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('MC cycles')
    ylabel('mean_E')

    figure(2)
    plot(cycles, mean_E2)
    hold('on')
    plot(cycles, exp_E2_theory(T,N)*ones(len(cycles)))
    title('mean_E2, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('MC cycles')
    ylabel('mean_E2')

    figure(3)
    plot(cycles, C_v)
    hold('on')
    plot(cycles, C_v_theory(T,N)*ones(len(cycles)))
    title('C_v, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('MC cycles')
    ylabel('C_v')

    figure(4)
    plot(cycles, mean_absM)
    hold('on')
    plot(cycles, exp_absM_theory(T,N)*ones(len(cycles)))
    title('mean_absM, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('MC cycles')
    ylabel('mean_absM')

    figure(5)
    plot(cycles, mean_M2)
    hold('on')
    plot(cycles, exp_M2_theory(T,N)*ones(len(cycles)))
    title('mean_M2, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('MC cycles')
    ylabel('mean_M2')

    figure(6)
    plot(cycles, chi)
    hold('on')
    plot(cycles, chi_theory(T,N)*ones(len(cycles)))
    title('chi, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('MC cycles')
    ylabel('chi')

if error_plot == True:
    figure(1)
    plot(cycles, abs(mean_E - exp_E_theory(T,N)))
    title('error mean_E, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    xlabel('MC cycles')
    ylabel('error')

    figure(2)
    plot(cycles, abs(mean_E2 - exp_E2_theory(T,N)*ones(len(cycles))))
    title('error mean_E2, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    xlabel('MC cycles')
    ylabel('error')

    figure(3)
    plot(cycles, abs(C_v - C_v_theory(T,N)*ones(len(cycles))))
    title('error C_v, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    xlabel('MC cycles')
    ylabel('error')

    figure(4)
    plot(cycles, abs(mean_absM - exp_absM_theory(T,N)*ones(len(cycles))))
    title('error mean_absM, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    xlabel('MC cycles')
    ylabel('error')

    figure(5)
    plot(cycles, abs(mean_M2 - exp_M2_theory(T,N)*ones(len(cycles))))
    title('error mean_M2, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    xlabel('MC cycles')
    ylabel('error')

    figure(6)
    plot(cycles, abs(chi - chi_theory(T,N)*ones(len(cycles))))
    title('error chi, T= %s \n #MCcycles= %s, L= %s, initial_state=%s' %(T, max_nr_of_cycles, L, initial))
    xlabel('MC cycles')
    ylabel('error')

show()








