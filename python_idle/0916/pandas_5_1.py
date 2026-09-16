import json
import csv

json_file_path = "0916/3-1-6.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)

# 將 JSON 資料寫入 CSV 檔案
csv_file_path = "0916/3-1-6.csv"
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["title", "clicks"])
    writer.writeheader()
    for item in data:
        writer.writerow({"title": item["title"][0], "clicks": item["clicks"][0]})