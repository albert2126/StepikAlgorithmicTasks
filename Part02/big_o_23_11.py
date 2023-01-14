import math
import numpy as np
from matplotlib import pyplot as plt

f1 = lambda n: n ** 0.1
f2 = lambda n: math.log(n, 5)

n = 10 ** 13
# while f1(n) > f2(n):
#     n += 1

print(n, f1(n), f2(n))


# n = np.linspace(1, 10)
# plt.plot(n, f1(n), label='$n^0.1$')
# plt.plot(n, f2(n), label='$log(n)^5$')
# plt.legend()
# plt.savefig('plot_n01_and_log.png')
