# str() 转换为字符串
num1 = 123
print(type(num1))   # <class 'int'>
s1 = str(num1)
print(s1,type(s1))  # 123 <class 'str'>

# int()  转换为整型
# s2 ='haha123'
# print(int(s2))   # ValueError: invalid literal for int() with base 10: 'haha123'

s3 = '123'
print(int(s3),type(int(s3)))    # 123 <class 'int'>

# print("我们都是中国人")

# eval() -----效果是去掉引号
x = 4
print('x*4')      # x*4
print(x*4)        # 16
print(eval('x*4'))# 16
