import re  # 💡 步驟 1：匯入正規表達式模組

# 💡 步驟 2：定義搜尋規則
# 使用 r"..." 建立原始字串，避免 Python 3.12+ 噴出無效跳脫字元警告
# \d 代表數字，+ 代表連續出現 1 次以上（適當的量詞）
pattern = r"\d+"

# === 測試輸入範例 1 ===
text1 = "產品編號 A5566，價格是 1200 元"
# re.findall() 會掃描整段文字，把所有符合 \d+ 的數字片段通通抓出來，放到 List 中
result1 = re.findall(pattern, text1)
print(f"輸出範例 1 : {result1}")  # 預期輸出: ['5566', '1200']


# === 測試輸入範例 2 ===
text2 = "今天是 2026 年 5 月 12 日"
result2 = re.findall(pattern, text2)
print(f"輸出範例 2 : {result2}")  # 預期輸出: ['2026', '5', '12']
