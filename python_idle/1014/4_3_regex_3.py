import re  # 匯入 Python 內建的正則表達式模組

text = "2026-04-16"

# --- 關鍵：具名群組 Regex 語法解析 ---
# 在括號開頭加上 `?P<名字>`，就能為該分組命名！
# pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})" 的詳細結構：
#
# 1. (?P<year>\d{4})  -> 匹配 4 位數字，並將這個群組命名為 "year"
# 2. -                -> 匹配固定的橫線「-」
# 3. (?P<month>\d{2}) -> 匹配 2 位數字，並將這個群組命名為 "month"
# 4. -                -> 匹配固定的橫線「-」
# 5. (?P<day>\d{2})   -> 匹配 2 位數字，並將這個群組命名為 "day"
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"

# 使用 re.search() 在字串中搜尋符合特徵的片段，成功會回傳 Match 物件
match = re.search(pattern, text)

if match:
    # 傳統做法是用數字：match.group(1) 拿年份
    # 具名群組做法：直接傳入字串名字，不用再數括號是第幾個，程式碼一目了然！
    print(match.group("year"))  # 輸出: 2026
    
    # 核心大招：.groupdict() 函數
    # 它會自動把所有「有名字的群組」打包，直接轉換成一個標準的 Python 字典（Dictionary）
    # Key（鍵）就是群組名稱，Value（值）就是匹配到的文字
    print(match.groupdict())  # 輸出: {'year': '2026', 'month': '04', 'day': '16'}

