from lxml import etree

# 測試用 HTML 字串（以輸入範例一為例）
html_str = """
<div class="directory">
    <div class="member-card">
        <span class="name">張經理</span>
        <span class="title">專案主管</span>
    </div>
    <div class="member-card">
        <span class="name">李工程師</span>
        <span class="title">後端開發</span>
    </div>
</div>
"""

# 將字串轉換為可查詢的樹狀結構
tree = etree.HTML(html_str)

# 1. 使用相對路徑找出所有的成員容器 (具有 class='member-card' 的 div)
cards = tree.xpath("//div[@class='member-card']")

# 2. 使用 for 迴圈遍歷每個容器
for card in cards:
    # 3. 在迴圈內部，務必使用局部相對路徑（帶有點點 .），分別提取姓名與職稱的純文字內容
    # 並且記得使用 [0] 取出列表中的字串
    name_list = card.xpath(".//span[@class='name']/text()")
    title_list = card.xpath(".//span[@class='title']/text()")
    
    # 安全檢查：確保有抓到資料再取出，避免 IndexError
    name = name_list[0] if name_list else "未知"
    title = title_list[0] if title_list else "未知"
    
    # 4. 將每位成員的資料格式化印出
    print(f"成員：{name}，職稱：{title}")
