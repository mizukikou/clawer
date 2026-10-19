# soup.find()&soup.find_all()很難直接做多重 Class 篩選
# ==============================================================================
# 範例 1：基礎選取實作 (CSS Selector 基礎教學)
# 核心觀念：使用 soup.select() (找全部) 與 soup.select_one() (找單個)
#           並用 # 代表 ID，用 . 代表 Class
# ==============================================================================

# 從 bs4 套件中引入 BeautifulSoup 類別，負責解析網頁結構
from bs4 import BeautifulSoup

# 定義一個名為 html 的多行字串，模擬從網路上下載下來的網頁原始碼
html = """
<div id="content">
    <h1 class="title">今日熱門商品</h1>
    <ul class="item-list">
        <li class="item hot">iPhone 15</li>
        <li class="item">PS5 Slim</li>
        <li class="item hot">RTX 4090</li>
    </ul>
    <p id="footer">最後更新：2026-04-22</p>
</div>
"""

# 初始化 BeautifulSoup 解析器，將 HTML 純文字轉換成結構化的 DOM 家族樹
soup = BeautifulSoup(html, 'html.parser')

# ==============================================================================
# # 1. 用 ID 選取：在 CSS 選擇器中，井字號 (#) 專門代表 ID
# ==============================================================================
# soup.select_one() 的特性是「點到為止」：只抓符合條件的「第一個」物件，等同於 .find()
# 傳入 "#footer" 代表尋找網頁中 id="footer" 的標籤
footer = soup.select_one("#footer")

# footer.text：提取該標籤包裹住的純文字內容
print(f"頁尾文字：{footer.text}")


# ==============================================================================
# # 2. 用 Class 選取：在 CSS 選擇器中，點符號 (.) 專門代表 Class
# ==============================================================================
# soup.select() 的特性是「全面搜尋」：抓出「所有」符合條件的標籤，打包成「列表(List)」，等同於 .find_all()
# 傳入 ".item" 代表尋找網頁中所有 class 包含 "item" 的標籤
items = soup.select(".item")

# len(items)：計算列表裡總共有幾個元素（在此範例中，三個 <li> 的 class 都含有 item，所以數量為 3）
print(f"商品數量：{len(items)}")


# ==============================================================================
# # 3. 組合選取：同時具備多個條件（標籤名 + 多個 Class 連續黏在一起）
# ==============================================================================
# 傳入 "li.item.hot" 代表精準篩選：
# 1. 必須是 <li> 標籤
# 2. 必須包含 .item 這個 class
# 3. 必須同時包含 .hot 這個 class
# 💡 注意：Class 與 Class 之間的「.」必須緊緊黏在一起，中間絕對不能有空格！
hot_items = soup.select("li.item.hot")

# 使用 for 迴圈，依序將符合「熱門商品」列表中的每一個 <li> 節點抓出來列印
for hi in hot_items:
    # 這裡會成功印出 iPhone 15 與 RTX 4090，而 PS5 Slim 因為沒有 hot 樣式會被自動過濾
    print(f"熱門商品：{hi.text}")
