import re  # 💡 步驟 1：匯入 Python 內建的正規表達式模組（Regular Expression）

# 💡 步驟 2：準備要拿來搜尋的原始文字字串
test = "電話:0912345678"

# 💡 步驟 3：定義搜尋規則（Pattern）
# \d 代表「任何一個數字」（等同於 [0-9]）
# + 代表「前面的東西必須連續出現 1 次以上」，因為有 +，它會貪婪地繼續往後看。
# 所以 "\d+" 意思就是：幫我找出「連續的一整串數字」
pattern = r"\d+"  # 加了 r，警告就會消失
print(re.findall(pattern, test)) # 💡 使用 re.findall() 可以找出所有符合的片段，回傳一個列表（List）

# 💡 步驟 4：執行搜尋
# re.search() 會在整個 test 字串中從頭開始掃描，尋找「第一個」符合 pattern 規則的片段。
# 如果找到了，它會回傳一個「比對成功物件（Match Object）」；如果找不到，會回傳 None。
# 在這裡，它會略過「電話:」，然後成功捕捉到 "0912345678"
match = re.search(pattern, test)

# 💡 步驟 5：安全檢查（條件判斷）
# 因為如果完全找不到數字，match 的值會是 None，直接取值會導致程式出錯（Crash）。
# 使用 if match: 可以確保「只有在成功找到東西時」才執行接下來的動作。
if match:
    # 💡 步驟 6：取出並印出符合的文字
    # match.group() 是 Match Object 的專屬方法，用來把剛才真正比對成功的「那段文字內容」提取出來。
    # 畫面上將會輸出：0912345678
    print(match.group())

