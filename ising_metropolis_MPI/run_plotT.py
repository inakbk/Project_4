from pylab import *
import os as os

"""
------------------------------------------------------------------------------------------
"""
def read_file(filename):
    infile = open(filename, "r")
    all_lines = infile.readlines()
    infile.close()

    T = zeros(len(all_lines)/10)
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
        T[i] = all_lines[8+i].split()[1]
        #--- on all_lines[9+i].split()[1]
        i += 10
        j += 1

    return T, nr_of_cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi

"""
------------------------------------------------------------------------------------------
"""

Tcount = 21
L = 40
max_nr_of_cycles = 500000 #must delelig 10

N = L**2
initial = 1
plot_exp_val = True

T_plot = zeros(Tcount)
nr_of_accepted_config_plot = zeros(Tcount)
mean_E_plot = zeros(Tcount)
mean_E2_plot = zeros(Tcount)
C_v_plot = zeros(Tcount)
mean_absM_plot = zeros(Tcount)
mean_M2_plot = zeros(Tcount)
chi_plot = zeros(Tcount)

for i in range(Tcount):
    filename = 'Tcount20/metropolis_L%s_Tcount%s_initial%s_MC%s.txt' %(L, i, initial, max_nr_of_cycles)
    T_in_loop, cycles, nr_of_accepted_config, mean_E, mean_E2, C_v, mean_absM, mean_M2, chi = read_file(filename)   

    T_plot[i] = T_in_loop[-1]
    nr_of_accepted_config_plot[i] = nr_of_accepted_config[-1]
    mean_E_plot[i] = mean_E[-1]
    mean_E2_plot[i] = mean_E2[-1]
    C_v_plot[i] = C_v[-1]
    mean_absM_plot[i] = mean_absM[-1]
    mean_M2_plot[i] = mean_M2[-1]
    chi_plot[i] = chi[-1]

"""
------------------------------------------------------------------------------------------
"""

if plot_exp_val == False:
    figure(1)
    plot(T_plot, nr_of_accepted_config_plot)
    title('Number of accepted cycles \n #MCcycles= %s, L= %s, initial_state=%s' %(max_nr_of_cycles, L, initial))
    xlabel('temp')
    ylabel('nr of accepted config')

if plot_exp_val == True:
    figure(1)
    plot(T_plot, mean_E_plot, '-o')
    title('mean_E\n #MCcycles= %s, L= %s, initial_state=%s' %(max_nr_of_cycles, L, initial))
    xlabel('T_plot')
    ylabel('exp E')
    """
    figure(2)
    plot(T_plot, mean_E2_plot, '-o')
    title('mean_E2\n #MCcycles= %s, L= %s, initial_state=%s' %(max_nr_of_cycles, L, initial))
    xlabel('T_plot')
    ylabel('exp E2')
    """
    figure(3)
    plot(T_plot, C_v_plot, '-o')
    title('C_v\n #MCcycles= %s, L= %s, initial_state=%s' %(max_nr_of_cycles, L, initial))
    xlabel('T_plot')
    ylabel('C_v')

    figure(4)
    plot(T_plot, mean_absM_plot, '-o')
    title('mean_absM\n #MCcycles= %s, L= %s, initial_state=%s' %(max_nr_of_cycles, L, initial))
    xlabel('T_plot')
    ylabel('exp abs M')
    """
    figure(5)
    plot(T_plot, mean_M2_plot, '-o')
    title('mean_M2\n #MCcycles= %s, L= %s, initial_state=%s' %(max_nr_of_cycles, L, initial))
    xlabel('T_plot')
    ylabel('exp M2')
    """
    figure(6)
    plot(T_plot, chi_plot, '-o')
    title('chi\n #MCcycles= %s, L= %s, initial_state=%s' %(max_nr_of_cycles, L, initial))
    xlabel('T_plot')
    ylabel('chi')

show()








