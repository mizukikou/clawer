import csv

list_of_dicts = [
    {"id":1,"name":"紅毛丹","price":2000},
    {"id":2,"name":"黃金果","price":1500},
    {"id":3,"name":"斐濟龍眼","price":1000}
    ]

with open('fruits.csv', mode='w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "price"])
    writer.writeheader()
    for item in list_of_dicts:
        writer.writerow(item)
        
with open('fruits.csv', mode='r', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    sum = 0
    for row in reader:
        sum += int(row["price"])
    print("總價：", sum)