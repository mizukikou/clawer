from lxml import etree
html = """
<div class="user-card">
    <span class="name">老王</span>
</div>
<div class="user-card">
    <span class="name">小李</span>
</div>
"""

tree = etree.HTML(html)
# 在 XPath 中，@ 代表屬性的意思。程式只保留 class 屬性剛好等於 'user-card' 的那些 <div>。
cards = tree.xpath("//div[@class='user-card']")
for card in cards:
    # 注意這裡的 .// 代表「從當前節點開始找」
    # 若沒加點，會變成從整份文件的開頭找
    name = card.xpath(".//span/text()")
    print(f"使用者：{name[0]}")
