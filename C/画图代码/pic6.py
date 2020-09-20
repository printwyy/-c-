import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
ym=[1026,1532,1900]
ysr=[18122,8295,7219]

x=[2017,2018,2019]


plt.plot(x, ym, marker='o', markersize=3)
plt.plot(x, ysr, marker='o', markersize=3)
plt.legend(['out','in'])
plt.title('E3c The company is three-year flow sheet')
plt.show()