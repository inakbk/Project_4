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

T = linspace(1,9,10)

L = 2
N = L**2
max_nr_of_cycles = 10000 #must delelig 10
initial = 1
error_plot = False

#compiling once:
os.system('g++ -o main *.cpp -larmadillo -llapack -lblas -L/usr/local/lib -I/usr/local/include -O3 -std=c++11')

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

#plot against T:
#Everything is per spin!

if error_plot == False:
    figure(1)
    plot(T, mean_E_plot)
    hold('on')
    plot(T, exp_E_theory(T,N))
    title('mean_E, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('T')
    ylabel('exp E')

    figure(2)
    plot(T, mean_E2_plot)
    hold('on')
    plot(T, exp_E2_theory(T,N))
    title('mean_E2, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('T')
    ylabel('exp E2')

    figure(3)
    plot(T, C_v_plot)
    hold('on')
    plot(T, C_v_theory(T,N))
    title('C_v, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('T')
    ylabel('C_v')

    figure(4)
    plot(T, mean_absM_plot)
    hold('on')
    plot(T, exp_absM_theory(T,N))
    title('mean_absM, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('T')
    ylabel('exp abs M')

    figure(5)
    plot(T, mean_M2_plot)
    hold('on')
    plot(T, exp_M2_theory(T,N))
    title('mean_M2, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('T')
    ylabel('exp M2')

    figure(6)
    plot(T, chi_plot)
    hold('on')
    plot(T, chi_theory(T,N))
    title('chi, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    legend(['numerical', 'theory'])
    xlabel('T')
    ylabel('chi')

if error_plot ==True:
    figure(1)
    plot(T, abs(mean_E_plot - exp_E_theory(T,N)))
    title('error mean_E, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    xlabel('T')
    ylabel('error')

    figure(2)
    plot(T, abs(mean_E2_plot - exp_E2_theory(T,N)))
    title('error mean_E2, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    xlabel('T')
    ylabel('error')

    figure(3)
    plot(T, abs(C_v_plot - C_v_theory(T,N)))
    title('error C_v, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    xlabel('T')
    ylabel('error')

    figure(4)
    plot(T, abs(mean_absM_plot - exp_absM_theory(T,N)))
    title('error mean_absM, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    xlabel('T')
    ylabel('error')

    figure(5)
    plot(T, abs(mean_M2_plot - exp_M2_theory(T,N)))
    title('error mean_M2, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    xlabel('T')
    ylabel('error')

    figure(6)
    plot(T, abs(chi_plot - chi_theory(T,N)))
    title('error chi, temp range: [%s,%s] \n #MCcycles= %s, L= %s, initial_state=%s' %(T[0],T[-1], max_nr_of_cycles, L, initial))
    xlabel('T')
    ylabel('error')

show()








