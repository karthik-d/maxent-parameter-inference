import matlab.engine

eng = matlab.engine.start_matlab()
val = eng.lac_system_ode_solve()
print(val)