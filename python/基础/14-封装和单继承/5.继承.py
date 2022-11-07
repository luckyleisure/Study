# @Time   : 2022/4/28
# @Author : Wilia
"""
继承的语法：
class 类名(父类名):
    pass
"""

# 单继承：一个子类只能继承一个父类
class God:
    def sing(self):
        print('会唱歌')
    def dance(self):
        print('会跳舞')
class Person(God):  # 继承
    pass
p = Person()
p.sing()
p.dance()
"继承的传递性"


class Animal:                    # 爷爷
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('吃--')
    def drink(self):
        print('喝--')
class Dog(Animal):               # 爸爸
    def bark(self):
        print(f'{self.name}在汪汪叫')
class Black(Dog):                # 儿子
    def fly(self):
        print(f'{self.name}说它会飞')
# 对Black进行实例化对象
b = Black('哮天犬')
b.fly()
b.bark()
b.eat()
b.drink()
print(Black.__mro__)

