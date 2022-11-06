# @Time   : 2022/4/26
# @Author : Wilia
"__init__方法：通常用来做属性初始化 或 赋值 操作"
# 当该类被实例化的时候会自动执行该函数
# class Hero:
#     # 构造函数
#     def __init__(self):
#         self.name = 'gailun'
#         self.hp = 200  # 生命值
#         self.at = 450  # 攻击力
#     def move(self):
#         print(f'{self.name}正在移动')
#     def attack(self):
#         print(f'{self.name}的生命值是{self.hp}，发出了一招攻击{self.at}')
# # 实例化一个对象
# h1 = Hero()
# h1.move()
# h1.attack()


# 上例优化：让不同对象拥有不同的hp at name---传参
class Hero:
    # 构造函数
    def __init__(self,name,hp,at):
        self.name = name
        self.hp = hp # 生命值
        self.at = at # 攻击力
    def move(self):
        print(f'{self.name}正在移动')
    def attack(self):
        print(f'{self.name}的生命值是{self.hp}，发出了一招攻击{self.at}')
# 实例化一个对象
h1 = Hero('wukong',300,900)
h1.move()
h1.attack()
h2 = Hero('bajie',600,500)
h2.move()
h2.attack()


