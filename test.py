import numpy as np
import matplotlib.pyplot as plt


# تعریف تابع
def func(x):
    return np.sin(x)  # تابع مثال: سینوس


# تولید داده‌ها
x = np.linspace(0, np.pi / np.pi, 100)  # تولید 100 نقطه بین 0 تا 2*pi
y = func(x)

# رسم نمودار
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('نمودار تابع')
plt.grid(True)

# نمایش نمودار
plt.show()
