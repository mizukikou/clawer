import tkinter as tk

def click():
    print("發生按下事件")
    label4['text'] = "發生按下事件"

root = tk.Tk()

root.geometry("600x500")

label = tk.Label(root, text="這是我的第一個視窗")
label2 = tk.Label(root, text="這是第二個Label")
label3 = tk.Label(root, text="這是第三個Label")
label4 = tk.Label(root, text="顯示結果")

button = tk.Button(root, text="按下", width= 20, command=click)

label.pack(pady = (20, 0)) # 上距, 下距
label2.pack(pady = (20, 0))
label3.pack(pady = (20, 0))
button.pack(pady = (20, 0))
label4.pack(pady = (20, 0))

# padx = (a, b) # 左距=a， 右距=b

root.mainloop()



# root = tk.Tk()

# root.geometry("600x500")