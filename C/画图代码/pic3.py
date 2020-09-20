import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
ym=[501538,194457.28,176074.54]
ysr=[1038679.26,1528332.65,1719602.8]

x=[2017,2018,2019]


plt.plot(x, ym, marker='o', markersize=3)
plt.plot(x, ysr, marker='o', markersize=3)
plt.legend(['out','in'])
plt.title('E76B Three year flow line chart of the company')
plt.show()