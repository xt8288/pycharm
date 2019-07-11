from __future__ import print_function
import tensorflow as tf
import numpy as np

'''y=0.1x+0.3'''
'''https://github.com/MorvanZhou/tutorials'''
# create data
x_data = np.random.rand(100).astype(np.float32)#生成100随机数列，TensorFlow大部分数据是float32
y_data = x_data*0.1 + 0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
#W大写可能是矩阵，定义变量Variable随机数列生成参数，一维结构，随机数列范围-1~1
#初始值为零，一步步学习接近0.1和0.3
y = Weights*x_data + biases
#预测的y
loss = tf.reduce_mean(tf.square(y-y_data))#计算预测y和实际y的差别。
optimizer = tf.train.GradientDescentOptimizer(0.5)#学习效率小于1
train = optimizer.minimize(loss)#减少误差
### create tensorflow structure end ###

sess = tf.Session()
# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()#初始化
else:
    init = tf.global_variables_initializer()
sess.run(init)  #激活 非常重要

for step in range(201):#训练201步
    sess.run(train)    #训练
    if step % 20 == 0: #每隔20步打印一下
        print(step, sess.run(Weights), sess.run(biases))
