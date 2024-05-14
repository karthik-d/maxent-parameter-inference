function funcs = lac_system_ode
    funcs.dydt = @lac_system_dydt;
end


function dydt = lac_system_dydt
    dydt(1) = 0;
end