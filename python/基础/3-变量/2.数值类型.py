num1 = 10
num2 = 10.5
print(type(num2))  # <class 'float'>
# 科学计数法
print(3.2E5)  # 320000.0 = 3.2*10^5
print(type(3.2E5))  # <class 'float'>
print(3e5)  # 300000.0
print(type(3e5))  # <class 'float'>
"所有判断的结果都是布尔序列：True或False"
print(True)
print(type(True))  # <class 'bool'>
print(True + 2)  # 3
print(False + 1)  # 1

"复数：包含了实部和虚部"
# x^2 + 1 = 0
# 复数范围内：x^2 = -1
# z = a + bj
a = 1
b = 2
z = a + 1j * b
print(z)  # (1+2j)
z = 2 + 3j
print(z)  # (2+3j)
print(type(z))  # <class 'complex'>
