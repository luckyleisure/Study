"""1. 算术运算符"""
print(10 + 20)  # 30
print(10 - 20)  # -10
print(10 * 20)  # 200
print(10 / 20)  # 0.5
print(9 // 2)  # 表示9除以2，取整数部分  4
print(9 % 2)  # 表示9除以2,取余数部分
print(5 ** 3)  # 表示5的3次幂125

"""2. 赋值运算符"""
num = 1
# 多个变量赋值
num1, float1, str1 = 10, 10.5, 'hello world'
print(num1)
print(float1)
print(str1)

# +=
a = 99
a += 1  # 等效于a = a+1
print(a)

# # -=
a -= 1  # 等效于a = a - 1
print(a)

# *=
b = 2
b *= 3  # 等效于 b = b*3
print(b)

# /=
a = 2
b = 11
b /= a  # 等效于b = b/a
print(b)

# //=
a = 2
b = 11
b //= a  # b = b//a
print(b)

# # **=
a = 3
b = 10
b **= a  # 等效于b = b**a
print(b)

"""3.比较运算符"""
"通常判断的结果是True或False"
"== 表示等号   ！= 不等号"
a = 10
b = 20
print(a >= b)  # False
print(a == b)  # False
print(a < b)  # True
print(a != b)  # True
