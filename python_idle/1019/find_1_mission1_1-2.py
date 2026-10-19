# ==============================================================================
# 題目要求：分別使用 .find() 與 .find_all() 方法來尋找檔案 "表格範例.html"中 
#           欄位名稱（th） & "td"的內容，td的內容要排列整齊。
# ==============================================================================

# 引入 os 模組：用於處理檔案路徑、目錄操作，確保程式在不同作業系統（Windows/Mac）都能正常運行
import os
# 引入 unicodedata 模組：用來判斷字元是否為全形（中文字元佔 2 個字元寬度，數字/英文字母只佔 1 個）
import unicodedata
# 引入 BeautifulSoup 類別：網頁解析的核心套件，負責將 HTML 純文字轉換成結構化的 DOM 家族樹
from bs4 import BeautifulSoup


def pad_display_width(text, width):
    """依「顯示寬度」而非字元數補空白，避免中英文混排時欄位對不齊。"""
    display_width = sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in text)
    return text + " " * max(width - display_width, 0)
    #  W (Wide)：代表「寬字元」，也就是繁體中文、簡體中文、日文、韓文等。
    #  F (Fullwidth)：代表「全形字元」，例如全形的驚嘆號 ！ 或全形空格。
    # width - display_width：用你想要的總目標寬度，減掉這串字實際吃掉的視覺寬度，算出來的差額就是「該補幾個空格」
# --- 步驟一：動態建立檔案路徑（解決跨平台與 VS Code 執行目錄不同的問題） ---
# 1. os.path.abspath(__file__)：獲取目前這份 Python 腳本檔案的「絕對路徑」
# 2. os.path.dirname(...)：從絕對路徑中，切出該檔案所在的「資料夾路徑」
# 3. os.path.join(..., "表格範例.html")：把資料夾路徑與檔名串接起來，組出最精準的網頁檔案路徑
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "表格範例.html")

# --- 步驟二：安全讀取 HTML 檔案 ---
# 使用 with open 語法：好處是當讀取完畢（或中間出錯時），Python 會自動把檔案關閉，釋放系統記憶體
# "r" 代表唯讀模式（Read）；encoding="utf-8" 指定編碼，徹底防止中文網頁讀進來變成亂碼
with open(html_path, "r", encoding="utf-8") as file:
    # 讀取檔案內的所有文字內容，並指派給變數 html_doc（這時候它還只是一大串純文字）
    html_doc = file.read()

# --- 步驟三：初始化 BeautifulSoup 解析器 ---
# 將 HTML 純文字丟給 BeautifulSoup，並指定使用 Python 內建的 'html.parser' 解析器
# 此步驟會在記憶體中建立起完整的 DOM 家族樹，接下來才能使用 .find() 或 .find_all()
soup = BeautifulSoup(html_doc, "html.parser")

# --- 步驟四：使用 .find_all() 尋找所有 <th> 標籤（表格的欄位名稱） ---
# .find_all("th") 會搜出網頁中「所有」的 <th> 標籤，並包裝成一個「列表（List-like Object）」回傳
#-------- 任務一：尋找所有欄位名稱（th）並列印
all_th = soup.find_all("th")
print("欄位名稱：")

# 使用 for 迴圈，把找到的每一個 <th> 標籤物件依序抓出來處理（暫時命名為 th）
for th in all_th:
    # th.name：抓取目前節點的標籤名稱，結果固定為字串 "th"
    # th.text：抓取該標籤包裹住的文字內容
    # .strip()：極其關鍵！自動剃除文字前後看不見的「換行符號(\n)」與「空白」，達到排列整齊的效果
    print(f"- <{th.name}> {th.text.strip()}")

# --- 步驟五：使用 .find() 尋找「第一個」 <td> 標籤 ---
# .find("td") 的特性是「點到為止」：它在 DOM 樹中由上往下找，只要摸到第一個 <td> 就立刻回傳該物件
# 如果網頁裡有 100 個 td，它也只會抓回最上方的第 1 個。如果找不到，則會回傳 None
first_td = soup.find("td")
# --- 步驟六：依「列（tr）」分組，把每列的 td 分別歸類到 運算子／描述 兩欄 ---
# 表格每個 <tr> 資料列固定是「第 1 個 td = 運算子，第 2 個 td = 描述」，
# 若直接用 find_all("td") 攤平成一條列表，會看不出哪個 td 屬於哪一欄，所以改成逐列（tr）取出 td。
print("運算子／描述 分欄整理：")
print('=' * 60)
all_tr = soup.find_all("tr")
for tr in all_tr:
    # -------------------任務二：找出所有的 td -------------------
    tds = tr.find_all("td")
    # 表頭那一列只有 th 沒有 td，tds 會是空列表，略過即可
    if len(tds) < 2:  
        continue
    operator, description = tds[0].text.strip(), tds[1].text.strip()
    print(f"運算子：{pad_display_width(operator, 50)}描述：{description}")

