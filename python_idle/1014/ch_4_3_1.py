import re  # 匯入 Python 內建的正則表達式模組

# 1. 定義要解析的 log 訊息字串
log_msg = "UserID: admin, Access: 2026-04-16"

# 2. 撰寫 Regex 模式：使用兩個括號擷取目標
# r"UserID:\s*(\w+),\s*Access:\s*(\d{4}-\d{2}-\d{2})" 的詳細結構：
#   - UserID:\s*    : 匹配固定文字 "UserID:" 與後方可能存在的空格
#   - (\w+)         : 【第 1 個括號】匹配 1 個以上的文字/底線（擷取使用者名稱）
#   - ,\s*Access:\s*: 匹配逗號、空格與固定文字 "Access:" 及其後方空格
#   - (\d{4}-\d{2}-\d{2}) : 【第 2 個括號】匹配固定格式的日期（擷取日期）
pattern = r"UserID:\s*(\w+),\s*Access:\s*(\d{4}-\d{2}-\d{2})"

# 3. 使用 re.search() 進行地毯式搜尋
match = re.search(pattern, log_msg)

# 4. 防錯判斷：確保有成功匹配到內容再印出結果
if match:
    # 依題目要求，分別印出 group(1) 與 group(2) 的結果
    print(f"使用者：{match.group(1)} 日期：{match.group(2)}")
else:
    print("找不到符合的格式")
