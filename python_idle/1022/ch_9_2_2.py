from lxml import etree

# 1. 題目提供的輸入範例 HTML 資料
html_data = """
<div class="article-box">
    歡迎來到<b>Python 爬蟲特訓班</b>，本節課我們將深入探討 <span>XPath</span> 的強大進階功能！
</div>
"""

# 解析 HTML 字串，建立樹狀結構物件
tree = etree.HTML(html_data)

# 2. 依照題目提示，使用 string() 函數直接提取特定 div 內部包含的所有文字
# 提示強調：string() 回傳的是一個「單一字串」，而不是列表，因此不需使用 [0] 取值
raw_article = tree.xpath("string(//div[@class='article-box'])")

# 3. 使用 Python 的 .strip() 方法去除頭尾可能產生的換行與空白後印出結果
clean_article = raw_article.strip()

# 印出最終結果
print(clean_article)
