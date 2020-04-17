import matplotlib.pyplot as plt
from algs import signal_func, autocorr, R, m, D

n = 12
omega = 2700
N = 64
range_min = 0
range_max = 1

x_gen = signal_func(n, omega, range_min, range_max)
y_gen = signal_func(n, omega, range_min, range_max)

x = [x_gen(i) for i in range(N)]
y = [y_gen(i) for i in range(N)]

fig, ax = plt.subplots()
ax.plot(range(N), x, label='x')
ax.plot(range(N), y, label='y')
plt.legend()
plt.show()
fig.savefig('Графік')
m = m(x)
D = D(x, m)
print(f'm: {m}\nD: {D}')

#Rxx = R(x[:N//2], x[N//2:])
#plt.plot(range(N//2), Rxx, label='Rxx')
#Rxy = R(x[:N//2], y[:N//2])
#plt.plot(range(N//2), Rxy, label='Rxy')

R_taux = [autocorr(x_gen, y_gen, N, tau) for tau in range(N//2)]
R_tauy = [autocorr(x_gen, x_gen, N, tau) for tau in range(N//2)]
fig1, ax1 = plt.subplots()
ax1.plot(range(N//2), R_taux, label='RxxtauX')
ax1.plot(range(N//2), R_tauy, label='RxxtauY')
plt.legend()
plt.show()
fig1.savefig('Графік1')
