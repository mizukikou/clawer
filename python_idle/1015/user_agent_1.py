# 匯入 requests 套件，專門用來處理發送 HTTP 網路請求
import requests

# 定義目標測試網址。
# httpbin.org/headers 是一個專門用來「照妖鏡」的測試接口，它會原封不動地把你發送過去的 Headers 回傳。
url = "https://httpbin.org/headers"

# 🎭【核心步驟：定義標頭字典】
# 建立一個名為 headers 的字典，將關鍵字 'User-Agent' 設定為一般人類瀏覽器的特徵字串。
headers = {
    # 這串超長的字串就是標準的瀏覽器指紋（User-Agent 字串）：
    # Windows NT 10.0 -> 代表作業系統是 Windows 10
    # Chrome/124.0.0.0 -> 代表瀏覽器是 Chrome 124 版本
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# 📡【發送帶有面具的 GET 請求】
# 將準備好的 headers 字典帶入 requests.get() 的 headers 官方指定參數中。
res = requests.get(url, headers=headers)

# 🔍【檢查並印出伺服器收到的內容】
# res.json()：將 httpbin 回傳的測試報告轉為 Python 字典。
# ["headers"]["User-Agent"]：精準撈出伺服器最終在網路上看到的「你是誰」。
print(res.json()["headers"]["User-Agent"])

# 💡【最終輸出結果】：
# 程式執行後，終端機會完美印出：
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 ... Chrome/124.0.0.0 Safari/537.36
# 這代表對方伺服器已經被我們成功騙過去，誤以為這個請求是由一個真人打開 Chrome 瀏覽器所發出的！
