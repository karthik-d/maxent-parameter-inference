function x = lac_system_ode_solve

	consts.glu = 50;
	consts.tmg_e = 80;

	% total LacI conc.
	consts.rT = 0.4e-3;

	% model params.
	params.rho = 167.1;
	params.beta_g = 65;
	params.n = 2;

	% time duration.
	consts.tmax = 50;

	% get ODE functions.
	ode_funcs = lac_system_ode;

	figure; hold on; zoom on;
	% initial concentrations.
	consts.y_init = [0; 8];

	% solve ODE.
	disp("solving ode");
	[ode_tout, x] = ode45(@(t,y) ode_funcs.dydt(t, y, consts, params), [0; consts.tmax], consts.y_init);
	disp("ode solved");

	ode_lacy = x(:, 2);
	trajectory = cat(2, ode_tout, ode_lacy)

end