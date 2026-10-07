import pandas as pd
import webview

# --- 1. 準備 15 筆原始資料（包含大量重複、缺失值） ---
raw_data = [
    ("1", "王小明", 25.0, "台北"),
    ("2", "李四", None, "台中"),       # 缺年紀
    ("3", "王五", 30.0, None),         # 缺城市
    ("1", "王小明", 25.0, "台北"),   # 重複 1
    ("4", "張三", 22.0, "高雄"),
    ("4", "張三", 22.0, "高雄"),     # 重複 2
    ("5", "趙六", None, None),          # 缺年紀、缺城市
    ("6", "孫七", 28.0, "新竹"),
    ("2", "李四", None, "台中"),       # 重複 3
    ("7", "周八", 35.0, "台南"),
    ("8", "吳九", None, "基隆"),       # 缺年紀
    ("9", "鄭十", 40.0, "桃園"),
    ("7", "周八", 35.0, "台南"),     # 重複 4
    (None, None, 19.0, "花蓮"),       # 缺編號、姓名
    ("11", "錢十一", 27.0, "彰化")
]

# 轉成 Pandas DataFrame 方便進行資料清洗
df_original = pd.DataFrame(raw_data, columns=['編號', '姓名', '年紀', '城市'])

# --- 2. 各種資料清洗邏輯（完全對應你的按鈕功能） ---

def get_html_table(df_target):
    """將 DataFrame 轉換為帶有樣式的 HTML 表格字串"""
    # 對應你截圖中的 df.to_html(index=False, classes="paleBlueRows")
    return df_target.to_html(index=False, classes="paleBlueRows", na_rep="【空值】")

def process_data(mode):
    """根據模式，使用 Pandas 處理資料並回傳 HTML"""
    df_clean = df_original.copy()
    
    if mode == "delete_duplicates":
        # ⬅️ 刪除重複
        df_clean = df_clean.drop_duplicates()
        title = "▼ 刪除重複值結果 (已移除重複列)"
        
    elif mode == "fill_missing":
        # 🔼 補上缺失值 (參考你截圖中用中位數、平均數或特定文字補值的方式)
        # 數字型態欄位（年紀）：用中位數補值
        median_age = df_clean['年紀'].median()
        df_clean['年紀'] = df_clean['年紀'].fillna(median_age)
        
        # 文字型態欄位：用特定字串補值
        df_clean['編號'] = df_clean['編號'].fillna("未填")
        df_clean['姓名'] = df_clean['姓名'].fillna("無名氏")
        df_clean['城市'] = df_clean['城市'].fillna("未知城市")
        title = "▼ 補上缺失值結果 (已自動計算並補值)"
        
    elif mode == "both":
        # ➡️ 補上缺失 + 刪除重複
        # 先補值
        median_age = df_clean['年紀'].median()
        df_clean['年紀'] = df_clean['年紀'].fillna(median_age)
        df_clean['編號'] = df_clean['編號'].fillna("未填")
        df_clean['姓名'] = df_clean['姓名'].fillna("無名氏")
        df_clean['城市'] = df_clean['城市'].fillna("未知城市")
        # 再去重
        df_clean = df_clean.drop_duplicates()
        title = "▼ 補上缺失 + 刪除重複值結果 (乾淨資料)"
        
    else:
        title = "■ 原始資料視窗 (包含缺失值與重複列)"

    # 將 Pandas 表格轉換為網頁 HTML 碼
    table_html = get_html_table(df_clean)
    
    # 計算目前的資料筆數
    rows_count = len(df_clean)
    
    return title, table_html, rows_count

# --- 3. 提供給前端網頁呼叫的 Python 介面 (API) ---
class Api:
    def load_data(self, mode):
        """當網頁上的按鈕被點擊時，會觸發這個 Python 函式"""
        title, table_html, count = process_data(mode)
        # 回傳處理好的資料給前端 JavaScript 更新畫面
        return {"title": title, "table": table_html, "count": count}

# --- 4. 撰寫包含 CSS 樣式與按鈕主體的完整 HTML 字串 ---
# 對應你截圖中的 html = f"""..."""
html_content = f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background-color: #f4f6f9; color: #333; }}
        h1 {{ text-align: center; color: #2c3e50; font-size: 22px; }}
        .btn-group {{ display: flex; justify-content: space-between; margin: 20px 0; gap: 10px; }}
        button {{ flex: 1; padding: 12px; font-size: 14px; background-color: #34495e; color: white; border: none; border-radius: 4px; cursor: pointer; transition: 0.2s; }}
        button:hover {{ background-color: #415b76; }}
        .view-box {{ background: white; padding: 15px; border-radius: 6px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }}
        .box-title {{ font-weight: bold; font-size: 16px; margin-bottom: 10px; border-left: 5px solid #3498db; padding-left: 8px; color: #2c3e50; }}
        
        /* 🔵 專屬 paleBlueRows 表格樣式 (對應你截圖中的 classes) */
        table.paleBlueRows {{ border: 1px solid #FFFFFF; width: 100%; text-align: center; border-collapse: collapse; }}
        table.paleBlueRows td, table.paleBlueRows th {{ padding: 8px 10px; }}
        table.paleBlueRows tbody td {{ font-size: 14px; border: 1px solid #E6E6E6; }}
        table.paleBlueRows tr:nth-child(even) {{ background: #F2F5F8; }}
        table.paleBlueRows th {{ background: #3498db; color: white; font-size: 15px; font-weight: bold; border: 1px solid #3498db; }}
    </style>
</head>
<body>

    <h1>📊 VS Code 風格資料處理工具 (Pandas + PyWebview)</h1>

    <!-- 1. 上方原始資料視窗 -->
    <div class="view-box">
        <div class="box-title">■ 原始資料視窗 (原始資料共 {len(df_original)} 筆)</div>
        {get_html_table(df_original)}
    </div>

    <!-- 2. 中間 3 個功能按鈕 -->
    <div class="btn-group">
        <button onclick="updateView('delete_duplicates')">⬅️ 刪除重複</button>
        <button onclick="updateView('fill_missing')">🔼 補上缺失值</button>
        <button onclick="updateView('both')">➡️ 補上缺失+刪除重複值</button>
    </div>

    <!-- 3. 下方動態生成的結果視窗 -->
    <div class="view-box" id="result-box" style="display: none;">
        <div class="box-title" id="result-title">▼ 處理結果視窗</div>
        <div id="result-table-container"></div>
    </div>

    <!-- 4. 用 JavaScript 來跟後台 Python (pywebview) 溝通 -->
    <script>
        function updateView(mode) {{
            // 💡 呼叫 Python 後台的 Api.load_data 函式
            pywebview.api.load_data(mode).then(function(response) {{
                // 收到 Python 處理完的資料後，動態更新 HTML 畫面
                document.getElementById('result-title').innerText = response.title + " (共 " + response.count + " 筆)";
                document.getElementById('result-table-container').innerHTML = response.table;
                document.getElementById('result-box').style.display = 'block'; // 顯示下方視窗
            }});
        }}
    </script>

</body>
</html>
"""

# --- 5. 啟動 pywebview 視窗 ---
if __name__ == '__main__':
    api = Api()
    # 建立視窗並載入剛剛寫好的 HTML 字串，同時綁定 Python API 類別
    window = webview.create_window(
        title='Pandas 資料清洗工具', 
        html=html_content, 
        js_api=api,
        width=800,
        height=750
    )
    # 啟動網頁視窗
    webview.start()
