# name="fngksjlxmzadkkdkf"
# print(name[0])    #数组第一位
# print(len(name))  #数组长度
# print(name[2:5])  #数组第三位到第五位

# my_List=["你好",2018,2019,2020,"许桐","许桐"]
# print(my_List[0])    #第一位
# my_List.append("大哥") #将对象追加到列表末尾

# print(my_List)
# print(my_List.count("许桐"))#返回值出现的次数，许桐出现两次
# help(my_List)

# mylist=[1,2,3,4,5]
# mytuple=(1,2,3,4,5)
# # print(type(mylist))
# #list is mutable    数据类型可变
# #tuple is inmutable 数据类型不可变
# #For example
# print(dir(mylist))
# print(".............")
# print(dir(mytuple))
# mylist.remove(2)
# print(mylist)
'''dictionary'''
# myDictionary={"key":"value","key2":"value"}
# myphone={"Iphone x":1000,"Huawei":10000}
# Iphone_price=myphone["Iphone x"]
# print("Iphone price:"+str(Iphone_price))
# #"Iphone price"是字符串不能直接与价格相加，需要将价格转换为字符串类
# myphone["Iphone x"]=100#降价到100
# print(myphone)
# myphone.clear()

# a=10
# b=20
# if a<b:
#     print('hello')
# if b<30:
#     print("mmm")
age=int(input("please enter your age:"))
if age<21:
    print("you can not smoke")
elif age==100:
    print("you are 100 years old,please quit smoking")
else:
    print("you can smoke")

