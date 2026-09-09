import json  # 必須先載入 json 模組才能進行轉換

# 定義一個名為 raw_data 的變數
# 外圍使用 ''' (三個單引號) 包裹，代表這是在 Python 中定義的一整段「多行純文字字串」
# 最外圍是方括號 [ ]，這代表它是一個「只有一筆資料的清單」
raw_data = '''
[  # <-- 第 0 層：最外圍是一個 JSON 陣列 (對應 Python 的 List)，索引從 0 開始
   {  # <-- 第 1 層：陣列裡面的第一個元素，是一個 JSON 物件 (對應 Python 的 Dict)
    "status": "success",
    "result": [  # <-- 第 2 層："result" 這個鍵的值，又是一個 JSON 陣列 (List)
      {  # <-- 第 3 層：這個陣列的第一個元素 (索引為 0)，代表台北的資料
        "id": 1,
        "info": {  # <-- 第 4 層：台北的詳細資訊物件 (Dict)
            "name": "台北",
            "weather": "sunny"
        }
      },
      {  # <-- 第 3 層：這個陣列的第二個元素 (索引為 1)，代表台中的資料
        "id": 2,
        "info": {  # <-- 第 4 層：台中的詳細資訊物件 (Dict)
            "name": "台中",
            "weather": "cloudy"  # <-- 目標資料
        }
      }
    ]
  }
]
'''

# 執行動作：json.loads() 會將「JSON 字串」解析並轉換成「Python 的 List 與 Dict 物件」
# 轉換後，原先的雙引號在 Python 內部顯示時會自動變成 Python 習慣的單引號
data = json.loads(raw_data)

# 執行動作：精準提取「台中」的「天氣」並印出
# 🔍 尋找路徑拆解：
# 1. data[0]                  -> 進入最外層清單，取得第一個字典（內含 status 與 result）
# 2. data[0]["result"]        -> 從字典中，取出 "result" 的清單內容（包含台北、台中兩個字典）
# 3. data[0]["result"][1]     -> 在 "result" 清單中，取得索引為 1 的元素（也就是台中的字典）
# 4. data[0]["result"][1]["info"] -> 從台中字典中，進入 "info" 的子字典
# 5. data[0]["result"][1]["info"]["weather"] -> 最終取得 "weather" 的值，即字串 'cloudy'
print("台中天氣：", data[0]["result"][1]["info"]["weather"])
# 大括號 { } = 字典 (Dict) ➔ 必須寫文字欄位號 
# 方括號 [ ] = 清單 (List) ➔ 必須寫數字索引 (從 0 開始算)

# 終端機最終輸出結果：
# 台中天氣： cloudy
