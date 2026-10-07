import tkinter as tk

# 定義按鈕被點擊時要執行的函式
# 注意：這個函式必須寫在建立 Button 物件的「前面」，否則 Python 會找不到該名稱
def click_me():
    # 當使用者點擊按鈕時，在終端機（Console）印出提示訊息
    print("按鈕被點擊了！")
    
    # 透過 .config() 動態修改第一個標籤（label）的顯示文字
    label.config(text="你點了按鈕！")

# 建立 Tkinter 的主視窗物件（習慣命名為 root）
root = tk.Tk()  # tk是模組名稱，TK是的一個類別（Class）件；當後面加上括號 ()，在物件導向程式設計（OOP）中就代表執行「建構子」，也就是實例化（Instantiate）出一個全新的主視窗物件。

# 設定主視窗的標題文字
root.title("Tkinter 詳細註解範例")

# 設定主視窗的初始尺寸：寬 400 像素、高 300 像素
root.geometry("400x300")

# 建立第一個標籤（Label）元件，文字設為 "Hello, World!"，父視窗為 root
label = tk.Label(root, text="Hello, World!")

# 建立第二個標籤（Label）元件，文字設為 "Goodbye, World!"，父視窗為 root
label2 = tk.Label(root, text="Goodbye, World!")

# 建立第一個單行輸入框（Entry）元件，供使用者輸入文字
entry1 = tk.Entry(root)

# 建立第二個單行輸入框（Entry）元件
entry2 = tk.Entry(root)

# 建立按鈕（Button）元件
# text: 按鈕上顯示的文字
# width: 按鈕寬度
# command: 綁定點擊事件要觸發的函式（注意後面不能加括號 ()，否則程式啟動時會直接執行）
button = tk.Button(root, text="Click Me", width=10, command=click_me)

# 使用 grid 版面配置管理器將元件依序放入網格中（row 代表列、column 代表行）
# pady 代表上下邊距（padding y），避免元件彼此黏得太緊
label.grid(row=0, column=0, pady=5)
label2.grid(row=1, column=0, pady=5)
entry1.grid(row=2, column=0, pady=5)
entry2.grid(row=3, column=0, pady=5)
button.grid(row=4, column=0, pady=10)

# 進入主事件循環（Mainloop）
# 這行程式碼會讓視窗保持顯示狀態，並持續監聽使用者的滑鼠、鍵盤等操作事件
root.mainloop()
