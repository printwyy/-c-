import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
yj=[19633189.31,17012616.91,17841716.01]
ysr=[266378089.3,166578695.7,140534177.9]

x=[2017,2018,2019]


plt.plot(x, yj, marker='o', markersize=3)
plt.plot(x, ysr, marker='o', markersize=3)
plt.legend(['out','in'])
plt.title('E3C Three year flow line chart of the company')
plt.show()