import json

# Python转JSON
data1 = {'no': 1, 'name': 'Zara', 'age': '20'}  # 字典
json_str = json.dumps(data1)  # 对数据进行编码
print('Python原始数据:', repr(data1))
print('JSON对象:', json_str)

print('--------------------')

# JSON转Python
data2 = json.loads(json_str)  # 对数据进行解码
print("姓名:", data2['name'])
print("年龄:", data2['age'])
