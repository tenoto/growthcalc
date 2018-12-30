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

energy_MeV = np.logspace(-3,4,100) # MeV

plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))
plt.plot(energy_MeV,interp_dEdx_total(energy_MeV),label='Total')
plt.plot(energy_MeV,interp_dEdx_collision(energy_MeV),label='Collision')
plt.plot(energy_MeV,interp_dEdx_radiative(energy_MeV),label='Radiative')
axes.set_xlim(1e-3,1e+4)
axes.set_ylim(1,80)
#axes.legend(loc='upper right')
axes.set_xlabel('Energy (MeV)')
axes.set_ylabel('Stopping Power (MeV cm$^2$/g)')
axes.set_xscale('log')
axes.set_yscale('log')
plt.savefig('stopping_power_nist_air_MeVcm2g-1.pdf')


AIR_DENSITY = 1.293e-3 # g / cm3

plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))
plt.plot(energy_MeV,AIR_DENSITY*interp_dEdx_total(energy_MeV),label='Total')
plt.plot(energy_MeV,AIR_DENSITY*interp_dEdx_collision(energy_MeV),label='Collision')
plt.plot(energy_MeV,AIR_DENSITY*interp_dEdx_radiative(energy_MeV),label='Radiative')
plt.plot(energy_MeV,bethebloch_radiative(energy_MeV),label='Bethe-Bloch')
axes.set_xlim(1e-3,1e+4)
#axes.set_ylim(1,80)
#axes.legend(loc='upper right')
axes.set_xlabel('Energy (MeV)')
axes.set_ylabel('Stopping Power (MeV / cm)')
axes.set_xscale('log')
axes.set_yscale('log')
plt.savefig('stopping_power_nist_air_MeVcm-1.pdf')