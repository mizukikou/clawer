# ==============================================================================
# 題目要求：使用 Pandas 將本地端 "表格範例.html" 中的表格內容轉為 DataFrame，
#           並使用自訂寬度函式，確保中英文符號混排時，所有內容在終端機完美靠左對齊。
# ==============================================================================

# 引入 io 模組：內含 StringIO 工具，這是解決「把 HTML 字串誤判為長檔案路徑」的救星
import io
# 引入 os 模組：用於處理檔案路徑、目錄操作，確保程式在不同作業系統都能正常運行
import os
# 引入 unicodedata 模組：用來判斷字元是否為全形（中文字元佔 2 個字元寬度，數字/英文字母只佔 1 個）
import unicodedata
# 引入 pandas 套件：資料科學的核心套件，負責將 HTML 表格一鍵轉換為結構化的 DataFrame 豆腐塊
import pandas as pd
# 引入 BeautifulSoup 類別：網頁解析的核心套件，負責將 HTML 純文字轉換成結構化的 DOM 家族樹
from bs4 import BeautifulSoup


def pad_display_width(text, width):
    """依「顯示實際視覺寬度」而非純字元數補空白，避免中英文、括號符號混排時欄位對不齊。"""
    display_width = sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in text)
    return text + " " * max(width - display_width, 0)


# --- 步驟一：動態建立檔案路徑（解決跨平台與 VS Code 執行目錄不同的問題） ---
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "表格範例.html")

# --- 步驟二：安全讀取 HTML 檔案 ---
# "r" 代表唯讀模式（Read）；encoding="utf-8" 指定編碼，徹底防止中文網頁讀進來變成亂碼
with open(html_path, "r", encoding="utf-8") as file:
    html_doc = file.read()

# --- 步驟三：初始化 BeautifulSoup 解析器 ---
soup = BeautifulSoup(html_doc, "html.parser")
# .find("table")：在 DOM 樹中由上往下找，抓回最上方的第 1 個 table 表格節點
table_tag = soup.find("table")

# --- 步驟四：檢查並執行 Pandas 轉換 ---
if table_tag:
    # 使用 io.StringIO() 包裹 HTML 字串，避免 Pandas 誤判為長檔案路徑。
    # [0] 代表從回傳的列表中直接取出第一個表格的 DataFrame 物件。
    df_list = pd.read_html(io.StringIO(str(table_tag)))
    # 使用 str() 將這個複雜的節點物件強制轉換成「純 HTML 原始碼字串」（例如字串文字 "<table class="wikitable">...</table>"）。因為接下來的 Pandas 沒辦法直接閱讀 BeautifulSoup 的專屬物件，它只看得懂純文字。
    # pd.read_html()只要看到傳入的是一串字串，第一時間就會預設那是「電腦硬碟裡的檔案路徑。而io.StringIO() 會把傳入的 HTML 純文字字串，在記憶體裡包裝成一個「虛擬的文字檔案串流（String Stream）」
    df = df_list[0]
    
    # --- 步驟五：清洗資料（自動去除前後空白與換行） ---
    # 利用 .map(...) 把整張 DataFrame 裡每一個儲存格的文字都自動執行 .strip()，一線清乾淨。
    df = df.map(lambda x: str(x).strip() if pd.notnull(x) else x)

    # --- 步驟六：精準印出結果（終極靠左對齊修正） ---
    print("欄位名稱：")
    for col in df.columns:
        print(f"- <th_name> {col}")
        
    print('=' * 75)
    print("運算子／描述 分欄整理 (精準靠左對齊)：")
    print('=' * 75)
    
    # 1. 透過 pad_display_width 先印出完美對齊的「欄位標題」
    col_operator = pad_display_width("運算子", 50)
    col_description = "描述"
    print(f"{col_operator}{col_description}")
    print('-' * 75)
    
    # 2. .values 會把 DataFrame 一行一行拆開成陣列
    # df_row[0] 固定對應到左欄「運算子」，df_row[1] 固定對應到右欄「描述」
    for df_row in df.values:
        operator_text = str(df_row[0])
        description_text = str(df_row[1])
        
        # 強制讓左邊的「運算子」不論含有多複雜的特殊符號或中英文，視覺寬度一律固定為 60
        left_aligned_operator = pad_display_width(operator_text, 50)
        
        # 組合印出，右邊的描述就會像排隊一樣，完美地在同一條垂直線上起跑（靠左對齊）
        print(f"{left_aligned_operator}{description_text}")
        
    print('=' * 75)
    
else:
    print("錯誤：在網頁原始碼中找不到 <table> 標籤！")
