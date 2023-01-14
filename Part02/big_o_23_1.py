import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 30)
plt.plot(n, 4 * n * np.log2(n), label='$4n\log_2(n)$')
plt.plot(n, n ** 2, label='$n^2$')
# plt.plot(n, 32 * n, label='$32n$')
plt.legend()
plt.savefig('plot_nlogn_and_n2.png')
