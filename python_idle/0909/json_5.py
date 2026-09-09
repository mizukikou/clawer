import json
import requests
import urllib3

url = "https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/106/94b0e54b-ad45-4222-b26c-648773794ded.json"
try:
    response = requests.get(url, timeout=10, verify=False)
    data = response.json()
except requests.RequestException as e:
    print(f"Error fetching data: {e}")
    data = []

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    for item in loaded_data:
        print(f"機構名稱：{item['機構名稱']}, 電話：{item['電話']}")
        

