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

def write_to_table(x,y,xname,yname,fout):
	result = pd.DataFrame({xname:x, yname:y})
	result.to_csv(fout,index=False)

##########
Emax_max = 100
Emax_min = 7.3
Emax_step = 0.1
Emax_num = int((Emax_max-Emax_min)/Emax_step)
Emax_array = np.linspace(Emax_min,Emax_max,Emax_num)
print(Emax_array)

Ecut_min = 3.0
Ecut_max = 10.0
Ecut_step = 0.1
Ecut_num = int((Ecut_max-Ecut_min)/Ecut_step)
Ecut_array = np.linspace(Ecut_min,Ecut_max,Ecut_num)
print(Ecut_array)

k_MeV = np.logspace(-3,2,500) # MeV

for Emax in Emax_array:
	for Ecut in Ecut_array:
		fout = 'out/table/thick_Emax%s_Ecut%s.dat' % (('%.3f'%Emax).replace('.','p'),('%.3f'%Ecut).replace('.','p'))
		print(Emax,Ecut,fout)
		y = np.array([bremsstrahlung_thicktarget_rreaelectron(Emax,Ecut,k) for k in k_MeV])
		write_to_table(k_MeV,y,'photon_energy','photon_flux',fout)


