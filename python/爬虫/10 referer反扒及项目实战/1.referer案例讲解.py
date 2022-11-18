"""
网址:https://ke.qq.com/course/292490?tuin=d4c97e25
目的:采集腾讯课堂数据案例
采集字段:评论人 评论的信息
保存到json文件

流程
确认数据类型
    json类型     jsonpath
确认数据位置
    都在同一网页


抓包 tips
1在网页上看到了（你要的数据）以后，再去抓包!  不然继续做生成数据包的操作!
2发现网页数据加载是异步加载来的 可以点击fetch/xhr 筛选框进行筛选!


{"msg":"refer错误","type":1,"retcode":100101}
refer错误
请求来源异常!
产生的原因在于没有给服务器指定清楚，这个请求是从哪里来的!
根据产生异常的原因  就可以知道 解决方法是指定请求来源即可!

referer:是发送http请求的过程中 携带在headers里面的参数     useragent  cookie  === referer
referer作用: 表明本次请求是从哪个位置来的    (就是指定一个url) 本次请求是从这个url来的
referer  参数不是固定的      一个请求 可以从多个位置跳转

referer如何获取？
可以在数据包的 requests headers里面复制

"""
from jsonpath import jsonpath
import requests
import json
url="https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=0&bkn=965445969&r=0.0557"

# 请求头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    'cookie': 'tvfe_boss_uuid=3a974c9f273b9598; RK=s5XVhIvR/H; ptcz=571dbff3245ca3b337c7f002d20e8120c92a130b3bc021d419372c3d6ff122d0; ke_login_type=1; ts_uid=8574552847; o_cookie=3569974821; eas_sid=O1C6e417f6R835b7n2p5T6j1c2; ts_refer=www.baidu.com/link; Hm_lvt_0c196c536f609d373a16d246a117fd44=1663929441; p_lskey=000400002e020386d445a9b9a389400afa256eb4587afe4904c6a3ef1ab589cd580ed046e51abf2a14b00d12; pgv_pvid=5242021002; fqm_pvqid=3caf01bf-76f6-4191-bb94-f121ce477188; tdw_data_new_2={"auin":"3569974821","sourcetype":"tuin","sourcefrom":"d4c97e25","ver9":"","uin":"","visitor_id":"7559713451779204","ver10":"","url_page":"","url_module":"","url_position":""}; tdw_data_testid=; tdw_data_flowid=',
    "referer": "https://ke.qq.com/course/292490?tuin=d4c97e25"
}

response=requests.get(url=url,headers=headers).json()
# res_data=response.content.decode()
print(response)
print(type(response))
# 1.评论人
nick_name=jsonpath(response,"$..result.items[*].nick_name")
print(nick_name)
print(len(nick_name))
# 2.评论的信息
content=jsonpath(response,"$..result.items[*].first_comment")
print(content)
print(len(content))
data_list=[]
with open("评论.json","w",encoding="utf-8")as file1:
    for data in zip(nick_name,content):
        item={
            "nick_name":data[0],
            "content":data[1]
        }
        data_list.append(item)
    str_data=json.dumps(data_list,ensure_ascii=False,indent=2)
    file1.write(str_data)

























