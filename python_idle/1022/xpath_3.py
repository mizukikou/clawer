from lxml import etree

# 1. 建立具有 3 個 div，每個 div 下各有 3 個 li 的 HTML 結構
html = """
<div>
    <ul>
        <li>第一組 - 項目 A</li>
        <li>第一組 - 項目 B</li>
        <li>第一組 - 項目 C</li>
    </ul>
</div>
<div>
    <ul>
        <li>第二組 - 項目 D</li>
        <li>第二組 - 項目 E</li>
        <li>第二組 - 項目 F</li>
    </ul>
</div>
<div>
    <ul>
        <li>第三組 - 項目 G</li>
        <li>第三組 - 項目 H</li>
        <li>第三組 - 項目 I</li>
    </ul>
</div>
"""

tree = etree.HTML(html)

print("--- 情境一：一次抓取全部 9 個 li 的文字 ---")
# 使用 // 靈活跳轉，不管在第幾個 div，只要是裡面的 li 通通抓出來
all_targets = tree.xpath("//div//li/text()")
print(f"全部項目列表：{all_targets}")
print(f"總共抓到 {len(all_targets)} 個項目\n")


print("--- 情境二：利用迴圈，一組一組（div）分開處理 ---")
# 先抓出 3 個 div 節點
div_s = tree.xpath("//div")
# 加上 enumerate() 後，Python 會把列表裡的每個元素強行配上一個數字，打包成 (數字, 元素) 的組合。
for index, div in enumerate(div_s, start=1):
    # 注意！這裡要使用「局部路徑查找」，前面必須加一個點「.」
    group_items = div.xpath(".//li/text()")
    print(f"第 {index} 個 div 內部的項目：{group_items}")
print("\n")


print("--- 情境三：精準定位，只抓特定某個項目 ---")
# 語法說明：XPath 的索引值是從 1 開始計算（不是 0）
# 範例：抓取第 2 個 div 裡面的第 3 個 li
specific_target = tree.xpath("//div[2]//li[3]/text()")
if specific_target:
    print(f"第 2 個 div 的第 3 個項目是：{specific_target[0]}")
