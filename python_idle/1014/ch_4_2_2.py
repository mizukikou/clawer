import re

# 定義 Regex 模式
pattern = r"\d{4}[./-]\d{2}[./-]\d{2}"

# 測試輸入範例 1
text1 = "2026/05/20, 2026-06-15, 2026.07.01"
result1 = re.findall(pattern, text1)

print(result1)  # 輸出: ['2026/05/20', '2026-06-15', '2026.07.01']
