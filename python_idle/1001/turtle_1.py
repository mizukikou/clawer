import turtle

# 設定海龜畫筆
t = turtle.Turtle()
t.speed(0) # 設定到最快速度
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# 讓海龜循環畫出 360 條線，每次轉彎並換顏色
for x in range(360):
    t.pencolor(colors[x % 6]) # 循環切換 6 種顏色
    t.width(x // 100 + 1)     # 隨著畫越多，線條越粗
    t.forward(x)              # 前進 x 像素
    t.left(59)                # 向左旋轉 59 度（造成交錯效果）

turtle.done() # 繪圖結束，保持視窗開啟
