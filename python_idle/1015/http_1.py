# 匯入 Python 內建處理 HTTP 協定的底層模組
import http.client

# 【步驟 1】建立連線
# 建立一個與目標網站 (www.google.com) 的 HTTPS 加密連線物件。
# 注意：這裡只建立連線通道，尚未發送任何資料。
conn = http.client.HTTPSConnection("www.google.com")

# 【步驟 2】發送 GET 請求
# 使用 "GET" 方法請求目標網站的根目錄 "/" (即首頁)。
# 這個動作相當於在瀏覽器網址列輸入網址後按下 Enter。
conn.request("GET", "/")

# 【步驟 3】獲取回應
# 接收伺服器處理完後回傳的 HTTP 回應物件，並存入 response 變數中。
response = conn.getresponse()

# 印出 HTTP 狀態碼（例如：200 代表成功、302 代表重新導向）
print(f"狀態碼: {response.status}")

# 印出狀態碼對應的文字原因（例如：OK、Found）
print(f"原因: {response.reason}")

# 【步驟 4】觀察標頭 (Headers)
# 這些標頭是伺服器背後傳遞的元數據（Metadata），包含伺服器型態、安全設定、Cookie 等。
print("--- 回應標頭 ---")

# 使用 response.getheaders() 取得所有標頭鍵值對（以列表包裝元組格式：[(鍵, 值), (鍵, 值)]）
# 透過 for 迴圈逐一解包（Unpacking）並印出每個標頭的名稱與內容
for header, value in response.getheaders():
    print(f"header: {header}: value: {value}")

# 【步驟 5】關閉連線
# 釋放與伺服器之間的網路連線資源，這是一個良好的程式設計習慣。
conn.close()
