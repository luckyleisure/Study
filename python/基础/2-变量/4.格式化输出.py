"应用场景：需要按照指定的格式去输出内容时"
name = 'lucy'
age = 18
print("名字是",name,'年龄是',age,'岁')
# name : age
print(name,':',age)

# f表达式  f"{变量名}"
print(f'名字是{name},年龄是{age}岁')  # 名字是lucy,年龄是18岁
print(f'{name}={age}')

area = 500
print(area)
print(f'area = {area}')   # area = 500

print(f'10+8')   # 10+8
print(f'{10+8}') # 18

month = 3
salary = 500
print(f'{month}月的工资为{salary}元！')