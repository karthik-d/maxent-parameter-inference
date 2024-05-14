import matlab.engine
import tensorflow as tf
import pandas as pd
import numpy as np
import maxent
import os

from prepare_data import get_binned_timepoint_data, bin_timepoints

REF_FILE = os.path.join("./data/lacy_at_init_36.csv")
DATA_FILE = os.path.join("./data/lacy_at_init_36_gen.csv")

"""
rho = 167.1
beta_g = 65.0
n = 2.0
lacy_init = 36.0
"""

# start matlab engine.
# eng = matlab.engine.start_matlab()

# get and prepare observation data.
ref_trajectory = get_binned_timepoint_data(REF_FILE)[:, 0]
obs_data = pd.read_csv(DATA_FILE, header=None).to_numpy()

# prepare MaxEnt restraint per timepoint.
restraints_l = [
	maxent.Restraint(lambda traj, idx=idx: traj[idx], target=ref_trajectory[idx])
	for idx in range(len(ref_trajectory))
]

# create model by passing in restraints.
model = maxent.MaxentModel(restraints_l)
model.compile(tf.keras.optimizers.Adam(1e-4), "mean_squared_error")
# short burn-in
h = model.fit(obs_data, epochs=500, steps_per_epoch=1000/32)
# maxent weights.
maxent_weights = model.traj_weights
np.savetxt("maxent_traj_weights.txt", maxent_weights)

