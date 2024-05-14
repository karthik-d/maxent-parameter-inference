from matplotlib import pyplot as plot
from sklearn import metrics
import pandas as pd
import numpy as np 
import os


REF_FILE = os.path.join("./data/lacy_at_init_6.csv")
DATA_FILE = os.path.join("./data/lacy_at_init_6_gen.csv")


def bin_timepoints(trajectory):
	trajectory = np.array(trajectory)
	trajectory_binned = np.array([[
		5*i, 
		trajectory[np.argmin(np.abs(trajectory[:, 0] - 5*i)), 1]
		] for i in range(6)
	])
	return trajectory_binned


def get_binned_timepoint_data(filepath):
	# first column is the time step.
	# each row corresponds to specific time point. 
	data_df = pd.read_csv(filepath, index_col=None, header=None)
	trajectory = bin_timepoints(data_df.to_numpy()) 
	return trajectory


ref_trajectory = get_binned_timepoint_data(REF_FILE)
obs_data = pd.read_csv(DATA_FILE, header=None)

prediction = obs_data.sample(n=1).to_numpy().flatten()

rmse = metrics.mean_squared_error(ref_trajectory[:, 1], prediction)**0.5

plot.plot(ref_trajectory[:, 0], ref_trajectory[:, 1], '-bo', label='reference')
plot.plot(ref_trajectory[:, 0], prediction, '--ro', label='prediction')
plot.title(f"LacY Init = 6uM | RMSE = {round(rmse, 2)} uM")
plot.xlabel('Time Points')
plot.ylabel('LacY Concentration (uM)')
plot.show()