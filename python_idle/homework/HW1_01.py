students = [
    {"id": "A01", "name": "Alice", "score": 85},
    {"id": "A02", "name": "Bob", "score": 92},
    {"id": "A03", "name": "Charlie", "score": 78},
]

total = 0
for student in students:
    total += student["score"]

average = total / len(students)
print(f"平均分數：{average:.2f}")

target = input("請輸入學生姓名：").strip()

found = None
for student in students:
    if student["name"].lower() == target.lower():
        found = student
        break

if found:
    print(f"ID：{found['id']}，分數：{found['score']}")
else:
    print("查無此人")
