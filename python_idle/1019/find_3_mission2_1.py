# 引入必要的套件
import os
from bs4 import BeautifulSoup

# 1. 組出檔案路徑
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "評論範例.html")

# 2. 讀取檔案（因為網頁本身標註 Big5，我們可以用 cp950 或 utf-8 嘗試，讀得通最重要）
with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# 3. 初始化 BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# 4. 重新尋找這份網頁「真正存在」的結構標籤
# 檢查原始碼發現：評論的標題藏在 <h3 class="comment-item-header-title"> 裡面
title = soup.find("h3", class_="comment-item-header-title")

# 評論的內文主要藏在 <article> 或是 class="comment-item-detail" 的 <div> 裡面
content = soup.find("div", class_="comment-item-detail")

# 5. 安全列印：使用 if 判斷式，確保就算漏抓也絕對不會噴紅字錯誤
title_text = title.text.strip() if title is not None else "（找不到評論標題標籤）"
content_text = content.text.strip() if content is not None else "（找不到評論內文標籤）"

print(f"評論標題：{title_text}")
print(f"評論內容：{content_text}")
