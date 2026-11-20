import scipy.integrate as sp
import radioactivedecay as rd
import math
import matplotlib.pyplot as plt

NA = 6.022E+23
isotope_list = ['Ce-134', 'La-134', 'Ba-134']


def decay_eqns(t, atoms, lambda_ce, lambda_la):
    '''
    Args:
    t: independent variable, time in hours
    atoms: dependent variables, atom counts for Ce-134, La-134, and Ba-134
    lambda_ce: decay constant for the parent Ce-134, in inverse hours
    lambda_la: decay constant for the first daughter La-134, in inverse hours

    Returns:
    (d_Ce, d_La, d_Ba): tuple of all right hand sides of the coupled ODEs,
    in atoms per hour, when set up as dy/dt = f(y, t)

    Right hand sides of all coupled ODEs when set up as dy/dt = f(y, t).
    This function is used as input into the built-in ODE solver, solve_ivp.
    '''
    N_ce, N_la, N_ba = atoms

    d_Ce = -lambda_ce * N_ce
    d_La = lambda_ce * N_ce - lambda_la * N_la
    d_Ba = lambda_la * N_la

    return (d_Ce, d_La, d_Ba)


def initial_val(isotope):
    '''
    Args:
    isotope: string identifier for an isotope, such as 'Ce-134'

    Returns:
    N_0: initial number of atoms of the isotope
    lambda_A: decay constant of the isotope, in inverse hours

    Calculates the initial atom count and decay constant using radioactivedecay.
    The initial masses are 0.01 g of Ce-134 and zero La-134 and Ba-134.
    This function has no side effects.
    '''
    iso = rd.Nuclide(isotope)
    lambda_A = math.log(2) / iso.half_life('h')

    if iso.nuclide == 'Ce-134':
        N_0 = (0.01 / iso.atomic_mass) * NA
    else:
        N_0 = 0

    return N_0, lambda_A


def main(t_input):
    '''
    Args:
    t_input: time in days, between 0 and 30, at which to return atom counts

    Returns:
    atoms_at_input: array of Ce-134, La-134, and Ba-134 atom counts at t_input

    Solves the coupled ODEs from 0 to 720 hours using initial_val and decay_eqns.
    Displays three separate plots with linear axes, one for each isotope.
    Close all plot windows to continue to the returned atom counts.
    If the savefig lines are enabled, also saves each plot as a 300 dpi PNG.
    '''

    t_solutions = []
    lambda_atoms = []
    initial_atoms = []

    for i in range(1, 721, 2):
        t_solutions.append(i)

    for iso in isotope_list:
        N_0, lambda_A = initial_val(iso)
        initial_atoms.append(N_0)
        lambda_atoms.append(lambda_A)

    solutions = sp.solve_ivp(
        fun=decay_eqns,
        t_span=(0, 720),
        y0=initial_atoms,
        t_eval=t_solutions,
        args=tuple(lambda_atoms[:2]),
        dense_output=True,
    )


    atoms_at_input = solutions.sol(t_input * 24)

    ''' Plotting solution to system of ODEs below '''

    # Font properties for the axis labels.
    font = {'family': 'arial',
            'color': 'black',
            'weight': 'normal',
            'size': 12,
            }

    # Plot Ce-134 on its own linear axes, including the initial value.
    plt.figure()
    plt.plot(solutions.t, solutions.y[0], color = 'mediumseagreen', linestyle ='-', marker = '.')
    plt.xlabel('Time (h)', fontdict = font, labelpad=8)
    plt.ylabel('Number of Atoms', fontdict=font, labelpad=8)
    plt.title('Ce-134', fontdict=font)
    plt.yscale('linear')
    plt.ylim(bottom=0)
    plt.legend(['Ce-134'], ncol=1, edgecolor='black', loc='upper right', fontsize=10)
    plt.tick_params(axis="both",direction="in", labelsize = 12)
    plt.tight_layout()
    plt.savefig('CeLa-134_Decay_Ashik_Ce-134.png', dpi=300)

    # Plot La-134 on its own linear axes to make its smaller population visible.
    plt.figure()
    plt.plot(solutions.t, solutions.y[1], color = 'mediumorchid', linestyle ='-', marker = '.')
    plt.xlabel('Time (h)', fontdict = font, labelpad=8)
    plt.ylabel('Number of Atoms', fontdict=font, labelpad=8)
    plt.title('La-134', fontdict=font)
    plt.yscale('linear')
    plt.ylim(bottom=0)
    plt.legend(['La-134'], ncol=1, edgecolor='black', loc='upper right', fontsize=10)
    plt.tick_params(axis="both",direction="in", labelsize = 12)
    plt.tight_layout()
    plt.savefig('CeLa-134_Decay_Ashik_La-134.png', dpi=300)

    # Plot stable Ba-134 accumulating on its own linear axes.
    plt.figure()
    plt.plot(solutions.t, solutions.y[2], color = 'cornflowerblue', linestyle ='-', marker = '.')
    plt.xlabel('Time (h)', fontdict = font, labelpad=8)
    plt.ylabel('Number of Atoms', fontdict=font, labelpad=8)
    plt.title('Ba-134', fontdict=font)
    plt.yscale('linear')
    plt.ylim(bottom=0)
    plt.legend(['Ba-134'], ncol=1, edgecolor='black', loc='lower right', fontsize=10)
    plt.tick_params(axis="both",direction="in", labelsize = 12)
    plt.tight_layout()
    plt.savefig('CeLa-134_Decay_Ashik_Ba-134.png', dpi=300)

    # Uncomment the savefig lines above to save all three plots at 300 dpi.
    plt.show()

    return atoms_at_input



lambda_ce = initial_val('Ce-134')[1]
lambda_la = initial_val('La-134')[1]

# For initially absent La, its maximum occurs when production = decay.
t_peak_hours = math.log(lambda_la / lambda_ce) / (lambda_la - lambda_ce)
t_peak_days = t_peak_hours / 24

print(f'La-134 peak time: {t_peak_days:.8f} days '
      f'({t_peak_hours:.6f} hours)')
peak_atoms = main(t_peak_days)
print('Atom counts at the La-134 peak:')
for isotope, atom_count in zip(isotope_list, peak_atoms):
    print(f'{isotope}: {atom_count:.6e} atoms')
