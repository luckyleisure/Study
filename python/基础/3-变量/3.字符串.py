"""
"字符串：一串字符，使用一对引号把数据内容包围"
"字符串本身有多行时，使用三引号"
"字符串里面需要再使用引号时，要遵循 单包双 或 双包单 或转义"
"""
str1 = 'hello'
print(type(str1))
str2 = '10'
print(str2, type(str2))

# 字符串本身有多行时，使用三引号
str3 = """hello
python
"""
print(str3)

str5 = "I'l be a good person"  # 双包单
print(str5)  # I'l be a good person

# + 拼接
s1 = 'hello'
s2 = 'python'
print(s1 + ' ' + s2)  # hello python
print(s1 + '⭐' + s2)  # hello⭐python

# * 复制，乘法
print(s1 * 2)  # hellohello

# in  和 not in
print('h' in s1)  # True
print('p' not in s1)  # True
