function trajectory = lac_system_ode_trajectory(rho, beta_g, n, lacy_init)

	consts.glu = 50;
	consts.tmg_e = 80;
	% total LacI conc.
	consts.rT = 0.4e-3;

	% model params.
	params.rho = rho;
	params.beta_g = beta_g;
	params.n = 2;

	% time duration.
	consts.tmax = 50;
	% get ODE functions.
	ode_funcs = lac_system_ode;
	% initial concentrations.
	consts.y_init = [0; lacy_init];

	% solve ODE.
	disp("solving ode");
	[ode_tout, x] = ode45(@(t,y) ode_funcs.dydt(t, y, consts, params), [0; consts.tmax], consts.y_init);
	% disp("ode solved");

	% package for exporting to python.
	ode_lacy = x(:, 2);
	trajectory = cat(2, ode_tout, ode_lacy);

end