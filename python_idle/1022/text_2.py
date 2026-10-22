# 範例 2. 提取多個屬性值 (連結與圖片)

# 從 lxml 套件中匯入 etree 模組（用於解析 HTML 並支援 XPath 語法）
from lxml import etree

# 定義一個名為 html 的多行字串，模擬含有圖片牆（gallery）的網頁結構
html = """
<div class="gallery">
    <a href="https://example.com">
        <img src="thumb1.jpg" alt="圖片 1">
    </a>
    <a href="https://example.com">
        <img src="thumb2.jpg" alt="圖片 2">
    </a>
</div>
"""

# 使用 etree.HTML() 解析 HTML 字串，建立一個可供 XPath 查詢的樹狀結構物件 (ElementTree)
tree = etree.HTML(html)


# -------------------------------------------------------------------------
# # 1. 抓取所有連結
# -------------------------------------------------------------------------

# 使用 xpath() 尋找所有 <a> 標籤，並使用 `@href` 提取其超連結屬性的值
# 關鍵語法：在 XPath 中，`@` 代表「選取屬性」
links = tree.xpath("//a/@href")

# 格式化輸出結果。因為網頁中有兩個 <a> 標籤，會回傳包含兩個網址的字串清單
print(f"所有連結 : {links}")


# -------------------------------------------------------------------------
# # 2. 抓取所有圖片的替代文字 (alt)
# -------------------------------------------------------------------------

# 使用 xpath() 尋找所有 <img> 標籤，並使用 `@alt` 提取其圖片替代文字（描述）屬性的值
alts = tree.xpath("//img/@alt")

# 格式化輸出結果。同樣會依序抓到兩張圖片的 alt 屬性，並打包成字串清單回傳
print(f"圖片描述 : {alts}")
# 使用 zip() 將兩個清單對齊合併
for link, alt in zip(links, alts):
    print(f"圖片：{alt} -> 點擊前往：{link}")

# 執行輸出：
# 圖片：圖片 1 -> 點擊前往：https://example.com
# 圖片：圖片 2 -> 點擊前往：https://example.com

