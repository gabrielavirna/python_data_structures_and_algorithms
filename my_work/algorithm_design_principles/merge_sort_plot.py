"""
Merge Sort:
the relationship between the size of the input and the total running time: (7n*log2(n)+7) compared to n^2

Notice how for very low values of n, the time to complete, t , is actually lower for an algorithm that runs in n^2 time.
However, for values above about 40, the log function begins to dominate, flattening the output until at the
comparatively moderate size n = 100, the performance is more than twice than that of an algorithm running in n^2 time.
Notice also that the disappearance of the constant factor, + 7 is irrelevant at high values of n


In this way we can see that the two lower curves have similar growth rates, when compared to the top (x^2) curve.
We say that these two lower curves have the same complexity class.
"""

import matplotlib.pyplot as plt
import math

x = list(range(1, 100))
l = []
l2 = []
a = 1

plt.plot(x, [y * y for y in x], label='x^2')
plt.plot(x, [7 * y * math.log(y, 2) for y in x], label='7n*log2(n)')
# counting six operations vs seven operations
plt.plot(x, [6 * y * math.log(y, 2) for y in x], label='6n*log2(n)')
plt.legend(loc='upper left')
plt.xlabel("n")
plt.ylabel("t")
plt.show()
