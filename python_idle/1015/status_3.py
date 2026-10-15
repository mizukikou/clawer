# 進入 requests 套件，用來發送 HTTP 請求
import requests

# 💡 額外加入這兩行，用來關閉因為跳過憑證檢查而噴出的警告訊息
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 註解點出核心關鍵：許多網站如果偵測到請求沒有攜帶 User-Agent 瀏覽器特徵，就會拒絕連線
# 某些網站若不帶 User-Agent 會回傳 403

# 定義目標網址，這裡是 PTT 的看板首頁
url = "https://ptt.cc/bbs/index.html"

# 發送最陽春的 GET 請求
# 🎯【核心修正】：加上 verify=False，強迫跳過安全憑證驗證！
res = requests.get(url, verify=False)

# 【核心防禦機制】：專門捕捉被封鎖的 403 訊號
# 如果伺服器回傳的狀態碼等於 403 (Forbidden，代表被伺服器阻擋、拒絕存取)
if res.status_code == 403:
    # 印出人性化的警告，提醒工程師此時該去補上瀏覽器標頭了
    print("糟了！被伺服器拒絕存取（403），可能需要偽裝 User-Agent。")
