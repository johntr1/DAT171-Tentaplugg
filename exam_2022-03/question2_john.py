# Har mest problem med numpy och scipy! Lär nu
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

def polyfunk(x, li):
    if len(li) == 3:
        return li[0] * x * x + li[1]
    elif len(li) == 4:
        return li[0] * np.power(x, 3) + li[1] * np.power(x, 2) + li[2] * x + li[3]
    elif len(li) == 5:
        return li[0] * np.power(x, 4) + li[1] * np.power(x, 3) + li[2] * np.power(x, 2) + li[3] * x + li[4]
    elif len(li) == 6:
        return li[0] * np.power(x, 5) + li[1] * np.power(x, 4) + li[2] * np.power(x, 3) + li[3] * np.power(x, 2) + li[4] * x + li[5]


arr = np.loadtxt('values.txt')

x = arr[:, 0]

y = arr[:, 1]

x_eval = np.linspace(np.min(x), np.max(x), num=1000)  # Construct x-points for spline/poly evaluation

plt.subplot(2, 1, 1)
plt.plot(x, y, 'x')
legend = ['Data']
for smooth in [None, 0, 15]:
    spl = UnivariateSpline(x, y, w=None, k=2, s=smooth)
    plt.plot(x_eval, spl(x_eval))
    legend.append(f'{smooth}')
plt.legend(legend)

plt.subplot(2, 1, 2)
legend = ['Data']
plt.plot(x, y, 'x')

for i in range(2,6):
    output = np.polyfit(x, y, deg=i)
    plt.plot(x_eval, polyfunk(x_eval, output))
    legend.append(f'Deg = {i}')
plt.legend(legend)

plt.show()
# 5


