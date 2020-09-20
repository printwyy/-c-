import pandas as pd

from matplotlib import pyplot
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字

yj=[20678648.6,17874587.79,30153572.52]
yse=[265377041.2,316581849.7,180168535.6]
x=[2017,2018,2019]


plt.plot(x, yj, marker='o', markersize=3)
plt.plot(x, yse, marker='o', markersize=3)

plt.legend(['jinxiang','xiaoxiang'])
plt.title('E7A Three year flow line chart of the company')
plt.show()