import tkinter as tk
from tkinter import ttk  # Treeview 元件儲存在 ttk 子模組中
import pandas as pd
import webview  # 引入網頁視窗套件

# ====================================================================
# 核心資料準備：建立一筆跟您之前一模一樣的 Pandas 表格資料
# ====================================================================
df = pd.DataFrame({
    "姓名": ["小明", "小華", "小美"],
    "年齡": [20, 25, 22],
    "城市": ["台北", "桃園", "台中"]
})

# ====================================================================
# 【實戰範例一】手動建立：原生 Tkinter Treeview 視窗
# ====================================================================
def launch_treeview():
    # 建立一個傳統的 Tkinter 主視窗格式
    root = tk.Tk()
    root.title("🌲 傳統原生 Treeview 視窗")
    root.geometry("400x200")
    
    # 1. 宣告 Treeview 元件
    # columns: 指定欄位名稱的清單（直接抓取 Pandas 的欄位名稱）
    # show="headings": 隱藏最左邊預設的空白樹狀折疊欄，純粹當表格用
    tree = ttk.Treeview(root, columns=list(df.columns), show="headings")
    
    # 2. 手動設定每一縱行的標頭文字與對齊格式
    for col in df.columns:
        tree.heading(col, text=col)       # 設定表格標題（姓名、年齡、城市）
        tree.column(col, anchor="center", width=100) # 設定文字置中、欄寬 100 像素
        
    # 3. 核心資料填入：使用 Python 迴圈，手動將 Pandas 的每一列資料塞進格子裡
    # df.values.tolist() 會把表格變成如 [["小明", 20, "台北"], ...] 的格式
    for row in df.values.tolist():
        tree.insert("", tk.END, values=row) # tk.END 代表每次都依序加在最尾巴
        
    # 4. 版面配置：將 Treeview 表格填滿整個視窗空間
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    # 啟動事件監聽（注意：這會讓視窗維持開啟）
    root.mainloop()


# ====================================================================
# 【實戰範例二】手動建立：現代化 pywebview 網頁視窗
# ====================================================================
def launch_webview():
    # 1. 資料格式轉換：直接一鍵將 Pandas 表格手動翻譯成 HTML 網頁標籤格式
    # index=False 代表不顯示 0, 1, 2 的索引列
    # classes="my-table" 代表幫這個表格加上一個 CSS 班級標籤，方便等等化妝
    table_html = df.to_html(index=False, classes="my-table")
    
    # 2. 設計前端網頁程式碼：結合 HTML 與進階 CSS 語法（手動還原您最愛的深色主題格式）
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            /* 設定整個網頁的背景與字體風格 */
            body {{
                background-color: #1e1e1e;   /* 跟您 Figure 草圖一樣的深黑色 */
                color: #ffffff;              /* 白色文字 */
                font-family: 'Microsoft JhengHei', sans-serif;
                padding: 20px;
            }}
            /* 設計華麗的網頁表格外觀格式 */
            .my-table {{
                width: 100%;
                border-collapse: collapse; /* 讓格子框線合併，不產生雙重線 */
                margin-top: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.3); /* 手動加上網頁特有的陰影特效 */
            }}
            /* 設計表頭(th)與單元格(td)的框線與留白間距 */
            .my-table th, .my-table td {{
                border: 1px solid #3c3c3c;
                padding: 12px;
                text-align: center;
            }}
            /* 網頁進階特效：滑鼠滑過去時，整列會自動手動高亮變色！ */
            .my-table tr:hover {{
                background-color: #2d2d2d;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <h3 style="color: #81c784;">🌐 現代嵌入式 Webview 表格</h3>
        {table_html} <!-- 在這裡把 Pandas 生成的表格代碼手動注入進來 -->
    </body>
    </html>
    """
    
    # 3. 建立並呼叫內建微型瀏覽器，直接在桌面渲染出剛剛寫好的 HTML 網頁
    webview.create_window("WebView 渲染中心", html=html_content, width=450, height=350)
    webview.start()


# ====================================================================
# 3. 核心主執行程序：先開啟 Treeview，再開啟 Webview
# ====================================================================
# ====================================================================
# 修正前（會卡住）：
# if __name__ == "__main__":
#     launch_treeview()
#     launch_webview()
# ====================================================================

# ====================================================================
# 修正後（100% 同時彈出大並排）：
# ====================================================================
if __name__ == "__main__":
    print("🚀 正在為您同時啟動技術對比視窗...")
    
    # 1. 建立一個最頂層的 Tkinter 主視窗（用來裝 Treeview）
    root = tk.Tk()
    root.title("🌲 傳統原生 Treeview 視窗")
    root.geometry("400x200")
    
    # 2. 宣告並塞入 Treeview 表格元件（將原本 launch_treeview 內部的內容搬到這裡）
    tree = ttk.Treeview(root, columns=list(df.columns), show="headings")
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)
    for row in df.values.tolist():
        tree.insert("", tk.END, values=row)
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    # 🔥 【核心黑科技】：利用 root.after() 計時器功能！
    # 告訴 Tkinter：在主視窗啟動後的 100 毫秒（0.1秒），手動在背景悄悄呼叫 launch_webview 函式
    # 這樣兩個套件的視窗事件循環就不會打架，可以完美同時呈現在桌面上！
    root.after(100, launch_webview)
    
    # 3. 啟動總事件循環
    root.mainloop()
