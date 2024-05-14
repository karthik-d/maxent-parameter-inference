import pandas as pd 
import numpy as np 
import os 


DATA_FILE = os.path.join("./data/lacy_at_init_36.csv")


def bin_timepoints(trajectory):
	trajectory = np.array(trajectory)
	trajectory_binned = np.array([[
		10*i, 
		trajectory[np.argmin(np.abs(trajectory[:, 0] - 10*i)), 1]
		] for i in range(6)
	])
	return trajectory_binned


# first column is the time step.
# each row corresponds to specific time point. 
data_df = pd.read_csv(DATA_FILE, index_col=None, header=None)
trajectory = bin_timepoints(data_df.to_numpy()) 
print(trajectory)