# 匯入 requests 套件，專門用來處理發送 HTTP 網路請求
import requests

# 定義目標測試網址。httpbin.org/get 會把你送過去的參數與標頭通通打包回傳。
url = "https://httpbin.org/get"

# 🧩【設定 1：網址參數字典】
# 這個參數會被自動黏在網址的最後方，實際發出時網址會變成：.../get?id=12345
my_params = {"id": "12345"}

# 🎭【設定 2：自訂請求標頭字典】
# 這裡修改了 'User-Agent'。範例中老實地寫了 "MyCustomBot/1.0"（我的自訂機器人）。
# 💡 實務上，我們會把這裡換成 Chrome 瀏覽器的長字串，假裝自己是正常人類在瀏覽網頁。
my_headers = {"User-Agent": "MyCustomBot/1.0"}

# 📡【雙劍合璧：發送帶有參數與標頭的 GET 請求】
# 關鍵：同時把 my_params 傳給 params 參數，把 my_headers 傳給 headers 參數。
res = requests.get(url, params=my_params, headers=my_headers)


# 🔍【檢查伺服器收到的內容】
# 1. res.json()：把 httpbin 回傳的內容轉成 Python 字典。
# 2. ["headers"]["User-Agent"]：一路像剝洋蔥一樣，精準挖出伺服器剛才收到的 User-Agent 是什麼。
print(res.json()["headers"]["User-Agent"])

# 💡【最終輸出結果】：
# 程式執行後，終端機會完美印出：
# MyCustomBot/1.0
# 這證明了伺服器確實收到了我們客製化的身分特徵！
