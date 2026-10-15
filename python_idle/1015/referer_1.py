# 匯入 requests 套件，負責發送網路請求
import requests

# 定義測試網址。httpbin.org/headers 會原封不動回傳收到的所有 Headers 供我們檢視。
url = "https://httpbin.org/headers"

# 🎭【核心大腦：多重偽裝標頭字典】
headers = {
    # 1. 偽裝瀏覽器身分：告訴伺服器我是 Windows 10 的 Chrome 124 瀏覽器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0",
    
    # 2. 🎯【關鍵進階偽裝：自訂來源網頁】
    # 告訴伺服器：「我是先在 Google 搜尋，然後從搜尋結果點擊連結跳轉進來的用戶！」
    # 這是破解許多網站「防盜鏈（Anti-Hotlinking）」或圖片防外連最常用的必殺技。
    "Referer": "https://google.com/"
}

# 📡【發送帶有雙重面具的 GET 請求】
res = requests.get(url, headers=headers)

# 🔍【解析並印出結果】
# 1. res.json()['headers']：拿到伺服器收到的所有標頭字典
# 2. .get('Referer')：精準取出 Referer 欄位的值並格式化印出
print(f"伺服器看到的來源頁面：{res.json()['headers'].get('Referer')}")

# 💡【最終輸出結果】：
# 程式執行後，終端機會完美印出：
# 伺服器看到的來源頁面：https://google.com
# 這證明對方伺服器完全相信了你是從 Google 點選進來的，成功放行！
