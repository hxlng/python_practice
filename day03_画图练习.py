import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
#画出下图y = (np.sin(x-2)**2)*np.exp(-x**2)
plt.subplot(2,1,1)  #画到一张画布上 不能每张都show()
x = np.linspace(0,2,1000)
y = (np.sin(x-2)**2)*np.exp(-x**2)
# plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x-2)**2*e(-x**2)$",color="deepskyblue",linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$sin^2(x-2)e^{(-x^2)}$")
plt.legend()


#画cos(x)
plt.subplot(2,2,3)
x = np.linspace(0,6,1000)
y =np.cos(x)
# plt.figure(figsize=(8,4))
plt.plot(x,y,label="$cos(x)$",color="lightgreen",linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$cos(x)$")
plt.legend()


#画饼图
plt.subplot(2,2,4)
labels = ['oranges','apples','pears','bananas'] #定义标签
sizes = ["30","15","10","45"] #每块值
colors = ['yellow','red','blue','mediumseagreen'] #每块颜色定义
explode = (0.01,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
plt.pie(sizes,explode=explode,
                labels=labels,
                colors=colors,
                autopct = '%.1f%%', #数值保留固定小数位
                shadow = False, #无阴影设置
                startangle =90, #逆时针起始角度设置
                pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.show()