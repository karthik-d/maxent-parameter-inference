function funcs = lac_system_ode
    funcs.dydt = @lac_system_dydt;
end


function dydt = lac_system_dydt(t, y, consts, params)
       
    syms tmg_i lac_y alph beta_t beta_g r r0 rT n;
    exprs = lac_system_exprs;

    % compute dependent params and constants.
    consts.r0 = consts.rT/(params.rho - 1);
    params.alph = 84.4/(1 + (consts.glu/8.1)^1.2) + 16.1;
    params.beta_t = 1.23e-03 * consts.tmg_e^0.6;

    % active LacI (i.e., r).
    lac_i = double(subs(exprs.lac_i, ...
        {tmg_i rT n}, {y(1) consts.rT params.n} ...
    ));
    
    % dydt is a vector of rate eqns: [tmg_i; lac_y].

    dydt = [...
        double(subs(exprs.tmg_i, ...
        {lac_y tmg_i alph beta_t beta_g r r0 rT params.n}, ...
        {y(2) y(1) params.alph params.beta_t params.beta_g lac_i consts.r0 consts.rT params.n})) ...
    ; ...
        double(subs(exprs.lac_y, ...
        {lac_y tmg_i alph beta_t beta_g r r0 rT params.n}, ...
        {y(2) y(1) params.alph params.beta_t params.beta_g lac_i consts.r0 consts.rT params.n})) ...
    ];
end


function exprs = lac_system_exprs

    syms tmg_i lac_y alph beta_t beta_g r r0 rT n;

    exprs.tmg_i = beta_t*beta_g*lac_y - tmg_i;
    exprs.lac_y = alph*(r0/(r + r0)) - lac_y;
    exprs.lac_i = rT*(1/(1 + tmg_i^n));
end