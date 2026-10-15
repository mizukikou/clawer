# 匯入 requests 套件，負責處理所有的 HTTP 網路請求
import requests

# # 範例 4：處理需要自訂 Header 的非同步請求
# # 部分 AJAX 會檢查 X-Requested-With。

# 定義目標網址。httpbin.org/headers 會把你發送過去的所有 Headers 原封不動地打包回傳給你檢視。
url = "https://httpbin.org/headers"

# 🎯【核心反爬蟲破解：自訂標頭字典】
headers = {
    # 1. 偽裝瀏覽器基本外殼（這裡只寫了簡短的 Mozilla/5.0 作為示範）
    "User-Agent": "Mozilla/5.0",
    
    # 2. 🎯【最核心的 AJAX 認證暗號】：
    # 告訴伺服器：「我是網頁內部的 JavaScript（XMLHttpRequest）發出的非同步請求！」
    # 很多現代網站的 API 只要漏掉這一行，就會直接吐回 403 Forbidden 或 400 Bad Request。
    "X-Requested-With": "XMLHttpRequest"
}

# 📡【發送帶有精準偽裝的面具請求】
# 將剛剛準備好的 headers 字典，傳入到 requests.get() 的 headers 參數中
res = requests.get(url, headers=headers)

# 📥【解析並印出結果】
# 由於 httpbin 會將收到的標頭放在回傳 JSON 的 ['headers'] 欄位中，
# 程式將其轉為字典後精準印出，用來驗收伺服器是否真的有收到我們偽裝的暗號。
print(res.json()['headers'])
