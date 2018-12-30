#!/usr/bin/env python

import numpy as np
from growthcalc.electron import *

import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = '14'
mpl.rcParams['mathtext.default'] = 'regular'
mpl.rcParams['xtick.top'] = 'True'
mpl.rcParams['ytick.right'] = 'True'
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
#mpl.rcParams['axes.grid'] = 'True'
mpl.rcParams['axes.xmargin'] = '.05' #'.05'
mpl.rcParams['axes.ymargin'] = '.05'
mpl.rcParams['savefig.facecolor'] = 'None'
mpl.rcParams['savefig.edgecolor'] = 'None'
mpl.rcParams['savefig.bbox'] = 'tight'

Emin_hard = 0.1 # MeV
Emax_hard = 100.0 # MeV
Estep_hard = 0.1 # MeV
Nstep = int((Emax_hard-Emin_hard)/Estep_hard)
print(Nstep)

energy_MeV = np.linspace(Emin_hard,Emax_hard,Nstep)
print(energy_MeV)


exit()
Emax = 100.0 # MeV
Ecut = 7.3 # MeV

Ne = np.piecewise(energy_MeV, [energy_MeV<=Emax, energy_MeV>Emax],[lambda x: np.exp(-x/Ecut), 0])

plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))
plt.plot(energy_MeV,Ne,label='Total')
axes.set_xlim(1e-3,1e+4)
axes.set_ylim(1e-4,2.0)
#axes.legend(loc='upper right')
axes.set_xlabel('Energy (MeV)')
axes.set_ylabel('Intrinsic electron number (AU)')
axes.set_xscale('log')
axes.set_yscale('log')
plt.savefig('intrinsic_electron_energy.pdf')

