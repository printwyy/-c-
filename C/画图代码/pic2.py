import pandas as pd

from matplotlib import pyplot
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
yj=[2751,5128,5418]
yx=[3271,5174,4191]

x=[2017,2018,2019]


plt.plot(x, yj, marker='o', markersize=3)
plt.plot(x, yx, marker='o', markersize=3)

plt.legend(['jinxiang','xiaoxiang'])
plt.title('E7A The company is three-year flow sheet')
plt.show()