import requests


with open(r"G:\我的雲端硬碟\Crawler\課程資料\筆記\20261007\API_KEY.txt", "r") as file:
    api_key = file.read().strip()

url = f"http://api.openweathermap.org/data/2.5/weather?lat=25.0330&lon=121.5654&appid={api_key}"  

response = requests.get(url)
data = response.json()
print(data)