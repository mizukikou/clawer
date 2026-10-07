import tkinter as tk
# 引入 Matplotlib 的 Figure 物件（用來建立圖表畫布）
from matplotlib.figure import Figure
# 引入將 Matplotlib 圖表嵌入 Tkinter 的關鍵連接器
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 定義按鈕點擊函式：點擊後更換圖表數據
def update_chart():
    ax.clear()  # 清除原本的圖表內容
    # 畫一條新的折線（X軸: 1,2,3,4，Y軸: 10,25,15,30）
    ax.plot([1, 2, 3, 4], [10, 25, 15, 30], color="red", marker="o", label="新數據")
    ax.set_title("動態更新後的圖表")
    ax.legend()  # 顯示圖例
    canvas.draw()  # 重新繪製畫布以更新畫面

# 1. 初始化 Tkinter 主視窗
root = tk.Tk()
root.title("Tkinter 嵌入 Figure 圖表範例")
root.geometry("600x500")

# 2. 建立 Matplotlib 的 Figure 物件（畫布）
# figsize=(寬, 高) 單位是英吋，dpi 為每英吋像素點（會影響清晰度與大小）
fig = Figure(figsize=(5, 4), dpi=100)

# 3. 在 Figure 上建立一個子圖（Axes）
# 111 代表 1x1 網格中的第 1 個圖
ax = fig.add_subplot(111)
# 在子圖上畫初始數據（折線圖）
ax.plot([1, 2, 3, 4], [1, 4, 9, 16], color="blue", marker="s", label="初始數據")
ax.set_title("Matplotlib Figure 範例")
ax.set_xlabel("X 軸名稱")
ax.set_ylabel("Y 軸名稱")
ax.legend()

# 4. 使用 FigureCanvasTkAgg 將 Figure 轉換為 Tkinter 的元件
# master=root 代表這個畫布要放在 root 視窗中
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()  # 取得 Tkinter 實體元件

# 5. 使用 grid 進行版面配置
# 將圖表元件放在第 0 列，並允許它橫跨 2 行
canvas_widget.grid(row=0, column=0, columnspan=2, pady=10)

# 6. 建立一個 Tkinter 按鈕，點擊後觸發更新函式
button = tk.Button(root, text="更新圖表數據", command=update_chart)
button.grid(row=1, column=0, columnspan=2, pady=10)

# 7. 啟動 Tkinter 事件循環
root.mainloop()
