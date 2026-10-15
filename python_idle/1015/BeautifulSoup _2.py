from bs4 import BeautifulSoup

# ==========================================
# 🎯 範例 2：兄弟節點的移動 (水平橫移)
# ==========================================
html_table = """
<tr>
    <td class="label">姓名</td>
    <td class="value">張小明</td>
    <td class="label">職稱</td>
    <td class="value">工程師</td>
</tr>
"""

soup_table = BeautifulSoup(html_table, 'html.parser')

# 1. 尋找網頁中的第一個 <td> 標籤（即：<td class="label">姓名</td>）
first_td = soup_table.find('td')

# 2. 🎯【核心大招：橫移找下一個親兄弟】
# .find_next_sibling() 是 BeautifulSoup 專門用來過濾掉「換行空白」的超強指令！
# 它會直接跳過無用的空白文字，精準抓到下一個緊鄰的真實標籤（即：張小明那行 <td>）。
next_td = first_td.find_next_sibling()

print(f"第一個 td 的內容是：{first_td.text}")     # 輸出：姓名
print(f"它的下一個兄弟內容是：{next_td.text}")   # 輸出：張小明


# ==========================================
# 🎯 範例 3：獲取所有祖先 (Parents 向上無限流)
# ==========================================
html_tree = "<html><body><div><p><b id='target'>標籤文字</b></p></div></body></html>"

soup_tree = BeautifulSoup(html_tree, 'html.parser')

# 1. 精準鎖定最內層帶有 id='target' 的 <b> 標籤
b_tag = soup_tree.find(id='target')

# 2. 🎯【核心大招：向上追溯無限宗族】
# .parents (複數) 是一個迭代器，它會從目前節點的爸爸開始，
# 一路向上抓出「爸爸 ➔ 爺爺 ➔ 曾祖父 ➔ 到最外層的 html」，直到天花板為止。
for parent in b_tag.parents:
    # 確保抓到的父層標籤物件存在
    if parent is not None:
        # 印出標籤名稱（.name）
        print(f"上層標籤有：{parent.name}")

# 💡 範例 3 預期輸出結果（由內而外排隊現形）：
# 上層標籤有：p
# 上層標籤有：div
# 上層標籤有：body
# 上層標籤有：html
# 上層標籤有：[document]
