# 引入 Python 內建的 GUI（圖形介面）標準模組，並簡寫為 tk
import tkinter as tk

# ====================================================================
# 1. 核心邏輯函式：當使用者手動點擊中間的「圓角按鈕」時會被觸發
# ====================================================================
def on_calculate():
    try:
        # 【讀取資料】手動從 entry_height 輸入框中抓取文字資料，並用 float() 轉為小數
        # 除以 100 是為了手動將公分 (cm) 單位換算為公尺 (m)
        height_m = float(entry_height.get()) / 100
        
        # 【讀取資料】手動從 entry_weight 輸入框中抓取體重文字資料，並轉為小數公斤 (kg)
        weight_kg = float(entry_weight.get())
        
        # 【數據計算】套用標準公式：體重 / (身高公尺的平方)
        # ⚠️ 醫療與健康聲明提示：此處計算僅供一般 BMI 公式示範，若有專業健康管理需求，請諮詢專業醫療人員。
        bmi_value = weight_kg / (height_m ** 2)
        
        # 【更新 BMI 顯示框】使用 .config() 把計算好的實時數據填入第 3 列的方框格式中
        # :.1f 代表手動格式化，只保留顯示到小數點第一位，fg="lightblue" 設為亮藍色字
        label_bmi_val.config(text=f"{bmi_value:.1f}", fg="lightblue")
        
        # 【分析結果評語】根據數據資料，手動判定健康格式（此為標準 BMI 參考區間）
        if bmi_value < 18.5:
            res_text = "體重過輕 (過瘦)"
            res_color = "#ffb74d"  # 亮橘色格式
        elif 18.5 <= bmi_value < 24:
            res_text = "標準體重 (健康)"
            res_color = "#81c784"  # 亮綠色格式
        else:
            res_text = "體重過重 (過肥)"
            res_color = "#e57373"  # 亮紅色格式
            
        # 【更新結果顯示框】將判定好的字串文字與對應顏色，手動填入第 4 列的評語方框格式中
        label_res_val.config(text=res_text, fg=res_color)
        
    except ValueError:
        # 【錯誤處理】如果輸入框是空白，或者使用者手動輸入了英文字母等非數字，拋出紅字格式警告
        label_bmi_val.config(text="錯誤", fg="#e57373")
        label_res_val.config(text="請檢查輸入的內容", fg="#e57373")


# ====================================================================
# 2. 初始化主視窗物件（對應您 Figure 草圖最外圍的大黑底色畫布格式）
# ====================================================================
window = tk.Tk()

# 設定彈出視窗的最上方標題列文字
window.title("BMI 手動繪圖排版計算器")

# 設定視窗的初始尺寸格式：寬度 500 像素，高度 450 像素（剛好能裝下 5 列直排）
window.geometry("500x350")

# 【還原草圖配色】手動改為粉色背景顏色（十六進位碼 #e6a5dd）
window.config(bg="#e6a5dd")


# ====================================================================
# 3. 提取共用樣式風格（避免重複撰寫，讓程式碼更簡潔、好維護）
# ====================================================================
# 定義標籤的字體：微軟正黑體、字體大小 14、加粗 (bold)
font_style = ("Microsoft JhengHei", 14, "bold")

# 定義顯示數值/輸入格子的字體：Arial 英文、字體大小 14、加粗 (bold)
font_val_style = ("Arial", 14, "bold")


# ====================================================================
# 4. 依據您的 Figure 草圖，由上到下一列一列 (Row 0 ~ Row 4) 進行網格排版
# ====================================================================

# --- 【第 0 列 (Row 0)：身高區】 ---
# bg="#1e1e1e" 隱藏背景、fg="white" 設為白字
lbl_height = tk.Label(window, text="身高(CM)", font=font_style, bg="#1e1e1e", fg="white")
# sticky="w" 代表將元件手動「靠左對齊」（West 西方）
lbl_height.grid(row=0, column=0, padx=20, pady=15, sticky="w")

# width=20 控制輸入框長度、bd=2 設定框線寬度、bg="#2d2d2d" 手動將框格內底色改為深灰
# insertbackground="white" 是用來將打字時閃爍的「光標」手動設為白色，才不會在黑底中看不見
entry_height = tk.Entry(window, font=font_val_style, width=20, bd=2, bg="#2d2d2d", fg="white", insertbackground="white")
entry_height.grid(row=0, column=1, padx=20, pady=15)


# --- 【第 1 列 (Row 1)：體重區】 ---
lbl_weight = tk.Label(window, text="體重(KG)", font=font_style, bg="#1e1e1e", fg="white")
lbl_weight.grid(row=1, column=0, padx=20, pady=15, sticky="w")

entry_weight = tk.Entry(window, font=font_val_style, width=20, bd=2, bg="#2d2d2d", fg="white", insertbackground="white")
entry_weight.grid(row=1, column=1, padx=20, pady=15)


# --- 【第 2 列 (Row 2)：中間手動拉出的圓角按鈕格式】 ---
# bd=3 (邊框寬度 3), relief="groove" (邊框浮雕效果)：用來模擬您草圖中手繪白邊圓角按鈕的視覺感
# activebackground 代表滑鼠手動點擊按鈕「壓下去」瞬間的深灰色變化效果
calc_btn = tk.Button(window, text=" 點 擊 計 算 ", font=font_style, width=18, 
                      bg="#3c3c3c", fg="white", activebackground="#505050", activeforeground="white",
                      bd=3, relief="groove", command=on_calculate)
# columnspan=2 橫跨兩行（合併儲存格），讓這顆核心按鈕能完美佔據正中央
calc_btn.grid(row=2, column=0, columnspan=2, pady=20)


# --- 【第 3 列 (Row 3)：BMI 顯示區】 ---
lbl_bmi = tk.Label(window, text="BMI  =", font=font_style, bg="#1e1e1e", fg="white")
lbl_bmi.grid(row=3, column=0, padx=20, pady=15, sticky="w")

# relief="sunken" 代表方框要呈現「向下凹陷」的立體框線感，預設用文字 "--" 預留空資料位置
label_bmi_val = tk.Label(window, text="--", font=font_val_style, width=20, bd=2, relief="sunken", bg="#2d2d2d", fg="gray")
label_bmi_val.grid(row=3, column=1, padx=20, pady=15)


# --- 【第 4 列 (Row 4)：結果評語顯示區】 ---
lbl_res = tk.Label(window, text="結果：", font=font_style, bg="#1e1e1e", fg="white")
lbl_res.grid(row=4, column=0, padx=20, pady=15, sticky="w")

# 這裡是一個用來顯示「健康/過重」評語的空白預留格子格式，預設文字顯示 "等待計算..."
label_res_val = tk.Label(window, text="等待計算...", font=font_style, width=20, bd=2, relief="sunken", bg="#2d2d2d", fg="gray")
label_res_val.grid(row=4, column=1, padx=20, pady=15)


# ====================================================================
# 5. 啟動事件監聽循環（Mainloop）
# ====================================================================
# 這行程式碼會讓視窗維持顯示，並持續在背景手動監聽滑鼠點擊按鈕與鍵盤輸入等事件
window.mainloop()
