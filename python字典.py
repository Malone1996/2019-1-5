# 定义:字典是一种可变容器模型,可存储任意类型对象

# 字典格式
# d = {key1: value1, key2: value2}

# 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
dict = {'a': 1, 'b': 2, 'b': 3}
tem = dict['b']
print(tem)  # 输出3
print(dict)  # 输出{'a': 1, 'b': 3}

print('--------------------')

# 访问字典里的值
dict1 = {'name': 'Zara', 'age': 7, 'Class': 'First'}
print("dict1['name']:", dict1['name'])
print("dict1['age']:", dict1['age'])
print("dict1['Class']:", dict1['Class'])

print('--------------------')

# 删除字典元素
dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict2['Name']  # 删除Name键
print(dict2)
dict2.clear()  # 清空字典
print(dict2)
# del dict2  # 删除字典
# print(dict2)

print('--------------------')

# 字典内置函数
dict3 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(len(dict3))  # 输出字典长度
print(str(dict3))  # 输出字典，以可打印的字符串表示
print(type(dict3))  # 返回输入的变量类型，如果变量是字典就返回字典类型

print('--------------------')
# 注:字典单引号,JSON双引号
print('--------------------')
