import json
raw_json_str = '{"name":"台北天氣","temp":30,"status":"晴"}'
data = json.loads(raw_json_str)
print(data)

for key, value in data.items():
    print(f"{key}：{value}")