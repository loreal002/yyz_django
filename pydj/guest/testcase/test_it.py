import requests

#查询发布会接口
url = "http://127.0.0.1:8000/api/get_event_list/"

r = requests.get(url,params={"eid":"1"})

print(type(r))

result = r.json()

print(type(result))

print(result)

assert result['status'] == 200

assert result['message'] == "success"
assert result['data']['name'] == "小米发布会"
