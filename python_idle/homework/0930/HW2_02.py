import csv
import json
json_data = '[{"name": "小明", "score": 85}, {"name": "小華", "score": 92}, {"name": "小美", "score": 78}]'
students_list = json.loads(json_data)
with open("students.csv", mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    # 寫入標題列
    writer.writerow(["姓名", "成績"])
    # 依序寫入每位學生的資料
    for student in students_list:
        writer.writerow([student["name"], student["score"]])
print("students.csv 檔案已成功匯出！")