# 匯入 requests 套件，這是現代 Python 爬蟲發送網路請求的標準配備
import requests

# 【關鍵修正】：目標 API 網址。
# httpbin.org 規定只有在網址後方明確加上 "/post" 的路徑，才允許接受 POST 請求。
# 之前會噴出 405 Method Not Allowed 錯誤，就是因為網址打錯，戳到了不支援 POST 的頁面。
search_url = "https://httpbin.org/post"

# 準備要傳送給伺服器的表單資料（Payload）
# 以 Python 字典（Dictionary）格式封裝。這裡模擬了我們在網頁搜尋框輸入的關鍵字與頁碼。
payload = {
    "keyword": "Python 課程",
    "page": 2
}

# 準備自訂的請求標頭（Request Headers）
# 主要是帶上 User-Agent，把自己偽裝成一般的 Windows 10 Chrome 瀏覽器，避免被網站當成惡意機器人阻擋。
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0"
}

# 使用 requests.post() 方法發送請求
# 1. 傳入 search_url（去哪裡）
# 2. data=payload：把表單資料塞進 HTTP 的 Body 主體中傳送
# 3. headers=headers：戴上瀏覽器的面具發送
res = requests.post(search_url, data=payload, headers=headers)


print("=== 執行結果與解析 ===")

# 使用 try-except 機制來保護程式。
# 因為 .json() 非常脆弱，只要伺服器回傳的不是標準 JSON 格式（例如網頁 HTML 或錯誤訊息），
# 程式就會直接崩潰噴出 JSONDecodeError。用 try 包起來可以確保程式永遠不會死掉。
try:
    # 嘗試將伺服器回傳的內容，轉換為 Python 可以操作的字典（Dict）
    json_data = res.json()
    
    # 由於 httpbin.org 收到 POST 請求後，會把收到的表單資料放在回傳 JSON 的 'form' 欄位中。
    # 我們使用 .get('form') 或 ['form'] 就能把剛才送過去的關鍵字和頁碼完美撈出來！
    print(f"🎉 請求成功！狀態碼: {res.status_code}")
    print(f"👉 伺服器實際收到的表單參數為: {json_data.get('form')}")

except requests.exceptions.JSONDecodeError:
    # 如果進入到這裡，代表伺服器回傳的還是 HTML 網頁（例如又是 405 或 403 錯誤）
    print(f"❌ 解析失敗！目前的 HTTP 狀態碼為: {res.status_code}")
    print("👉 伺服器回傳的不是 JSON，前 200 個字元為：")
    print(res.text[:200])
