import numpy as np
#如何创建一个3×3的二维数组，值域为0到8？
a1=np.arange(9).reshape(3,3)
print("a1:",a1)
#给出起点2，长度10和步长4，如何创建一个numpy数组
a2=np.arange(2,4*10+2,4)
print("a2:",a2)
#创建一个10×10的随机矩阵并找到最大值和最小值
a3=np.random.random((10,10))
print("a3max min",a3.max(),a3.min())

a4=np.array([[4,5],[6,7]])
b4=np.array([[1,5],[3,4]])
#计算a和b的普通乘法
print(a4*b4)
print(np.multiply(a4,b4))
#计算a和b的矩阵乘法
print(np.dot(a4,b4))
#计算a和b的转置
print(a4.T,b4.T)
#沿列累计总和分别对a和b
print(np.cumsum(a4,1),np.cumsum(b4,1))
#计算a+b
print(np.add(a4,b4))
#横向合并a和b
print(np.hstack((a4,b4)))
#纵向合并a和b
print(np.vstack((a4,b4)))
#将a纵向分为两部分，将b横向分为两部分
print(np.split(b4, 2, axis=1)) # 表示对A进行分割，分为两块，axis=1为水平分割
print(np.hsplit(b4, 2)) # 效果同上
print(np.split(a4, 2, axis=0)) # 表示对A进行分割，分为3块，axis=0为垂直分割
print(np.vsplit(a4, 2)) # 效果同上
#表示在【0-31】这32个数字中分成8行4列
a5=np.arange(0,32).reshape(8,4)
print("a5",a5)
#在1和2之间（包括1和2）分成等值的3份输出，结果：[ 1. 1.5  2. ]
a6=np.linspace(1,2,3)
print("a6",a6)
#输出行列都为9的单位矩阵
a7=np.eye(9)
print("a7",a7)
a7=np.identity(9)
print("a7",a7)
#分别输出1.0，1.5，2.0
print('****************************************')
a8=np.linspace(1,2,3,dtype=float)
for x in np.linspace(1,2,3):
    print(x)

print(a8)
#创建一个大小为6的向量，值域为0到2
a9=np.linspace(0,2,6)
print(a9)
#创建大小为10的，值为0的向量
a10=np.zeros(10)
print(a10)
#创建大小为10的，值为0的向量
a11=np.sort(np.random.random((1,10)))
print(a11)
#创建一个4*4数组，使用索引的方式获取第二行第一列和第三行第二列的数据
a12=np.arange(1,17).reshape(4,4)
print(a12)
print(a12[1][0])
print(a12[2][1])
#使用切片的方式获取上题中数组的前2行第2，3列的数
a13=a12[0:2,1:3]
print(a13)