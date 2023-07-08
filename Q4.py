import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

num_lists = 1000
list_length = 15
lists = []
for i in range(num_lists):
    random_list = sorted([random.uniform(0, 1) for i in range(list_length)])
    lists.append(random_list)
lists_np = np.array(lists)
a = lists_np[:, 0]
b = lists_np[:, 9]
c = lists_np[:, 14]

alpha_a = 1
beta_a = 1

alpha_b = 2
beta_b = 2

alpha_c = 3
beta_c = 1

dist_a = beta(alpha_a, beta_a)
dist_b = beta(alpha_b, beta_b)
dist_c = beta(alpha_c, beta_c)

sample_size = len(a)
sample_a = dist_a.rvs(size=len(a))
sample_b = dist_b.rvs(size=len(b))
sample_c = dist_b.rvs(size=len(c))

# نمودار چگالی برای هر بردار
x = np.linspace(0, 1, 1000)
plt.plot(x, dist_a.pdf(x), label='a')
plt.plot(x, dist_b.pdf(x), label='b')
plt.plot(x, dist_c.pdf(x), label='c')

# نمونه‌ها را نمایش میدهد
plt.hist(sample_a, density=True, alpha=0.5)
plt.hist(sample_b, density=True, alpha=0.5)
plt.hist(sample_c, density=True, alpha=0.5)

plt.legend()
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Beta Distribution')
plt.show()

expected_value = np.mean(np.concatenate([a, b, c]))
print("Expected Value:", expected_value)