from lxml import etree

# 1. 題目提供的輸入範例 HTML 資料
html_data = """
<div class="shop-wall">
    <div class="item">
        <a href="https://shop.com">
            <img src="https://shop.com">
        </a>
    </div>
    <div class="item">
        <a href="https://shop.com">
            <img src="https://shop.com">
        </a>
    </div>
</div>
"""

# 解析 HTML 字串，建立樹狀結構物件
tree = etree.HTML(html_data)

# 2. 依照題目要求填寫 XPath 路徑
# 題目要求 1：提取所有商品 <a> 標籤的 href 連結字串列表
links = tree.xpath("//a/@href")

# 題目要求 2：提取所有 <img> 標籤的 src 圖片網址字串列表
images = tree.xpath("//img/@src")

# 題目要求 3：使用 zip() 函數將這兩個字串列表組合，並依序印出
for link, img in zip(links, images):
    print(f"商品連結 : {link} -> 圖片網址 : {img}")
