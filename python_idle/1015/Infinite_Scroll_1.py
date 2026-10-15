# 匯入 requests 套件，負責發送網路請求
import requests

# # 假設觀察到捲動會觸發 offset 增加 10

# 🎯【核心大腦】：建立一個專門用來處理「模擬滑動」的自訂函式（Function）
# 參數 offset_limit 代表「你打算往下滾動、累積到跳過多少筆資料為止」
def get_infinite_data(offset_limit):
    
    # 建立一個空的列表，準備拿來集中存放每一次往下捲動時抓到的「所有資料」
    results = []
    
    # 🧩【關鍵進階語法：帶有步長（Step）的 range 迴圈】
    # range(0, offset_limit, 10) 的意思是：從 0 開始，每次增加 10，直到 offset_limit 為止。
    # 假設我們傳入 offset_limit 是 30，那麼變數 offset 就會依序變成：0、10、20。
    # 這完美模擬了：滑第一下（offset=0）、滑第二下（offset=10）、滑第三下（offset=20）
    for offset in range(0, offset_limit, 10):
        
        # 📡【動態拼接網址】
        # 利用 f-string 把每次迴圈跳 10 的 offset 數字塞進 API 的網址裡
        url =  f'https://httpbin.org/get?offset={offset}'
        
        # 發送 GET 請求
        res = requests.get(url)
        
        # 📥【資料解析與集中打包】
        # httpbin.org 會把我們送過去的參數放在 JSON 的 ['args'] 鍵值中。
        # 我們把這一頁（這一下捲動）拿到的字典資料，透過 .append() 塞進一開始建立的 results 大箱子裡。
        results.append(res.json()['args'])
        
    # 當迴圈全部跑完（模擬手滑完了），把裝滿所有分頁資料的大箱子回傳（Return）出來
    return results


# ==========================================
# 🎯 實際呼叫與執行驗收
# ==========================================

# 呼叫剛才寫好的自訂函式，告訴它「我要模擬往下捲動，offset 目標累積到 30」
# 這代表迴圈會跑 3 次（offset=0, 10, 20），results 箱子裡會塞進 3 組資料
data = get_infinite_data(30)

# 使用 len(data) 來測量 results 大箱子裡的封包總數
print(f"總共抓取了 {len(data)} 組封包資料")
# 預期在終端機輸出：總共抓取了 3 組封包資料
