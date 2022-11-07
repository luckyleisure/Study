# @Time   : 2022/4/28
# @Author : Wilia
"重写---覆盖"
"""
需要满足的条件： 
1. 继承;
2. 父类与子类的方法名必须相同;
"""
class  Father():
    def myMethod(self):
        print("爸爸的学习方法")
class Child(Father):
    def myMethod(self):
        print('儿子的学习方法')
c = Child()
c.myMethod()


class  Father():
    def __init__(self, play):
        self.play = play
    def myMethod(self):
        print("爸爸的学习方法")
class Child(Father):
    # def __init__(self,play):
    #     self.play=play
    def myMethod(self):
        print('儿子的学习方法',self.play)
c = Child("haha")
c.myMethod()
"""
扩展父类的两种方式 
方法一：父类名.方法(self)
方法二：super().方法名()
"""
class  Father():
    def myMethod(self):
        print("爸爸的学习方法")
class Child(Father):
    def myMethod(self):
        # 方法一：父类名.方法(self)
        # Father.myMethod(self)
        # 方法二：super().方法名()
        super().myMethod()
        print('儿子的学习方法')
c = Child()
c.myMethod()