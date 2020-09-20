import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
yj=[17,173,101]
yx=[50,114,82]

x=[2017,2018,2019]


plt.plot(x, yj, marker='o', markersize=3)
plt.plot(x, yx, marker='o', markersize=3)
plt.legend(['Income','Sales'])
plt.title('E76B The company is three-year flow sheet')
plt.show()