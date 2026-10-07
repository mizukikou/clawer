import tkinter as tk

root = tk.Tk()
root.title("Tkinter Canvas 自由繪圖")

# 建立一個 400x300 的畫布，背景為白色
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=20)

# 1. 畫一條直線 (參數：x1, y1, x2, y2, fill=顏色, width=線條寬度)
canvas.create_line(50, 50, 200, 50, fill="blue", width=3)

# 2. 畫一個矩形 (參數：左上角x, 左上角y, 右下角x, 右下角y, fill=填滿顏色)
canvas.create_rectangle(50, 100, 150, 180, fill="yellow", outline="black")

# 3. 畫一個圓形或橢圓 (參數為該圓形的外切矩形座標)
canvas.create_oval(220, 100, 320, 200, fill="lightgreen")

# 4. 在畫布上寫字
canvas.create_text(200, 250, text="這是手動繪製的圖形", font=("Arial", 14), fill="purple")

root.mainloop()
