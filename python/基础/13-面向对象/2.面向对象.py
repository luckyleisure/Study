# @Time   : 2022/4/26
# @Author : Wilia
"面向过程：关注过程"
"面向对象：关注对象，侧重谁来完成这件事情"
"面向对象思路：封装   继承   多态"

"""
类：就是有相同属性和功能的一类事物 --- 物以类聚，人以群分---抽象概念
对象： 它是类的具体表现，是实实在在的具体事物
"""
# 例：苹果 梨子 香蕉 水果  车厘子 榴莲


"""
类的定义：
class 类名:
		pass

"""
# 类名除了要符合标识符命名规范，习惯上类的命名规则为”大驼峰命名法“(每个单词首字母大写)

# class Hero:  # 或Hero() 或  Hero(object)
#     pass
"创建对象： 对象名 = 类名()"

# 一个类可以创建多个对象
# 实例化一个对象
# h1 = Hero()
# print(h1)  # 打印对象的引用
# print(id(h1))
# h2 = Hero()
# print(h2)
# print(id(h2))

"对象的属性和方法"
"类的三要素： 类名 属性(对对象的特征描述) , 方法(对象具有的行为,是在类中的函数)"

# 例1： jack今年18岁，身高1.88米，喜欢每天早上慢跑。
# 类名 Person  属性：name age height  方法:jogging

# 例2
# class Hero(object):
#     pass
# # 实例化对象
# h1 = Hero()
# # 给对象添加属性
# h1.name = 'jack'
# h1.age = 18
# print(f'名字是{h1.name},年龄是{h1.age}岁')
# h2 = Hero()
# print(f'名字是{h2.name},年龄是{h2.age}岁') # 报错

# 例3： 通过对象获取方法---对象名.方法名()
# class Hero():
#     def move(self):
#         print('正在前往事发地点……')
# h1 = Hero()
# h1.move()

# class hero:
#     def move(self):
#         print('正在前往事发地点')
# h1=hero()
# h1.move()
# 例4：在方法内通过self获取对象的属性
"方法内的第一个参数一定是self,对象会作为实参传递给self"


# class Hero():
#     def move(self):
#         print(f'这位英雄救了一个名叫{self.name}的{self.age}岁小女孩')
# h1 = Hero()
# h1.name = 'rose'
# h1.age = 8
# h1.move()

class Hero():
    def __init__(self):
        self.name="alice"
    def dance(self):
        self.name="lucy"
    def move(self):
        print(f'这位英雄救了一个名叫{self.name}的{self.age}岁小女孩')


h1 = Hero()
# h1.name = 'rose'
h1.age = 8
h1.move()
