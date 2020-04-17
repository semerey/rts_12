import random
import math
import time


def ftime(f):
    def func(*args):
        start = time.time()
        a = f(*args)
        # print(f"({f.__name__})час:", time.time() - start)
        return a
    return func


@ftime
def signal_func(n, omega, start=0, end=1):
    A = [start + (end - start) * random.random() for _ in range(n)]
    phi = [start + (end - start) * random.random() for _ in range(n)]

    def f(t):
        x = 0
        for i in range(n):
            x += A[i]*math.sin(omega/n * t * i + phi[i])
        return x
    return f


@ftime
def expectedValue(x):
    m = sum(x)/len(x)
    return m, sum([(i - m) ** 2 for i in x]) / (len(x) - 1)


@ftime
def m(x):
    return sum(x)/len(x)


@ftime
def D(x, m=None):
    if m is None:
        m = m(x)
    return sum([(i - m) ** 2 for i in x]) / (len(x) - 1)


@ftime
def R(x, y, m=None):
    start = time.time()
    mx, Dx = expectedValue(x)
    my, Dy = expectedValue(y)
    if m is not None:
        mx = m
        my = m
    N = min(len(x), len(y))
    R = [(x[i]-mx)*(y[i]-my)/(N-1) for i in range(N)]
    print(time.time() - start)
    return R

@ftime
def autocorr(x_gen, y_gen, N, tau=0):
    x = [x_gen(i) for i in range(N)]
    y = [y_gen(i+tau) for i in range(N)]
    M_x, D_x = expectedValue(x)
    M_y, D_y = expectedValue(y)

    R = 0
    for i in range(N//2-1):
        R += (x[i] - M_x)*(y[i+tau] - M_y)/(N//2-1)
    R /= (D_x*D_y)**(1/2)
    return R
