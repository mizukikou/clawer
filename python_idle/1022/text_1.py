# 範例 1. 提取純文字與清理
from lxml import etree
html_str = """
<div class="header">
    <h1> 歡迎來到 Python 爬蟲教室 </h1>
    <p>這是一堂關於 <b>XPath</b> 的課程</p>
</div>
"""

tree = etree.HTML(html_str)
# 1. 提取 h1 的文字 (包含空白)
raw_text_list = tree.xpath("//h1/text()")
raw_text = raw_text_list[0] if raw_text_list else ""
print(f"原始文字 : '{raw_text}'")
# 2. 結合 Python 進行清理
clean_text = raw_text.strip()
print(f"清理後 : '{clean_text}'")
# 3. 提取 p 的文字 (注意:這不會包含 b 標籤裡的 'XPath')
p_text = tree.xpath("//p/text()")
print(f"p 標籤文字清單 : {p_text}")
# 當執行 tree.xpath("//p/text()") 時，在 <p> 這一層只看到了前段和後段兩次直接文字，而 <b> 內部的文字因為屬於下一層，會被直接忽略。
# 由於 xpath() 函數只要抓到多個符合條件的目標，就會把它們裝進「清單（List）」中回傳，因此 Python 就把這兩段獨立的文字分開存放：
# 這兩個字串之間的 ', '，正是 Python 清單用來分隔不同元素的逗號。
