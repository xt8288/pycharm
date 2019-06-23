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
# d=b**2          #b的平方
# c=10*np.cos(a)  #10xcosa
# print(c)
# print(d)
# print(b<3)
# print(b==3)

# a=np.array([[1,1],
#             [0,1]])
# b=np.arange(4).reshape((2,2))
# c=a*b                #逐个相乘
# c_dot=np.dot(a,b)    #矩阵乘法
# c_dot_2=a.dot(b)     #同上，表达方式不一样
# print(c)
# print(c_dot)
# print(c_dot_2)

# a=np.random.random((2,4))    #随机生成2行4列
# print(a)
# b=np.sum(a)                  #求和
# c=np.min(a)                  #元素当中最小值
# d=np.max(a)                  #元素当中最大值
# print(b)
# print(c)
# print(d)

A=np.arange(2,14).reshape((3,4)) #2-14数生成3行4列的矩阵
print(A)
print(np.argmin(A))              #最小值是2,2在第0位，打印出是0
print(np.argmax(A))              #最大值是13,13在第11位，打印出是11
print(np.mean(A))                #A的平均数7.5
print(A.mean())                  #A的平均数，同上
print(np.median(A))              #A的中位数位7.5，逐位相加平均数等于中位数
print(np.cumsum(A))              #第一个元素为第一位，第二个元素为前两位相加，依次类推


