import os
import shutil

target_dir = "history_logs"
def move_files(source):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"建立資料夾:{target_dir}")

    if os.path.exists(source):
        shutil.move(source,os.path.join(target_dir,"old.log"))
        print("日誌已經歸檔")

print(os.listdir("."))
for f in os.listdir("."):
    if os.path.isfile(f):
       if "py" in f:
          move_files(f)
          print(f)
