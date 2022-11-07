# @Time   : 2022/4/28
# @Author : Wilia

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def dance(self):
        print(f'名叫{self.name}的同学，年龄是{self.age}岁，喜欢跳舞')
s1 = Student('摇',19)
s1.dance()
s2 = Student('醉宝宝',16)
s2.dance()

"""
模拟士兵使用某种型号的枪进行射击
1.判断是否有子弹，没有子弹无法射击
2.使用 print 提示射击，并且输出子弹数量
用类来进行实现。
思路:
类的三要素：
类名 ： Soldier
属性 :  士兵名字name  某种型号的枪 model  子弹数量 num
方法 :  射击 shoot
"""
class Soldier():
    def __init__(self,name,model,num):
        self.name = name    # 射击人
        self.model = model  # 枪的型号
        self.num = num      # 子弹的初始值
    def shoot(self):
        # 判断子弹的数量
        if self.num <= 0:
            print('没有子弹了……')
        else:
            self.num -= 1
            print(f'{self.name}使用了{self.model}的枪射击了,目前还剩{self.num}颗子弹')
s1 = Soldier('david','ak47',5)
s1.shoot()   # 调用射击方法一次，表示射击一次
s1.shoot()
s1.shoot()
s1.shoot()
s1.shoot()
s1.shoot()
s1.shoot()
s1.shoot()




