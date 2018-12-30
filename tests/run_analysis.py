#!/usr/bin/env python

import pandas as pd
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


Emax = 100.0 # MeV
Ecut = 7.3 # MeV
energy_MeV = np.logspace(-3,4,200) # MeV
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

def write_to_table(x,y,xname,yname,fout):
	result = pd.DataFrame({xname:x, yname:y})
	result.to_csv(fout)

k_MeV = np.logspace(-3,2,500) # MeV

plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))

y = np.array([bremsstrahlung_thicktarget_rreaelectron(10,7.3,k) for k in k_MeV])
plt.plot(k_MeV,y,label='Emax=10 MeV, Ecut=7.3 MeV')
write_to_table(k_MeV,y,'photon_energy','photon_flux','out/table/thick_rrea_Emax10MeV_Ecut7p3keV.dat')

y = np.array([bremsstrahlung_thicktarget_rreaelectron(20,7.3,k) for k in k_MeV])
plt.plot(k_MeV,y,label='Emax=20 MeV, Ecut=7.3 MeV')
write_to_table(k_MeV,y,'photon_energy','photon_flux','out/table/thick_rrea_Emax20MeV_Ecut7p3keV.dat')

y = np.array([bremsstrahlung_thicktarget_rreaelectron(30,7.3,k) for k in k_MeV])
plt.plot(k_MeV,y,label='Emax=30 MeV, Ecut=7.3 MeV')
write_to_table(k_MeV,y,'photon_energy','photon_flux','out/table/thick_rrea_Emax30MeV_Ecut7p3keV.dat')

y = np.array([bremsstrahlung_thicktarget_rreaelectron(40,7.3,k) for k in k_MeV])
plt.plot(k_MeV,y,label='Emax=40 MeV, Ecut=7.3 MeV')
write_to_table(k_MeV,y,'photon_energy','photon_flux','out/table/thick_rrea_Emax40MeV_Ecut7p3keV.dat')

axes.set_xlim(1e-3,1e+4)
#axes.set_ylim(1e-4,2.0)
axes.legend(loc='upper right')
axes.set_xlabel('Energy (MeV)')
axes.set_ylabel('Photon flux (AU)')
axes.set_xscale('log')
axes.set_yscale('log')
plt.savefig('bremss_rrea_Ecut7p3MeV.pdf')



plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))

y = np.array([bremsstrahlung_thicktarget_rreaelectron(10,4.5,k) for k in k_MeV])
plt.plot(k_MeV,y,label='Emax=10 MeV, Ecut=4.5 MeV')
write_to_table(k_MeV,y,'photon_energy','photon_flux','out/table/thick_rrea_Emax10MeV_Ecut4p5keV.dat')

y = np.array([bremsstrahlung_thicktarget_rreaelectron(20,4.5,k) for k in k_MeV])
plt.plot(k_MeV,y,label='Emax=20 MeV, Ecut=4.5 MeV')
write_to_table(k_MeV,y,'photon_energy','photon_flux','out/table/thick_rrea_Emax20MeV_Ecut4p5keV.dat')

y = np.array([bremsstrahlung_thicktarget_rreaelectron(30,4.5,k) for k in k_MeV])
plt.plot(k_MeV,y,label='Emax=30 MeV, Ecut=4.5 MeV')
write_to_table(k_MeV,y,'photon_energy','photon_flux','out/table/thick_rrea_Emax30MeV_Ecut4p5keV.dat')

y = np.array([bremsstrahlung_thicktarget_rreaelectron(40,4.5,k) for k in k_MeV])
plt.plot(k_MeV,y,label='Emax=40 MeV, Ecut=4.5 MeV')
write_to_table(k_MeV,y,'photon_energy','photon_flux','out/table/thick_rrea_Emax40MeV_Ecut4p5keV.dat')

axes.set_xlim(1e-3,1e+4)
#axes.set_ylim(1e-4,2.0)
axes.legend(loc='upper right')
axes.set_xlabel('Energy (MeV)')
axes.set_ylabel('Photon flux (AU)')
axes.set_xscale('log')
axes.set_yscale('log')
plt.savefig('bremss_rrea_Ecut4p5MeV.pdf')


exit()



k_MeV = np.logspace(-3,2,500) # MeV

#print(photon_flux_from_monoenergy_electron(eint=3.0,k=1.0))
#exit()

plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))
plt.plot(k_MeV,np.array([bremsstrahlung_thicktarget_monoelectron(20.0,k) for k in k_MeV]),label='Eint=20 MeV')
plt.plot(k_MeV,np.array([bremsstrahlung_thicktarget_monoelectron(1.0,k) for k in k_MeV]),label='Eint=1 MeV')
axes.set_xlim(1e-3,1e+4)
#axes.set_ylim(1e-4,2.0)
axes.legend(loc='upper right')
axes.set_xlabel('Energy (MeV)')
axes.set_ylabel('Photon flux (AU)')
axes.set_xscale('log')
axes.set_yscale('log')
plt.savefig('bremss2.pdf')

exit()




k_MeV = np.logspace(-3,2,200) # MeV

plt.clf()
fig, axes = plt.subplots(1,1,figsize=(8,6))
plt.plot(k_MeV,np.array([bremss_dsdk(e0=20.0,k=k) for k in k_MeV]),label='Eint=20 MeV')
plt.plot(k_MeV,np.array([bremss_dsdk(e0=10.0,k=k) for k in k_MeV]),label='Eint=10 MeV')
plt.plot(k_MeV,np.array([bremss_dsdk(e0=5.0,k=k) for k in k_MeV]),label='Eint=5 MeV')
plt.plot(k_MeV,np.array([bremss_dsdk(e0=1.0,k=k) for k in k_MeV]),label='Eint=1 MeV')
axes.set_xlim(1e-3,1e+4)
#axes.set_ylim(1e-4,2.0)
axes.legend(loc='upper right')
axes.set_xlabel('Energy (MeV)')
axes.set_ylabel('Photon flux (AU)')
axes.set_xscale('log')
axes.set_yscale('log')
plt.savefig('bremss.pdf')



