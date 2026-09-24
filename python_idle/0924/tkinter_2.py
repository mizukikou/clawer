import tkinter as tk

root = tk.Tk() # 建立主視窗的實例

root.geometry("400x300") # 設定視窗的初始大小為 400x300

label1 = tk.Label(root, text="First Name!") # 建立第一個標籤，顯示文字 "First Name!" 並加入視窗顯示
label2 = tk.Label(root, text="Last Name!") # 建立第二個標籤，顯示文字 "Last Name!" 並加入視窗顯示

label1.grid(row=0, column=0) # 將第一個標籤放置在網格的第 0 行第 0 列
label2.grid(row=1, column=0) # 將第二個標籤放置在網格的第 1 行第 0 列

entry1 = tk.Entry(root) # 建立一個輸入框
entry2 = tk.Entry(root) # 建立第二個輸入框
entry1.grid(row=0, column=1) # 將第一個輸入框放置在網格的第 0 行第 1 列
entry2.grid(row=1, column=1) # 將第二個輸入框放置在網格的第 1 行第 1 列

def display():    # 顯示輸入的姓名在第三個標籤上
    label3['text'] = entry1.get() + " " + entry2.get() # 將第一個和第二個輸入框的內容組合成姓名並顯示在第三個標籤上

label3 = tk.Label(root, text="") # 建立第三個標籤，用來顯示輸入的姓名
#label3.grid(row=3, column=0, columnspan=2) # 將第三個標籤放置在網格的第 2 行，跨越兩列(columnspan：合併儲存格)
label3.grid(row=2, column=1) # 將第三個標籤放置在網格的第 2 行，跨越兩列(columnspan：合併儲存格)

button = tk.Button(root, text="顯示合併欄位", command=display) # 建立一個按鈕，點擊後執行 display 函數
button.grid(row=2, column=0) # 將按鈕放置在網格的第 3 行，跨越兩列

root.mainloop() # 啟動主事件迴圈，使視窗保持顯示並等待使用者操作
