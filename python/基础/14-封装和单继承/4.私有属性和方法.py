# @Time   : 2022/4/28
# @Author : Wilia
"""
_x     单前置下划线，伪私有，类和子类可以访问
__xx   双前置下划线，私有成员，只能类对象自己访问，连子类对象也不能访问到
__xx__ 双前后下划线，魔法对象或属性
xx_    单后置下划线，用于避免与python关键词的冲突
"""

# class Classmate:
#     name = 'lucy'
#     _age = 88    # 伪私有
#     __sex = 'F'  # 私有属性
# c = Classmate()
# print(c.name)           # lucy
# print(Classmate.name)   # lucy
# print(Classmate._age)   # 88
# print(c._age)           # 88
# print(c.__sex)            # 报错
# print(Classmate.__sex)    # 报错

# "强调访问法"  对象._类名私有属性
# print(c._Classmate__sex)

"通过'正规手段'去访问私有属性和方法"
"""
访问私有属性或方法的解决方案本质是：在类中再定义一个公有方法，然后在该公有方法里去使用私有属性或调用私有方法；访问：外部直接调用该公有方法
"""


# 1.正规方式调用私有属性
# class Classmate:
#     def __init__(self):
#         self.__name = '杨哈哈'
#     def fn(self):           # 公有方法
#         print(self.__name)
# c = Classmate()
# # print(c.__name)  # 报错
# c.fn()

# 2.正规方式调用私有方法
# class Classmate:
#     def __sing(self):
#         print('唱出了天籁之音')
#     def dance(self):
#         print('跳舞跳得好')
#         self.__sing()  # 调用私有方法
# c = Classmate()
# c.dance()
