import tkinter as tk

root = tk.Tk() # 建立主視窗的實例
root.title("My First Tkinter Window")
label = tk.Label(root, text="Hello, Tkinter!") # 建立一個標籤，顯示文字 "Hello, Tkinter!"
label.pack() # 將標籤加入視窗並顯示

root.geometry("400x300") # 設定視窗的初始大小為 400x300

button = tk.Button(root, text="Click Me") # 建立一個按鈕，顯示文字 "Click Me"
button.pack() # 將按鈕加入視窗並顯示

root.mainloop()
