import json
api_res = '{"count":1,"data":[{"title":"今日新聞","likes":99}]}'
data = json.loads(api_res)
print(data["data"][0]["title"], data["data"][0]["likes"])
