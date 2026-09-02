# 匯入 Python 內建的作業系統操作模組，用於處理檔案路徑、讀取資料夾與重新命名
import os

# 定義目標資料夾的名稱（或路徑），此處為當前目錄下的 "scraped_images" 資料夾
folder = "scraped_images"  # 假設資料夾裡有 img1.jpg, img2.jpg...

# 使用 os.listdir() 讀取該資料夾，並將裡面「所有檔案的檔名」存成一個列表（List）
# 例如 files = ["img1.jpg", "img2.jpg", "photo.png"]
files = os.listdir(folder)  # 列出資料夾內所有檔案

# 使用 for 迴圈搭配 enumerate() 逐一讀取檔案列表
# enumerate() 會同時抓出「目前的索引數字（從 0 開始）」與「原本的檔案名稱」
# index 變數接收：0, 1, 2... ； filename 變數接收："img1.jpg", "img2.jpg"...
for index, filename in enumerate(files):
    
    # 1. 建立新名字 : pet_0.jpg, pet_1.jpg...
    # 使用 f-string 格式化字串，將 index 數字塞入檔名中，建立全新的檔名
    new_name = f"pet_{index}.jpg"
    
    # 2. 使用 os.path.join 結合「資料夾名稱」與「舊檔名」，得到舊檔案的完整路徑
    # 例如："scraped_images/img1.jpg"
    old_path = os.path.join(folder, filename)
    
    # 3. 結合「資料夾名稱」與「新檔名」，得到新檔案的完整目標路徑
    # 例如："scraped_images/pet_0.jpg"
    new_path = os.path.join(folder, new_name)
    
    # 4. 呼叫 os.rename(舊路徑, 新路徑) 執行實際的檔案重新命名（改名）動作
    os.rename(old_path, new_path)
    
    # 5. 在控制台印出改名成功的提示訊息，方便追蹤進度
    print(f"更名成功: {filename} -> {new_name}")

# https://picsum.photos/200/300.jpg
