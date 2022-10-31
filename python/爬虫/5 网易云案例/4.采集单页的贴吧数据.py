"""
目的 采集https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9E%97%E4%BF%8A%E6%9D%B0&fr=search 对应的数据保存到本地

流程
1 .抓取数据包
2.发送请求 获取响应
3.暂时不清洗  直接保存到本地



"""
import requests

url = "https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9E%97%E4%BF%8A%E6%9D%B0&fr=search"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# 发送请求
response = requests.get(url=url, headers=headers)
data = response.content.decode()
# 数据的保存 保存为html类型的数据
# 因为我们明确的知道 采集的是字符类型的数据 所以可以使用w 形式进行数据保存
with open("林俊杰.html", "w", encoding="utf-8") as file1:
    file1.write(data)
