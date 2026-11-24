import scipy.integrate as sp
import matplotlib.pyplot as plt

initial_atoms = (0,0)
gamma_pm = 0.0108
Sigma_f = 4.819E22 * 585E-24
phi = 1E14
lambda_pm = 0.013054 / 3600
sigma_sm = 4.1E4 * 1E-24

def ODE_system(t, atoms, gamma_pm, Sigma_f, phi, lambda_pm, sigma_sm):
    
    (N_pm, N_sm) = atoms
    d_pm = gamma_pm * Sigma_f * phi - lambda_pm * N_pm
    d_sm = lambda_pm * N_pm - N_sm * phi * sigma_sm

    return d_pm, d_sm

def main(factor):
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