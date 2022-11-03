"""----------------------------2.cookie介绍----------------------------"""
import requests

URL = "https://www.kkkkkkkkk.com/user/bookshelf/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "cookie": "lf_user_auth=think%3A%7B%22uid%22%3A%22602%22%2C%22username%22%3A%22jiuhaoyyds%22%7D; lf_user_auth_sign=d91a0114ce350b1e7aa9ec7b6bf017599fddd80b; lf_user_recommend=1667475086; lf___forward__=%2F; Hm_lvt_bd48ecec99527fc609704be7dcf3fe88=1667475087; Hm_lpvt_bd48ecec99527fc609704be7dcf3fe88=1667475087"
}
response = requests.get(url=URL, headers=headers)
data = response.content.decode()
print(data)
"""----------------------------3.post的使用----------------------------"""
import requests

urls = "https://www.kkkkkkkkk.com/user/user/login.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
data = {
    "username": "jiuhaoyyds",
    "password": "qwe123.."
}
response = requests.post(url=urls, headers=headers, data=data)
datas = response.content.decode()
print(datas)
"""----------------------------4.session的使用----------------------------"""
import requests

sessions = requests.Session()
urls_login = "https://www.kkkkkkkkk.com/user/user/login.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
data = {
    "username": "jiuhaoyyds",
    "password": "qwe123.."
}
sessions.post(url=urls_login, headers=headers, data=data)
urls = "https://www.kkkkkkkkk.com/user/bookshelf/index.html"
response = sessions.get(url=urls, headers=headers)
datas = response.content.decode()
print(datas)
