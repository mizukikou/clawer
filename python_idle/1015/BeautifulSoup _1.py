# 從 bs4（BeautifulSoup 4）套件中，匯入 BeautifulSoup 網頁解析工具
from bs4 import BeautifulSoup

# 定義一段多行的 HTML 網頁純文字字串（模擬從網站抓回來的 HTML 原始碼）
html_doc = """
<div class="container">
    <h1 id="title">課程清單</h1>
    <ul class="course-list">
        <li>Python 基礎</li>
        <li>網路爬蟲實戰</li>
        <li>資料分析入門</li>
    </ul>
</div>
"""

# 🧠【初始化解析器】
# 將 HTML 純文字丟給 BeautifulSoup，並指定使用 Python 內建的 'html.parser' 解析器，
# 將這段文字在記憶體中建立成一棵完整的 DOM 家族樹。
soup = BeautifulSoup(html_doc, 'html.parser')

# 🎯【定位核心起點】
# 使用 .find('ul') 尋找網頁中的第一個 <ul> 標籤，並存入 list_tag 變數。
list_tag = soup.find('ul')


# 👨‍👦【1. 尋找父節點：向上爬】
# .parent 指令會直接找到包在 list_tag (ul) 外面的那層父標籤 (即 div)。
# .name 屬性則是用來撈出這個標籤的「名字」（例如標籤叫 div 就印出 div）。
print(f"ul 的父層是：{list_tag.parent.name}")
# 💡 預期輸出：ul 的父層是：div


# 👶【2. 尋找子節點：向下挖（只看直接下一層）】
# list_tag.children 會把 ul 裡面「直接包裹」的所有親生兒女通通抓出來。
# ⚠️ 注意：.children 原生是一個「迭代器（Iterator）」，不能直接拿來測量長度。
# 必須使用 list() 強制將它轉換為 Python 的「列表 (List)」格式。
children = list(list_tag.children)

# 使用 len() 來測量這個列表內總共有幾個子層節點
print(f"ul 的子層數量：{len(children)}")
# 💡 預期輸出：ul 的子層數量：7 （咦？！為什麼不是 3 個 li 而是 7 呢？請看下方秘密解密！）

# • 在網頁 DOM 結構的標準中，標籤與標籤之間的「換行符號（\n）」和「空白縮排（Indent）」通通會被當作是獨立的「換行文字節點 (NavigableString)」！
# • 我們來數一下 <ul> 裡面的 7 個親生兒女：
# 	1. <ul> 後面的「換行與空格」 ➔ (第 1 個孩子：文字)
# 	2. <li>Python 基礎</li> ➔ (第 2 個孩子：標籤)
# 	3. </li> 後面的「換行與空格」 ➔ (第 3 個孩子：文字)
# 	4. <li>網路爬蟲實戰</li> ➔ (第 4 個孩子：標籤)
# 	5. </li> 後面的「換行與空格」 ➔ (第 5 個孩子：文字)
# 	6. <li>資料分析入門</li> ➔ (第 6 個孩子：標籤)
# 	7. </li> 後面的「換行與空格」 ➔ (第 7 個孩子：文字)
print(f"ul 的所有子層節點（包含文字節點）：{children}")
print(f"ul 的所有子層節點：{[child.name for child in children if child.name is not None]}")
# 這些「換行符號（\n）」或「空白」是沒有標籤名稱的，所以它們的 .name 會是 None。
# 如果我們只想要真正的標籤節點，可以用上面那行 list comprehension 來過濾掉 None。
# ，放在 for 最前面的那個 child.name，代表的是「最後要留下來、放進新列表裡的『結果值』」。
