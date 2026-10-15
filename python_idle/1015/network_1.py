# 匯入 requests 套件，這是現代 Python 爬蟲最主流、最好用的 HTTP 請求庫
import requests

# 【步驟 1】定義從網頁開發者工具 (F12) 的 Network (網路) 面板中所監聽到的真實 API 網址
# 這是 Coinbase 交易所提供查詢「比特幣 (BTC) 對美金 (USD) 現貨價格」的公開 API 節點
api_url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

# 【步驟 2】向 API 網址發送 HTTP GET 請求，並將伺服器回傳的 Response 物件存入變數
response = requests.get(api_url)

# 【步驟 3】將回傳的 JSON 格式字串直接解析並轉換為 Python 的「字典 (dict)」結構
# 這樣一來，我們就可以用點選或鍵值（Key）的方式直接存取裡面的欄位資料
data = response.json()

# 【步驟 4】使用 f-string 格式化字串，並依照 JSON 的層級結構取出所需的資料
# 根據該 API 的結構，真實數據包裹在 'data' 這個大外殼內：
# data['data']['amount']   --> 取出價格數字（例如：96500.50）
# data['data']['currency'] --> 取出貨幣單位（例如：USD）
print(f"目前比特幣價格: {data['data']['amount']} {data['data']['currency']}")
