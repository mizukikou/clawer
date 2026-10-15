# 匯入 requests 套件，負責發送網路請求
import requests
# 匯入 time 套件，專門用來控制程式暫停與延遲
import time

# 設定基礎目標網址。httpbin.org/get 會原封不動地把你送過去的參數回傳顯示出來。
base_url = "https://httpbin.org/get"

# # 模擬抓取前三頁

# 🎯【核心控制：翻頁迴圈】
# 使用 range(1, 4) 會產生數字 1, 2, 3（在 Python 中不包含結尾的 4）。
# 變數 page 隨著迴圈執行，會依序變成 1、2、3，藉此模擬使用者點擊第 1、2、3 頁。
for page in range(1, 4):
    
    # 🧩【參數動態打包】
    # 建立一個參數字典（Params Dictionary）。
    # 'page': page -> 將迴圈當前的數字動態帶入，變成 'page': 1, 'page': 2...
    # 'per_page': 10 -> 告訴伺服器「我每一頁只要看 10 筆資料」
    params = {'page': page, 'per_page': 10}
    
    # 📡【發送帶有參數的請求】
    # 使用 requests.get() 的 params 參數，
    # requests 套件會自動幫我們把 params 組合、編碼並黏在 base_url 後方
    # 實際發出的網址會變成：https://httpbin.org?page=1&per_page=10
    res = requests.get(base_url, params=params)
    
    # 在終端機印出目前進度，方便工程師掌握程式進度
    print(f"正在抓取第 {page} 頁...")
    
    # # 實際開發時，我們會在這裡解析 JSON 並存入資料庫
    
    # ⏳【溫柔爬蟲的自我修養】
    # 強迫程式在抓完每一頁後，在原地「僵直/暫停 1 秒鐘」，再進入下一次迴圈。
    # 這是寫爬蟲最重要的禮貌！如果不加這行，Python 會在一秒內對伺服器轟炸數百次請求，
    # 這不僅會造成對方伺服器負擔，也會導致你的 IP 馬上被判定為惡意攻擊而遭到永久封鎖。
    time.sleep(1) 
