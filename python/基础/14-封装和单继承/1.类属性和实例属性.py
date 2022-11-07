# @Time   : 2022/4/28
# @Author : Wilia
"""
类体中、所有方法之外，此范围定义的变量，就是类属性；
类体中、所有方法内部：以"self.变量名"的方式定义的变量，称为实例属性；
"""


# class Hero():
#     money = 1000000  # 类属性
#     print(f'捐赠了{money / 2}元')
#
#     def __init__(self, name):
#         self.name = name  # 实例属性
#
#     def move(self):
#         print(f'我的名字是{self.name}')
#
#
# h = Hero('seeky')
# h.move()
# print(h.money)  # 1000000 对象它能够访问类属性
# print(h.name)  # seeky   对象它能够访问实例属性
# print(Hero.money)  # 1000000 类可以访问类属性
# print(Hero.name)  # 报错   类不能访问实例属性

'''**********************************************'''


# class Hero():
#     num = 0  # 类属性
#
#     def __init__(self, name):
#         self.name = name  # 实例化属性
#
#     def move(self):
#         print(f"{self.name}正在移动")
# h1=Hero("wang")
# h1.move()