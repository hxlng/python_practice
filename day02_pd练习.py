import pandas as pd
import numpy as np
#1、ob=pd.Series([2,3,5,7,3,1]),建立Series的时候指定索引
ob=pd.Series([2,3,5,7,3,1],index=['a','b','c','d','e','f'])
print(ob)
#2、根据dt、id创建Series
dt=[1,2,3,4,5]
id=['a','b','c','d','e']
ob=pd.Series(dt,id)
print(ob)
#3建立下列DataFame
data1={'subject_id':['1','2','3','4','5'],
       'first_name':['Alex','Amy','Allen','Alice','Ayoung'],
       'last_name':['Anderson','Ackerman','Ali','Aoni','Atiches']}
data2={'subject_id':['4','5','6','7','8'],
       'first_name':['Billy','Brian','Bran','Bryce','Betty'],
       'last_name':['Bonder','Black','Balwner','Brice','Btisan']}
data3={'subject_id':['1','2','3','4','5','7','8','9','10','11']
       ,'test_id':[51,15,15,61,16,14,15,1,61,16]}
#(1)返回最大值
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df3=pd.DataFrame(data3)
Max=df3['test_id'].max()
print(Max)
#(2)把df1和df2两个DadaFrame沿着x轴进行合并,命名为df12x
df12X=pd.concat([df1,df2],axis=1)
print(df12X)
#(2)把df1和df2两个DadaFrame沿着y轴进行合并,命名为df12y
df12Y=pd.concat([df1,df2],axis=0)
df12Y=pd.concat([df1,df2],ignore_index=True) #同上
print(df12Y)
#(4)
three=df1.head(3)
print(three)
#4建下列DataFrame
data={'Cite':['Neijiang','Chegdu','Beijing'],
      'year':[20,21,24],
      'cash':[6,8,10]}
df=pd.DataFrame(data)
print(df)

#5添加book列

df['book']=['001','002','003']
print(df)
#6打印year列 删除book列
print(df['year'])
del df['book']
print(df)
#7开方 year和cash                 
print("*********************")
print(np.sqrt(df['year']))
kai=df['year'].apply(np.sqrt)
print(kai)

#平方 year和cash
print('****************')
print(df['year'].apply(lambda x:x**2))
print('平方结果：',df['year']**2,df['cash']**2)
print('开方结果：',(df['year'])**(1/2),(df['cash'])**(1/2))
