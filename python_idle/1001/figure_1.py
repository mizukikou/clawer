import matplotlib.pyplot as plt

# 1. 建立一張乾淨的空白畫布 (Figure)
fig = plt.figure(figsize=(6, 5), dpi=100)

# 2. 建立一個作畫區域 (Axes)，並將座標軸隱藏，讓它看起來像一張純白畫布
ax = fig.add_subplot(111)
ax.set_xlim(0, 10)  # 設定畫布 X 軸範圍 0~10
ax.set_ylim(0, 10)  # 設定畫布 Y 軸範圍 0~10
ax.axis('off')     # 隱藏外框與數字刻度
ax.set_title("手動繪圖：請按住滑鼠左鍵在白色區域塗鴉", fontproperties="Microsoft JhengHei")

# 3. 設計手動繪圖的邏輯變數
is_drawing = False  # 紀錄滑鼠目前是否處於「按住」狀態
x_data, y_data = [], [] # 儲存滑鼠滑過的座標點

# 4. 定義滑鼠事件函式
def on_press(event):
    """當滑鼠左鍵按下時觸發"""
    global is_drawing, x_data, y_data
    if event.button == 1: # 1 代表滑鼠左鍵
        is_drawing = True
        x_data, y_data = [event.xdata], [event.ydata]

def on_move(event):
    """當滑鼠在畫布上移動時觸發"""
    global is_drawing, x_data, y_data
    # 確保滑鼠在畫布內，且左鍵有被按住
    if is_drawing and event.xdata is not None and event.ydata is not None:
        x_data.append(event.xdata)
        y_data.append(event.ydata)
        
        # 在畫布上即時畫出線條 (黑色，線條粗細為 2)
        ax.plot(x_data[-2:], y_data[-2:], color="black", linewidth=2)
        
        # 手動強制 Figure 畫布即時重繪更新，這樣滑鼠劃過才能立刻看到線條
        fig.canvas.draw()

def on_release(event):
    """當滑鼠左鍵放開時觸發"""
    global is_drawing
    if event.button == 1:
        is_drawing = False

# 5. 【核心】將手動滑鼠事件與 Figure 畫布連結起來
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('motion_notify_event', on_move)
fig.canvas.mpl_connect('button_release_event', on_release)

# 6. 顯示手動繪圖視窗
plt.show()
