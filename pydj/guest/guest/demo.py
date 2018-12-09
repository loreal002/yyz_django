# import requests
# from datetime import datetime
# url = "http://127.0.0.1:8000/api/add_event/"
#
#  # eid = request.POST.get('eid','') # 发布会 id
#  #    name = request.POST.get('name','') # 发布会标题
#  #    limit = request.POST.get('limit','') # 限制人数
#  #    status = request.POST.get('status','') # 状态
#  #    address = request.POST.get('address','') # 地址
#  #    start_time = request.POST.get('start_time','') # 发布会时间
#
#  #YYYY-MM-DD HH:MM:SS
# data = {"eid":'4',"limit":500,"address":"shanghai","start_time":"2018-09-18 14:00:00","name":"小米发布会"}
# res = requests.post(url=url,data=data)
# print(res.json())

# import configparser
# import ConfigParser
#
# cf = ConfigParser.ConfigParser()

import requests
import json
import collections

# data = {
#     "eid":"1",
#     "realname":"davia",
#     "phone":"13122002200",
#     "email":"david@mail.com"
#
# }
#
# url = "http://127.0.0.1:8000/api/add_guest/"
#
# r = requests.post(url,json=data)
#
# print(r.content.decode('utf-8'))
#
# url = 'http://127.0.0.1:8000/api/add_event/'
#
# data = {
#     "eid":7,
# 	"name":"华为手机发布会",
# 	"limit":3000,
# 	"status":1,
# 	"address":"南京华为研究所",
# 	"start_time":"2018-12-05 06:00:00.000000"
# }
#
# r = requests.post(url,data=data)
# print(r.json())
colors = ["black","red"]
sizes = ["S","M","L"]
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)
collections.namedtuple()
