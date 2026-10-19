# ==============================================================================
# 任務：讀取本地端 "task2.html" 檔案，並精準抓取其中所有消費者的評論標題與內容。
# 核心亮點：利用正規表達式 (re.compile) 進行 class 模糊搜尋，完美防止改版漏抓。
# ==============================================================================

import os
import re  # 引入正規表達式模組：爬蟲的文字雷達，負責處理 class 名稱的模糊比對與搜尋
from bs4 import BeautifulSoup  # 網頁解析核心套件，負責將 HTML 純文字轉換成結構化的 DOM 家族樹

# --- 步驟一：動態建立檔案路徑（解決跨平台與 VS Code 執行目錄不同的問題） ---
# 1. os.path.abspath(__file__)：獲取目前這份 Python 腳本檔案的「絕對路徑」
# 2. os.path.dirname(...)：從絕對路徑中，切出該檔案所在的「資料夾路徑」
# 3. os.path.join(..., "task2.html")：把資料夾路徑與檔名串接起來，組出最精準的網頁檔案路徑
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "task2.html")

# --- 步驟二：安全讀取 HTML 檔案 ---
# 使用 with open 語法：好處是當讀取完畢（或中間出錯時），Python 會自動把檔案關閉，釋放系統記憶體
# "r" 代表唯讀模式（Read）；encoding="utf-8" 指定編碼，徹底防止繁體中文網頁讀進來變成亂碼
with open(html_path, "r", encoding="utf-8") as file:
    # 讀取檔案內的所有文字內容，並指派給變數 html_doc（這時候它還只是一大串純文字）
    html_doc = file.read()

# --- 步驟三：初始化 BeautifulSoup 解析器 ---
# 將 HTML 純文字丟給 BeautifulSoup，並指定使用 Python 內建的 'html.parser' 解析器
# 此步驟會在記憶體中建立起完整的 DOM 家族樹，接下來才能使用 .find_all() 進行節點撈取
soup = BeautifulSoup(html_doc, "html.parser")

# --- 步驟四：使用大範圍模糊雷達，搜捕所有評論的「大箱子（完整區塊）」 ---
# class_=re.compile("comment-item|review-item") 翻譯成白話文就是：
# 「只要發現任何標籤的 class 名字裡包含 'comment-item' 或是 'review-item'，通通算數，一律抓回來！」
# 這樣可以一次把網頁上 ThomasKu100、Jason 等人的整塊評論卡片區域全部打包成一個列表（List）
comment_blocks = soup.find_all(class_=re.compile("comment-item|review-item"))

# --- 步驟五：使用 for 迴圈走訪每一個抓到的評論箱子，並用 enumerate 自動編號 ---
# enumerate(..., 1) 的作用是讓迴圈在跑第一輪時 index 從 1 開始計算（1, 2, 3...），方便列印
for index, block in enumerate(comment_blocks, 1):
    
    # 1. 🔍 模糊搜尋標題節點（在目前這個 block 箱子內部，尋找 class 含有 title 或 header 的小標籤）
    title_node = block.find(class_=re.compile("title|header"))
    # 【安全防錯機制】如果有找到標籤，就拿 text 並用 .strip() 剔除髒空白；萬一找不到，就預設填入「（無標題）」
    title_text = title_node.text.strip() if title_node else "（無標題）"
    
    # 2. 🔍 模糊搜尋內容節點（在目前這個 block 箱子內部，尋找 class 含有 detail、content 或 body 的小標籤）
    content_node = block.find(class_=re.compile("detail|content|body"))
    # 【安全防錯機制】如果有找到獨立內容節點就拿文字；
    # 萬一網頁排版沒有獨立節點，則直接把整個箱子的前 100 個字切下來作為替代，確保程式絕對不死機
    content_text = content_node.text.strip() if content_node else block.text.strip()[:100]
    
    # --- 步驟六：漂亮排版列印輸出 ---
    print(f"【評論第 {index} 筆】")
    print(f"👉 標題：{title_text}")
    print(f"💬 內容：{content_text}")
    print("-" * 70)  # 印出 70 個減號作為每筆評論的分隔線，讓畫面一目了然
