"用户（键盘）输入：input()"
"input的3个特点"
# 1） 当程序执行input时，会等待用户输入，输入完成后才继续向下执行-----"死等"
# input('哈哈，来输入一个数：')
# print('haha')
# 2) 在python中，input接收用户输入后，一般存储到变量，方便使用
# num = input('哈哈，来输入一个数：')
# print(num)
# 3) input会把接收到的任意用户输入的数据都当作字符串来处理。
# num = input('哈哈，来输入一个数：')
# print(num, type(num))    # 7 <class 'str'>

# ---限制输入为整数---
# num1 = int(input('哈哈，来输入一个数：'))
# print(num1, type(num1))

# 转换为小数
# num1 = float(input('哈哈，来输入一个数：'))
# print(num1, type(num1))

# 限制输入为数字
# num1 = eval(input('哈哈，来输入一个数：'))
# print(num1, type(num1))

# num1= input('请输入三个整数：').split()
# print([type(eval(i)) for i in num1]) #[<class 'int'>, <class 'int'>, <class 'int'>]
# num1,num2,num3= input('请输入三个整数：').split(',')
# print(num1,num2,num3)
num1,num2,num3= map(eval,input('请输入三个整数：').split())
print(num1,num2,num3)
print(num1,type(num1))
print(num2,type(num2))
print(num3,type(num3))
