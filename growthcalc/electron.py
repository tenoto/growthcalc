"""
Physical process related to electrons.

Bethe-Bloch stopping power is descfribed in the "Radiation Detection and Measurement 4th Edition" by Glenn F. Knowll (S2.2.1)
and also "Particle Data Group (PDG) Passage of particles through matter" 
http://pdg.lbl.gov/2018/reviews/rpp2018-rev-passage-particles-matter.pdf

However, here we use the table downlaoded from the NIST website.
"""

#import numpy as np
import pandas as pd
from scipy.interpolate import interp1d 

NIST_DEDX_TABLE = "growthcalc/data/nist_estar_e_stopping.dat"

df_NIST_DEDX_TABLE = pd.read_table(NIST_DEDX_TABLE,
	skiprows=[0,1,2,3,4,5,6,7],header=None,
	names=['Kinetic Energy','Collision Stp. Pow.','Radiative Stp. Pow.','Total Stp. Pow.','D. Effect'])
interp_dEdx_total = interp1d(df_NIST_DEDX_TABLE['Kinetic Energy'],df_NIST_DEDX_TABLE['Total Stp. Pow.']) # MeV, MeV cm2/g
interp_dEdx_collision = interp1d(df_NIST_DEDX_TABLE['Kinetic Energy'],df_NIST_DEDX_TABLE['Collision Stp. Pow.']) # MeV, MeV cm2/g
interp_dEdx_radiative = interp1d(df_NIST_DEDX_TABLE['Kinetic Energy'],df_NIST_DEDX_TABLE['Radiative Stp. Pow.']) # MeV, MeV cm2/g

