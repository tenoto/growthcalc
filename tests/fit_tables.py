#!/usr/bin/env python

import pandas as pd
import numpy as np
import scipy
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

df = pd.read_csv('out/table/thick_rrea_Emax40MeV_Ecut7p3keV.dat')
#print(df)

parameter_initial = np.array([50.0, 1.0, 7.3]) #a, b, c
def cutoff_powerlaw(x, N, index, Ecut):
    return N * x ** (-index) * np.exp(-x/Ecut)

xmin = 1.0
xmax = 8.0

filter_range = np.logical_and(df['photon_energy']>xmin,df['photon_energy'] <= xmax)

paramater_optimal, covariance = scipy.optimize.curve_fit(
	cutoff_powerlaw, 
	df['photon_energy'][filter_range],
	df['photon_flux'][filter_range], p0=parameter_initial)    
print(paramater_optimal)
y = cutoff_powerlaw(df['photon_energy'],paramater_optimal[0],paramater_optimal[1],paramater_optimal[2])

plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))
plt.plot(df['photon_energy'],df['photon_flux'],label='Emax:20 MeV, Ecut:7.3 MeV')
plt.plot(df['photon_energy'],y,label='fit')
axes.set_xlim(1e-3,1e+4)
#axes.set_ylim(1e-4,2.0)
axes.legend(loc='upper right')
axes.set_xlabel('Energy (MeV)')
axes.set_ylabel('Photon flux (AU)')
axes.set_xscale('log')
axes.set_yscale('log')
plt.savefig('fit.pdf')
