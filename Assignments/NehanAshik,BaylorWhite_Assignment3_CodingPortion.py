import scipy.integrate as sp
import matplotlib.pyplot as plt

initial_atoms = (0,0) # initial concentrations of Pm-149 and Sm-149
gamma_pm = 0.0108
Sigma_f = 4.819E22 * 585E-24 
phi = 1E14
lambda_pm = 0.013054 / 3600 # decay constant converted from h-1 to s-1
sigma_sm = 4.1E4 * 1E-24

def ODE_system(t, atoms, gamma_pm, Sigma_f, phi, lambda_pm, sigma_sm):
    '''
        Args:
        t: independent variable
        atoms: dependent variable
        gamma_pm: Yield of Pm-149
        Sigma_f: Fission cross-section
        phi: Neutron Flux (cm2/s)
        lambda_pm: decay constant of Pm-149 (s-1)
        sigma_sm: neutron absorption cross section of Sm-149 (cm2)
        
        Returns:
        d_pm: Pm-149 concentration
        d_sm: Sm-149 concentration
        
        Right-hand side of all coupled ODE's when set up as dy/dt = f(y, t).
        This is used as input into the built-in ODE solver, solve_ivp.
        '''
    (N_pm, N_sm) = atoms
    d_pm = gamma_pm * Sigma_f * phi - lambda_pm * N_pm
    d_sm = lambda_pm * N_pm - N_sm * phi * sigma_sm

    return d_pm, d_sm

def main(factor):
    '''
    Args:
    factor: multiplies the neutron flux by the factor 
            to generate a plot of the modified neutron flux

    solves the ODEs using the solve_ivp function
    and plots the resulting isotope concentration

    '''
    t_solutions = []
    for i in range(0, 3600 * 24 * 7 * 3, 3600):
        t_solutions.append(i)

    for phi_new in [phi, factor*phi]:
        solutions = sp.solve_ivp(
                fun=ODE_system,
                t_span=(0, 3600 * 24 * 7 * 3),
                y0=initial_atoms,
                t_eval=t_solutions,
                args=(gamma_pm, Sigma_f, phi_new, lambda_pm, sigma_sm),
                dense_output=True,
            )

        #use solid lines for original flux and dashed lines for modified flux
        if phi_new == phi:
            style = '-'
        else:
            style = '--'

        plt.plot(solutions.t, solutions.y[0],
                 color = 'blue',
                 linestyle = style,
                 label = f'Pm-149 ({phi_new:.0e})')
        plt.plot(solutions.t, solutions.y[1],
                 color = 'orange',
                 linestyle = style,
                 label = f'Sm-149 ({phi_new:.0e})')

    plt.xlabel('Time (s)')
    plt.ylabel('Isotope Concentration (atoms/m3)')
    plt.title('Effect of neutron flux on isotope concentrations')
    plt.legend()

    plt.savefig('Flux_comparison_NehanAshik,BaylorWhite.png', dpi=300)
    plt.show()

factor = int(input("Enter factor by which neutron flux should be modified: "))

main(factor)