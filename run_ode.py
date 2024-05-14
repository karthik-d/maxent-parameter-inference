import matlab.engine
import numpy as np

rho = 167.1
beta_g = 65.0
n = 2.0
lacy_init = 36.0


eng = matlab.engine.start_matlab()
trajectory = eng.lac_system_ode_trajectory(rho, beta_g, n, lacy_init)


# extract 6 time points only: 0, 10, ..., 50.
def bin_timepoints(trajectory):
	trajectory = np.array(trajectory)
	print(trajectory.shape)

	trajectory_binned = np.array([[
		10*i, 
		trajectory[np.argmin(np.abs(trajectory[:, 0] - 10*i)), 1]
		] for i in range(6)
	])
	return trajectory_binned