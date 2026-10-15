# 匯入 requests 套件，用來發送 HTTP 請求
import requests

# 定義目標網址，這裡以 Google 首頁為例
url = "https://google.com"

# 使用 requests.get() 發送 GET 請求，並將伺服器回應的物件存入變數 res
res = requests.get(url)

# 【核心防禦機制】：檢查伺服器回傳的 HTTP 狀態碼 (status_code)
# 狀況 A：如果狀態碼等於 200 (代表連線成功、一切正常)
if res.status_code == 200:
    print("請求成功，開始解析內容...")
    # 💡 實務上，接下來就會在這裡加入 BeautifulSoup(res.text) 開始撈資料

# 狀況 B：如果狀態碼等於 404 (代表找不到網頁，通常是網址、路徑打錯了)
elif res.status_code == 404:
    print("找不到網頁，請檢查網址是否有誤。")

# 狀況 C：除了 200 與 404 以外的其他所有狀況（例如 403 被封鎖、500 伺服器壞掉）
else:
    # 使用 f-string 動態把當前的錯誤狀態碼印出來，方便工程師排查問題
    print(f"出現其他狀況，狀態碼：{res.status_code}")
