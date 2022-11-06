# @Time   : 2022/4/23
# @Author : Wilia
"即使语句或表达式使用了正确的语法，执行时仍然有可能触发错误。那这个执行时检测到的错误称为异常"
"异常要达到的效果：通过异常处理机制，使用有异常的后面的代码能够正常执行"
# num = int(input('请输入一个整数：'))
# print(num)

# 格式一：try  …… except
'''
语法格式一：
try:
    可能引发异常现象的代码  
         #不确定是否能够正常执行的代码
except 异常类型：
    出现异常现象的处理代码  
         #出现异常时希望执行的代码
'''
# try:
#     print(a)
# except:
#     print('出现错误')
# print(123)
# print(456)
# a = 1
# try:
#     print(a)
# except Exception as error:
#     print(error)
# else:
#     print('没有异常')
'''
语法格式二:
    try:	必选
        可能引发异常现象的代码
    except:
            出现异常现象的处理代码
    else:	可选
            未出现异常现象的处理代码
'''
# dic = {'name': 'zs'}
# try:
#     print(dic['id'])
# except Exception:  # Exception 常见异常基类  ,except是用来捕捉异常的
#     print("出现错误")
# else:
#     print('没有捕获到异常')

'''
语法格式三:
    try:
            可能引发异常现象的代码
    except: (可以没有)
            出现异常现象的处理代码
    finally:
            try代码块结束后运行的代码
'''
try:
    print(a)
except NameError:
    print('出现错误')
finally:
    print('无论有无异常都会执行的代码')

# try:
#     print(a)
# except KeyboardInterrupt:
#     print('出现错误')
# finally:
#     print('无论有无异常都会执行的代码')

'''
语法格式四:
    try:	必选
        可能引发异常现象的代码
    except:	必选: 二选一
            出现异常现象的处理代码
    else:	可选
            未出现异常现象的处理代码
    finally:	必选:二选一
            try代码块结束后运行的代码
'''
# try:
#     n = int(input('请输入一个整数：'))
#     print(10 / n)
# except ValueError:
#     print('请输入正确的数据')
# except Exception as e:  # as取别名
#     print(f'未知错误{e}')
# else:
#     print('没有异常时才执行的代码')
# finally:
#     print('无论有无异常都会执行的代码')

"异常的传递"

# def f1():
#     return int(input('请输入整数'))
#
#
# def f2():
#     return f1()
#
#
# try:
#     print(f2())
# except Exception as e:
#     print(f'错误{e}')
# print('哈哈')

"主动抛出异常"
"""
步骤：
1.创建一个Exception('×××')的对象，×××表示的异常提示信息
2.raise 抛出这个对象
"""
"一旦执行了raise语句,其内部raise后面的语句就不会执行了"
# def funa():
#     raise Exception('抛出一个异常')
#     print("哈哈")
# funa()

"事例：密码长度如果小于6，则提示长度不够；否则输出这个密码；提示：使用异常处理机制"

# def user():
#     # pwd = input('请输入密码')
#     pwd = '123'
#     if len(pwd) >= 6:
#         return pwd
#     else:
#         ex = Exception('密码长度不够')
#         raise ex
#
#
# try:
#     upwd = user()
#     print(upwd)
# except Exception as e:
#     print(f'错误:{e}')

"""_________________________________________________________"""

# def user():
#     ex = Exception('抛出一个异常')
#     raise ex
#     return ex
#
#
# try:
#     upwd = user()
#     print(upwd)
# except Exception as e:
#     print(f'错误:{e}')
