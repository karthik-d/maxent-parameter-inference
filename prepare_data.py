import pandas as pd 
import numpy as np 
import os 

IN_FILE = os.path.join("./data/lacy_at_init_6.csv")
OUT_FILE = os.path.join("./data/lacy_at_init_6_gen.csv")


def bin_timepoints(trajectory):
	trajectory = np.array(trajectory)
	trajectory_binned = np.array([[
		10*i, 
		trajectory[np.argmin(np.abs(trajectory[:, 0] - 10*i)), 1]
		] for i in range(6)
	])
	return trajectory_binned


def get_binned_timepoint_data(filepath):
	# first column is the time step.
	# each row corresponds to specific time point. 
	data_df = pd.read_csv(filepath, index_col=None, header=None)
	trajectory = bin_timepoints(data_df.to_numpy()) 
	return trajectory


def add_noise_make_data(ref_trajectory, n_ecoli=1000):

	# ref_trajectory should be a n_timepoints x 2 matrix: time, value.
	# add standard normal noise to reference trajectory to generate synthetic data. 
	noise_matrix = np.random.normal(0, 1, size=(n_ecoli, ref_trajectory.shape[0]))
	data_matrix = np.array([ref_trajectory[:, 1] for _ in range(n_ecoli)]) + noise_matrix 
	pd.DataFrame(data_matrix).to_csv(OUT_FILE, index=False, header=False)


add_noise_make_data(get_binned_timepoint_data(IN_FILE))
	
