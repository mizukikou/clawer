# 讀取與本 Python 檔案放在同一個資料夾的 Task2.html，
# 找出所有具有 href 屬性的 <a> 超連結，並印出各連結的文字與網址。
import os
from bs4 import BeautifulSoup

# __file__ 是目前這個 Python 腳本的檔案路徑。
# abspath() 將路徑轉成絕對路徑，dirname() 再取出腳本所在資料夾。
# 最後用 join() 組出同資料夾內 HTML 檔案的完整路徑，避免依賴執行時的工作目錄。
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "task2.html")

# 使用 with 管理檔案，讀取結束後會自動關閉檔案。
# 指定 utf-8 可正確解碼 HTML 中的中文等文字。
with open(html_path, "r", encoding="utf-8") as f:
    # BeautifulSoup 讀入 HTML 原始內容，並使用 Python 內建的 html.parser 解析標籤結構。
    soup = BeautifulSoup(f, "html.parser")

# CSS 選擇器 a[href] 代表：選取所有具有 href 屬性的 <a> 標籤。
# 不含 href 的 <a> 不會被選中；select() 回傳符合條件的標籤清單。
for a_tag in soup.select("a[target]"): # 某個連結沒有 href 屬性，BeautifulSoup 就會引發 KeyError: 'target'
# for a_tag in soup.select("a[href]"): # 某個連結沒有 target 屬性，BeautifulSoup 就會引發 KeyError: 'target'
    # text 取得標籤內的可見文字，例如 <a href="...">連結文字</a> 中的「連結文字」。
    print("text:", a_tag.text)
    # 以屬性名稱取出 href 值，也就是超連結的目標網址。
    print("href:", a_tag['href'])
    print("target:", a_tag['target'])
