"""
翻页数据关键点   在于 参数的变化

第二页url
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=1&bkn=965445969&r=0.4218
第三页url
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=2&bkn=965445969&r=0.0135
第四页url
https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page=3&bkn=965445969&r=0.0739

观察发现
1.page参数变化
2.r参数变化了

tips
一 发现参数没有规律时  先考虑生成有规律的参数 发送请求尝试！
    1如果能请求到
        不用考虑后面的参数变化
    2.不能请求到
        再考虑后面参数生成

二 可以尝试性的删除一部分参数 尝试看能不能发送请求
      1如果能请求到
        不用考虑后面的参数变化 直接删掉
      2.不能请求到
        再考虑后面参数生成


"""

from jsonpath import jsonpath
import requests
import json

data_list = []
with open(f"评论.json", "w", encoding="utf-8")as file1:
    for i in range(10):
        url=f"https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=292490&filter_rating=0&page={i}"
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
        # 10
        for data in zip(nick_name,content):
            item={
                "nick_name":data[0],
                "content":data[1]
            }
            data_list.append(item)
    #         list>>str
    str_data=json.dumps(data_list,ensure_ascii=False,indent=2)
    file1.write(str_data)








