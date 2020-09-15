import numpy as np
import matplotlib.pyplot as plt

#Define parameters
t_max = 120 #Maximum time in days
dt = .1 #time steps, in days
t = np.linspace (0, t_max, int(tmax/dt) + 1) # create time datapoints

N = 10000 #total population
init_vals = 1 - 1/N, 1/N, 0,0

alpha = 0.2
gamma = 0.5
beta = 1.75

params = alpha, gamma, beta

def myfunc(init_vals, params, t, rho):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R =[S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma = params
    dt = t[1] - t[0]
    for k in t[1:]:
        next_S = S[-1] - (rho*beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (rho*beta*S[-1]*I[-1] - alpha * E [-1])* dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])* dt
        next_R = R[-1] + (gamma * I[-1]) *dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    return S, E, I, R, t

