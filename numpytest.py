import numpy as np
# array=np.array([[1,2,3],
#                 [3,4,5]])
# print(array)
# print('number of dim:',array.ndim)
# print('shape:',array.shape).
# print('size:',array.size)

# a=np.array([2,23,4])
# print(a)
# a=np.array([2,3,4],dtype=np.int)#编译错误
# print(a)

# a=np.zeros((3,4))
# print(a)
# a=np.arange(10,20,2)
# print(a)
# print('10-20的数列，步长为2')
# a=np.arange(12).reshape((3,4))
# print(a)
# print('0-11的数列，生成了3行4列的矩阵')
# a=np.linespace(1,10,5)
# print(a)#此处无法运行
'''
5.基础运算
'''
# a=np.array([10,20,30,40])
# b=np.arange(4)#0-3
# # c=a-b
# d=b**2                     #b的平方
# c=10*np.cos(a)             #10xcosa
# print(c)
# print(d)
# print(b<3)
# print(b==3)

# a=np.array([[1,1],
#             [0,1]])
# b=np.arange(4).reshape((2,2))
# c=a*b                       #逐个相乘
# c_dot=np.dot(a,b)           #矩阵乘法
# c_dot_2=a.dot(b)            #同上，表达方式不一样
# print(c)
# print(c_dot)
# print(c_dot_2)

# a=np.random.random((2,4))    #随机生成2行4列
# print(a)
# b=np.sum(a)                   #求和
# c=np.min(a)                   #元素当中最小值
# d=np.max(a)                   #元素当中最大值
# print(b)
# print(c)
# print(d)

# A=np.arange(2,14).reshape((3,4)) #2-14数生成3行4列的矩阵
# print(A)
# print(np.argmin(A))            #最小值是2,2在第0位，打印出是0
# print(np.argmax(A))            #最大值是13,13在第11位，打印出是11
# print(np.mean(A))              #A的平均数7.5
# print(A.mean())                #A的平均数，同上
# print(np.median(A))            #A的中位数位7.5，逐位相加平均数等于中位数
# print(np.cumsum(A))            #第一个元素为第一位，第二个元素为前两位相加，依次类推,累加
# print(np.diff(A))              #累差，相邻两个数相减，三行四列累差之后变成三行三列，四个数三个空
# print(np.nonzero(A))           #查询矩阵之中非零数位置，输出两个array,前面代表行，后面代表列
# print(np.sort(A))              #逐行排序
# print(np.transpose(A))         #矩阵A的转置
# print(A.T)                     #矩阵A的转置
# print((A.T).dot(A))            #A*A^T
# print(np.clip(A,3,7))          #3-7之间的数保留，小于3都变成3，大于7都变成7
# print(np.mean(A,axis=0))       #A的列平均值
# print(np.mean(A,axis=1))       #A的行平均值
'''
7.numpy索引
'''
# A=np.arange(3,15)              #生成3-15的数组
# print(A)                       #
# print(A[2])                    #数组中第三个元素是5
# A=np.arange(3,15) .reshape((3,4))#3-15变成三行四列的数列
# print(A)
# print(A[2])                      #矩阵中第三行，0 1 2 ，2代表第三行
# print(A[1][1])                   #矩阵中的2行2列
# print(A[1,1])                    #同上，表示方法不同
# print(A[:,1])                    #矩阵中的第二列，1代表矩阵第二列
# print(A[2,:])                    #矩阵中的第三行，2代表第三行，都是从0开始算
# print(A[1,1:3])                  #矩阵中第二行，第二列到第四列之间的数

# A=np.arange(3,15) .reshape((3,4))#3-15变成三行四列的数列
# for row in A:                      #输出迭代A的行
#     print(A)
# for column in A.T:                 #输出迭代A的列，三行四列numpy不能直接迭代出来
#     print(column)
#     print(A.flat)
#     print(A.flatten())             #三行四列变成一行
# for item in A.flat:                #迭代A的每一个项目
#     print(item)



