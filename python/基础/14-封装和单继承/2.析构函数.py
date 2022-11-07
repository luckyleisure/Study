# @Time   : 2022/4/28
# @Author : Wilia

"__del__():主要对那些长期占用内存的临时变量进行销毁"


# 正常情况下，__del__()最后被执行
# class Person:
#     def __init__(self):
#         print('这是构造方法')
#
#     def __del__(self):
#         print('被销毁了')
#
#
# p = Person()
# print(123)
# print(456)


# 当使用del手动删除对象时，会直接调用这个方法
# class Person:
#     def __init__(self):
#         print('这是构造方法')
#
#     def __del__(self):
#         print('被销毁了')
#
#
# p = Person()
# del p
# print(123)
# print(456)


# class Dog:
#     def __init__(self):
#         print("构造！")
#
#     def __del__(self):
#         print("析构！")
#
#
# d = Dog()
# # del d
# print(123)