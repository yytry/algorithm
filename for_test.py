import numpy as np
x = np.array([1, 11, 22, 33, 44, 55])
"""
array 删除内容
while 1:
    key = input("请输入0~5的数字索引: ")
    if 0 <= int(key) <= 5:
        x = np.delete(x, int(key))
        print(x)
        break
    else:
        print("输入索引不在0~5之间，请重新输入！")
"""

while 1:
    key = int(input("请输入0~5的数字索引: "))
    num = int(input("请输入欲添加的数值: "))
    if 0 <= key <= 5:
        x = np.insert(x, key, num)
        print(x)
        break
    else:
        print("输入索引不在0~5之间，请重新输入！")