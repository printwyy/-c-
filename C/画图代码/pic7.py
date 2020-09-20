import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
ya=[0.2787,0.3677,0.3536]
yb=[0.2698,0.4094,0.3209]
yc=[0.3984,0.2982,0.3033]
x=[2017,2018,2019]


plt.plot(x, ya, markersize=3,marker='o')
plt.plot(x, yb, marker='o', markersize=3)
plt.plot(x, yc, marker='o', markersize=3)
'''
plt.scatter(x,ya)
plt.scatter(x,yb)
plt.scatter(x,yc)
'''
plt.legend(['A','B','C'])
plt.title('Influence index')
plt.xticks(x)
plt.show()