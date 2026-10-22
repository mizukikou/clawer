# 範例 3. 同時選取多個節點的文字 XPath

# 從 lxml 套件中匯入 etree 模組（用於解析 HTML 並支援 XPath 語法）
from lxml import etree

# 定義一個名為 html 的多行字串，模擬清單（ul / li）的網頁結構
html = """
<ul>
    <li id="id_01">項目一</li>
    <li id="id_02">項目二</li>
    <li id="id_03">項目三</li>
</ul>
"""

# 使用 etree.HTML() 解析 HTML 字串，建立一個可供 XPath 查詢的樹狀結構物件 (ElementTree)
tree = etree.HTML(html)

# # 抓取所有 li 的 id 屬性與文字

# 使用 xpath() 尋找所有 <li> 標籤，並使用 `@id` 提取它們的 id 屬性值
# 關鍵語法：`//li/@id` 會回傳一個包含所有 id 的字串清單
ids = tree.xpath("//li/@id")

# 使用 xpath() 尋找所有 <li> 標籤，並使用 `/text()` 提取標籤內部的直接純文字
# 關鍵語法：`//li/text()` 會回傳一個包含所有項目文字的字串清單
texts = tree.xpath("//li/text()")

# # 使用 zip 縫合資料

# 使用 Python 內建的 zip() 函數，將 ids 和 texts 兩個獨立清單「像拉鍊一樣」一一對齊配對
# 每次迴圈會同時取出同一個位置的 id（賦值給變數 i）與文字（賦值給變數 t）
for i, t in zip(ids, texts):
    # 使用 f-string 格式化字串，將編號與內容組合並列印輸出到終端機
    print(f"編號 : {i} | 內容 : {t}")
