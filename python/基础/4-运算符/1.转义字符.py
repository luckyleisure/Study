"转义字符：默认是转义的意思"
# \n  换行符
print('123\n123')
print('123\\n123')  # 123\n123

# \t制表符，默认4个空格
# 有排版的功能
str1 = '网站\t\t域名\t\t\t\t\t\t\t\t年龄\t\t价值'
str2 = '六星教育 https://www.sixstaredu.com/\t\t8\t\t500000w'
str3 = '百度\t\twww.baidu.com\t\t\t\t\t20\t\t5000000w'
print(str1)
print(str2)
print(str3)

# 自动排版对齐
print("\t*")
print('w\t*')
print('ww\t*')
print('www\t*')
print('wwww\t*')
print('wwwww\t*')
print('wwwwww\t*')
print('wwwwwww\t*')

# \ 转义符
str1 = 'I\'ll go home'
print(str1)

# \续行符
str2 = """你们\
为什么总有十万个为什么？
"""
print(str2)

str3 = """你们
为什么总有十万个为什么？
"""
print(str3)
