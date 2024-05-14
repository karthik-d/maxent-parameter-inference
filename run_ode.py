import matlab.engine
# import numpy as np

rho = 167.1
beta_g = 65.0
n = 2.0
lacy_init = 36.0

eng = matlab.engine.start_matlab()
val = eng.lac_system_ode_trajectory(rho, beta_g, n, lacy_init)
