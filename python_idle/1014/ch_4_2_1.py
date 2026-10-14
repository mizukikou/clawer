import re

# 題目要求的固定格式：2位區域碼-4位數字-4位數字
pattern = r"\d{2}-\d{4}-\d{4}"

# 測試輸入範例 1
text1 = "我的電話是 02-1234-5678，請撥打。"
result1 = re.findall(pattern, text1)
print(result1)  # 輸出: ['02-1234-5678']

# 測試輸入範例 2
text2 = "台北 02-8888-9999 ，台中 04-2222-3333"
result2 = re.findall(pattern, text2)
print(result2)  # 輸出: ['02-8888-9999', '04-2222-3333']
