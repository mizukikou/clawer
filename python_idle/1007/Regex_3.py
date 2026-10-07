import re

text = "我的分機是 526，他的手機是 0912-345-678，員編是 ABC12345。"

# 提取分機號碼
extension = re.findall(r"\b\d{3}\b", text)  # \b 表示單詞邊界，確保只匹配獨立的三位數字
print(f"分機號碼: {extension}")

# 提取手機號碼
mobile = re.findall(r"\b09\d{2}-\d{3}-\d{3}\b", text)
print(f"手機號碼: {mobile}")

# 提取員編
employee_id = re.findall(r"\b[A-Z]{3}\d{5}\b", text)
print(f"員編: {employee_id}")

content = "活動日期為 2024-10-07，聯絡信箱是 example@example.com。"

# 提取活動日期
date = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", content)
print(f"活動日期: {date}")

# 提取聯絡信箱 .-：允許點 .（如 gmail.）或減號 -（如 soft-bank），{2,}：數量限定詞，代表**「長度至少要 2 個字母以上」
email = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", content)
print(f"聯絡信箱: {email}")