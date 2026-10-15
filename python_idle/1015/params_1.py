# 匯入 requests 套件，專門負責處理發送 HTTP 網路請求
import requests

# 定義基礎目標網址。httpbin.org/get 是一個測試接口，
# 它規定必須使用 GET 方法，並會將接收到的網址參數原封不動地回傳顯示出來。
url = "https://httpbin.org/get"

# 🎯【核心步驟：準備參數字典】
# 將我們要在搜尋框裡輸入的條件，以 Python 字典（Dictionary）格式進行封裝。
payload = {
    "keyword": "python 爬蟲", # 搜尋關鍵字（內含中文與空白欄位）
    "page": 5,                # 指定切換到第 5 頁
    "sort": "desc"            # 指定排序方式為降冪排序（descending）
}

# 📡【使用 params 參數發送請求】
# 將剛剛準備好的 payload 字典，帶入到 requests.get() 的 params 參數中。
# requests 套件此時會在底層自動執行兩件大事：
# 1. 自動把字典轉換為 `?keyword=...&page=5&sort=desc` 的標準網址格式。
# 2. 自動將中文字「爬蟲」與空白字元，轉換為合法的「百分比編碼（URL Encoding）」。
res = requests.get(url, params=payload)

# 印出最終發送出去的完整真實網址，用來驗收 requests 自動組合的效果
print(f"最終請求的網址：{res.url}")

# 💡【輸出結果解析】：
# 程式執行後，您會在終端機看到 res.url 自動變成了：
# https://httpbin.org
# 其中「%E7%88%AC%E8%9F%B2」就是「爬蟲」這兩個中文字轉換後的百分比編碼（Percent-encoding）。
