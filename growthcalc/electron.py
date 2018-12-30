"""
Physical process related to electrons.

Bethe-Bloch stopping power is descfribed in the "Radiation Detection and Measurement 4th Edition" by Glenn F. Knowll (S2.2.1)
and also "Particle Data Group (PDG) Passage of particles through matter" 
http://pdg.lbl.gov/2018/reviews/rpp2018-rev-passage-particles-matter.pdf

However, here we use the table downlaoded from the NIST website.
"""

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d 
from scipy.integrate import quad

mec2_MeV = 0.511 # MeV
NUMBER_DENSITY_OF_AIR = 0.02504e+21 # cm-3
# https://en.wikipedia.org/wiki/Number_density
AVERAGE_Z_OF_AIR = 7.22 # 7*0.78+8*(1-0.78)
# https://core.ac.uk/download/pdf/39720756.pdf

### Bethe-Bloch energy loss functions from NIST
NIST_DEDX_TABLE = "growthcalc/data/nist_estar_e_stopping.dat"

df_NIST_DEDX_TABLE = pd.read_table(NIST_DEDX_TABLE,
	skiprows=[0,1,2,3,4,5,6,7],header=None,
	names=['Kinetic Energy','Collision Stp. Pow.','Radiative Stp. Pow.','Total Stp. Pow.','D. Effect'])
interp_dEdx_total = interp1d(df_NIST_DEDX_TABLE['Kinetic Energy'],df_NIST_DEDX_TABLE['Total Stp. Pow.']) # MeV, MeV cm2/g
interp_dEdx_collision = interp1d(df_NIST_DEDX_TABLE['Kinetic Energy'],df_NIST_DEDX_TABLE['Collision Stp. Pow.']) # MeV, MeV cm2/g
interp_dEdx_radiative = interp1d(df_NIST_DEDX_TABLE['Kinetic Energy'],df_NIST_DEDX_TABLE['Radiative Stp. Pow.']) # MeV, MeV cm2/g

### Bethe-Bloch from equation 
def bethebloch_radiative(energy_MeV,Z=AVERAGE_Z_OF_AIR,N=1,q=1):
	"""
	b : beta 
	"""
	g = energy_MeV / mec2_MeV
	b = np.sqrt(1.0-1.0/g*g)
	term2 = 0.0
	return term2

def bethebloch_collision(energy_MeV,Z=AVERAGE_Z_OF_AIR,N=1,q=1):
	"""
	g : Lorentz factor
	"""
	g = energy_MeV / mec2_MeV
	return N * q**2 * g * Z * (Z+1) / 137.0  * (4 * np.log(2*g) - 3.0/4.0)

### Bremsstrahlung cross section
def bremss_dsdk(electron_MeV,photon_MeV,Z=AVERAGE_Z_OF_AIR):
	"""
	e0 : initial energy E0 = e0 m_e c^2 
	k  : photon energy k m_e c^2
	e1 : final energy 
	Z_air = 7.22#7*0.78+8*(1-0.78)
	"""
	e0 = electron_MeV / mec2_MeV
	k  = photon_MeV / mec2_MeV
	e1 = e0 - k # m_e c^2 unit 
	if e1 <= 0.0:
		return 0.0
	else:
		b = 2.0 * e0 * e1 * Z**(1.0/3.0) / 111.0 / k
		inverse_M0 = (k/(2.0 * e0 * e1))**2 + (Z**(-1.0/3.0)/111.0)**2
		term1 = 2.0 * Z**2 / 137.0 / k # r_e is needed. 
		term2 = (1 + (e1/e0)**2 -2.0*e1/3.0/e0) 
		term3 = (np.log(1.0/inverse_M0)+1-2/b*np.arctan(b))
		term4 = e1/e0 * (2.0/b**2 * np.log(1+b**2) + 4.0*(2.0-b**2)/(3*b**3)*np.arctan(b)-8.0/3.0/b**2+2.0/9.0)
		return term1 * (term2 * term3 + term4)

def bremsstrahlung_thicktarget_monoelectron(electron_MeV,photon_MeV,integrate_Nstep=500):
	eint = electron_MeV / mec2_MeV
	k = photon_MeV / mec2_MeV	
	if k >= eint:
		return 0.0
	else:
		tmp_energy_array = np.linspace(k+1,eint,integrate_Nstep)
		destep = (eint-(k+1))*mec2_MeV/float(integrate_Nstep) # MeV
		tmp_function_array = np.array([bremss_dsdk(i*mec2_MeV,k*mec2_MeV)/interp_dEdx_total(i*mec2_MeV) for i in tmp_energy_array])
		return np.sum(tmp_function_array)*destep

def bremsstrahlung_thicktarget_rreaelectron(electron_Emax,electron_Ecut,photon_MeV,integrate_Nstep=20):
	k = photon_MeV / mec2_MeV	
	electron_MeV = np.linspace((k+1)*mec2_MeV,electron_Emax,integrate_Nstep) # MeV
	destep = (electron_Emax-(k+1))*mec2_MeV/float(integrate_Nstep) # MeV
	Ne = np.piecewise(electron_MeV, [electron_MeV<=electron_Emax, electron_MeV>electron_Emax],[lambda x: np.exp(-x/electron_Ecut), 0])
	Pe = np.array([bremsstrahlung_thicktarget_monoelectron(Ee,photon_MeV,integrate_Nstep) for Ee in electron_MeV])
	return np.sum(Pe * Ne) * destep

