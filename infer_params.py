import matlab.engine
import pandas as pd
import numpy as np
import maxent
import os

from .prepare_data import get_timepoint_data, bin_timepoints

DATA_FILE = os.path.join("./data/lacy_at_init_36.csv")

"""
rho = 167.1
beta_g = 65.0
n = 2.0
lacy_init = 36.0
"""

def restraint(rho, beta_g, n, lacy_init, t):
	predicted_traj = eng.lac_system_ode_trajectory(rho, beta_g, n, lacy_init)
	predicted_traj = bin_timepoints(predicted_traj)


# start matlab engine.
eng = matlab.engine.start_matlab()

# get and prepare observation data.
obs_trajectory = get_binned_timepoint_data(DATA_FILE)

# prepare MaxEnt restraint per timepoint.
restraints_l = [
	maxent.Restraint(lambda traj: traj[-1,0], target=2)
]
rx = 
ry = maxent.Restraint(lambda traj: traj[-1,1], target=1)

# create model by passing in restraints.
model = maxent.MaxentModel([rx, ry])
