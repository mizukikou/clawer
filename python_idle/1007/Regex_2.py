import re

# 💡 步驟 1：建立全台灣英文字母與代號的對照字典（Dictionary）
# 包含已經停招的縣市代碼（例如：台中縣 L、台南縣 R、高雄縣 Y）也完整保留，確保舊身份證可驗證。
letter_map = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
    'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23,
    'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30,
    'Y': 31, 'Z': 33
}

# 💡 步驟 2：輸入要驗證的身份證字號（可自由更改測試，英文大小寫皆可）
id_number = "A123456789"  # 範例：A 代表台北市 [1]

print(f"原始輸入: {id_number}")

# 💡 步驟 3：使用 Regex 先行檢查格式
# ^[A-Za-z] : 開頭必須是一個英文字母（大小寫皆可）
# [1-2]     : 第二碼性別碼必須是 1 或 2
# \d{8}     : 後面必須精準接上 8 個數字
# $         : 剛好結束
pattern = r"^[A-Za-z][1-2]\d{8}$"

if not re.match(pattern, id_number):
    print("❌ 格式錯誤：不符合身份證字號的基本格式規則！")
else:
    # 💡 步驟 4：將輸入一律轉為大寫，避免使用者輸入小寫造成字典查不到
    id_upper = id_number.upper()
    first_letter = id_upper[0]  # 取出首字母，例如 'H'
    
    # 💡 步驟 5：從字典查出對應的兩位數字數字
    # letter_map[first_letter] 會去查表，若 first_letter 是 'H'，則回傳 17
    # str(...) 將其轉回字串，方便與後面的數字做字串拼接
    code_digits = str(letter_map[first_letter])
    
    # 💡 步驟 6：進行字串拼接（首字母數字 + 後面 9 碼數字）
    # id_upper[1:] 代表利用字串切片（Slicing）取出從索引 1 到最後的數字（即 "123456789"）
    converted_id = code_digits + id_upper[1:]
    print(f"首字母 '{first_letter}' 轉換為 '{code_digits}' ➔ 完整數值字串: {converted_id}")

    # 💡 步驟 7：初始化總和變數
    total_sum = 0

    # 💡 步驟 8：核心加權迴圈（共執行 11 次，索引 0 到 10）
    for i in range(len(converted_id)):
        digit = int(converted_id[i])  # 將當前位置的字元轉成整數數字

        if i == 0:
            total_sum += digit * 1  # 轉換後首碼的十位數，權重為 1
        elif i == 10:
            total_sum += digit * 1  # 最後一碼（檢查碼），權重為 1
        else:
            # 索引 1 時：10 - 1 = 權重 9
            # 索引 2 時：10 - 2 = 權重 8 ... 
            # 索引 9 時：10 - 9 = 權重 1
            total_sum += digit * (10 - i)

    # 💡 步驟 9：驗證總和是否能被 10 整除
    if total_sum % 10 == 0:
        print("✅ 驗證結果: Valid ID (這是一個合法的身份證字號)")
    else:
        print("❌ 驗證結果: Invalid ID (這是一個偽造或輸入錯誤的身份證字號)")
