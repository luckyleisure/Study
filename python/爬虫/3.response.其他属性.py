"""




"""
import requests

# 查看常见的响应码
# 响应码的作用   可以判断时候执行业务逻辑
# 200 403
url="https://www.baidu.com/"
response=requests.get(url=url)
# 返回响应码
code=response.status_code
print(code)  #200
print(type(code))  #<class 'int'>
# 可以拿来进行判断
if code ==200 :
    print("执行清洗数据的方法")
    print("执行保存数据的方法")
else:
    print("本次响应码是"+str(code))
    print("不进行数据清洗 保存")

# 查看请求头信息 本次请求的身份 是以一个什么身份去请求的
# response.request.headers
headers=response.request.headers
print(headers)
# 'python-requests/2.26.0'

# {'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}











