# import sys
# print(sys.executable)

students = [
    {"id": "A01", "name": "Alice", "score": 85},
    {"id": "A02", "name": "Bob", "score": 92},
    {"id": "A03", "name": "Charlie", "score": 78}
]

average = sum = 0
for x in students:
    sum += x["score"]
print(f"平均分數：{sum/(len(students))}")


name = input("請輸入學生姓名:")
found = False 
for x in students:
    if name in x["name"]: 
        print(f"學生姓名:{x['name']}，ID：{x['id']}，分數：{x['score']}")
        found = True       
if not found:
    print("查無此人")
