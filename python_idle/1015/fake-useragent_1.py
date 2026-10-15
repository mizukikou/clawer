# 【重要前提】：這個功能需要額外安裝第三方套件。
# 必須先在終端機（Terminal）執行指令：pip install fake-useragent

# 從 fake_useragent 套件中，單獨匯入 UserAgent 這個專門用來生成隨機名稱的類別
from fake_useragent import UserAgent
# 匯入標準的 requests 網路請求套件
import requests

# 🎯【核心步驟 1：初始化產生器】
# 實例化一個 UserAgent 物件，存入變數 ua 中。它可以被想像成一個「千面人面具庫」。
ua = UserAgent()

# 🎭【核心步驟 2：動態生成隨機標頭】
# 呼叫 ua.random 屬性。
# 關鍵：每次程式跑到這一行，ua.random 都會隨機抽出一串目前世界上真實存在、且最新的瀏覽器特徵字串！
headers = {
    "User-Agent": ua.random  # 每次執行或每次跑迴圈，這裡的值都會完全不同
}

# 📡【發送請求】
# 戳 httpbin.org/user-agent 節點，它會直接回傳我們這次送過去的 User-Agent 到底長怎樣
res = requests.get("https://httpbin.org/user-agent", headers=headers)

# 印出結果進行驗收
print(f"本次隨機身分：{res.text}")

# 💡【連續執行的神奇效果】：
# 如果您把這段程式碼多執行幾次，您會發現每次印出來的結果都驚奇地不一樣：
# 第 1 次執行：... Chrome/120.0.0.0 ...（假裝自己是 Chrome）
# 第 2 次執行：... Firefox/118.0 ...   （假裝自己是 Firefox）
# 第 3 次執行：... Safari/605.1.15 ... （假裝自己是蘋果 Mac 的 Safari）
