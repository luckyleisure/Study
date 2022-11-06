# @Time   : 2022/4/23
# @Author : Wilia
"全局变量：在函数的外部"
"局部变量：在函数的内部"
"""
全局作用域：对整个py文件有效；
局部作用域：局部有效
"""
# num = 10
# def fn():
#     age = 20

a = 1
def f1():
    a = 2 #此处不能做a+=1 此类变更运算 除非声明 global全局变量以指代全局变量a=1
    print('f1里面的a', a)
    a += 3  #此处默认为前面的局部变量a=2 进行变量运算
    print(a)
def f2():
    a = 4
    print('f2里面的a', a)
print(a)
f1()
f2()

"修改全局变量:声明  用global ---- 针对不可变对象"
# a = 1
# def fn():
#     global a   # 此处声明a= 2,是对全局变量的a做修改
#     a = 2
#     print(a)
# fn()
# print(a)

# a = 1
# def fn():
#     print(a)   # 全部变量
#     a = 2      # 局部变量
# fn()
# print(a)


# 拓展 ---- 可变对象修改可不做声明
# lst = [1,2,3,4]   # 列表是可变类型
# def f():
#     lst[0] = 88
#     print(lst)
# f()


"用nonlocal 用来声明外层的局部变量"
# a = 10
# def outer():
#     a = 2
#     def inner():
#         nonlocal a             # 声明此处用的是outer中的局部变量
#         print("inner中的a", a)  # 表示的是outer中的局部变量
#         a = 3                  # 表示inner中的局部变量
#     inner()
#     print("outer中的a", a)
# outer()
# print(a)
