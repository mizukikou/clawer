# 匯入 requests 套件，用來發送 HTTP 請求
import requests

# 定義目標網址。
# httpbin.org/status/404 是專門用來測試的網址，不論誰戳它，它都一定會回傳 404 Not Found 的狀態碼。
url = "https://httpbin.org/status/404" # 模擬一個 404 頁面

# 【核心防禦開始】try 區塊：把可能會出事、出錯的程式碼包在這裡面
try:
    # 向目標網址發送 GET 請求
    res = requests.get(url)
    
    # 🎯 核心關鍵：檢查狀態碼的一鍵快捷鍵！
    # 如果 res.status_code 是 200 正常的範圍，這行會安靜地放行，繼續跑下面的程式。
    # 如果狀態碼是 4xx（客戶端錯誤，如 404）或 5xx（伺服器錯誤，如 500），
    # 這行會【立刻強制拋出】一個名為 HTTPError 的異常，直接中斷 try 區塊！
    
    res.raise_for_status()
    
    # 💡 註：如果上面那一列噴出錯誤，程式會直接「跳走」，這一行之後的 try 內代碼就不會執行。
    print("連線成功，準備解析資料...")

# 【攔截網頁錯誤】except 區塊：專門用來捕捉由 raise_for_status() 丟出來的 HTTPError 異常
# 並將詳細的錯誤原因打包進變數 err 中。
except requests.exceptions.HTTPError as err:
    # 捕捉到錯誤後，不讓程式崩潰跳出紅字，而是優雅地印出我們看得懂的自訂警告訊息
    # 執行結果會印出：連線出錯了：404 Client Error: Not Found for url: ...
    print(f"連線出錯了：{err}")
