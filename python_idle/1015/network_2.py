# 匯入 requests 套件，用來發送 HTTP 請求
import requests

# 定義目標網址。httpbin.org/headers 是一個測試工具，
# 它會原封不動地把你發送過去的請求標頭（Request Headers）回傳展示給你。
url = "https://httpbin.org"

# 【關鍵步驟】建立偽裝標頭的字典（Dictionary）
# 這些資料通常是打開瀏覽器 F12 的 Network 面板，從 Request Headers 複製過來的
headers = {
    # 1. 偽裝瀏覽器身分：告訴伺服器這是一個 Windows 10 電腦上的 Chrome 124 瀏覽器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0",
    
    # 2. 偽裝來源網頁：告訴伺服器「我是從 Google 搜尋結果頁面點選連結進來的」
    # 這是破解許多網站「防盜鏈（Anti-Hotlinking）」或圖片防外連的最常用手法
    "Referer": "https://google.com" 
}

# 發送 GET 請求，並透過 headers 參數將我們偽裝好的字典一併送給伺服器
res = requests.get(url, headers=headers)

# 印出伺服器回傳的純文字內容（在 httpbin 中，這裡會顯示你剛剛送過去的 User-Agent 與 Referer）
print(res.text)
