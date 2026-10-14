import re

text = "我有 500 元，他有 1200 元"

# 搜尋 1 個以上的數字
result = re.search(r"\d+", text)
print(type(result))  # 輸出: <class 're.Match'> (這是一個物件，不是純文字)
if result:
    # 必須使用 .group() 才能把裡面的文字吐出來
    print(result.group())  # 輸出: '500' (後面那個 1200 直接被忽略)

# 搜尋 1 個以上的數字
result = re.findall(r"\d+", text)
print(type(result))  # 輸出: <class 'list'> (直接回傳一個乾淨的列表)
print(result)        # 輸出: ['500', '1200'] (文字全部都在清單裡了)

# re.search()：只找出「第一個」 符合條件的對象。Match 物件 (找不到則回傳 None)。必須透過 .group() 函數來提取文字。
# re.findall()：找出「所有」 符合條件的對象。回傳型態：List (列表) (找不到則回傳空列表 [])。直接用 索引 [0] 或 for 迴圈 讀取列表。