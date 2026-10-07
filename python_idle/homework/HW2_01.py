import json
import csv

json_data = '[{"name":"小明","score":85}, {"name":"小華","score":92}, {"name":"小美","score":78}]'
students = json.loads(json_data)
with open('students.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = ['姓名', '成績']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow({
            '姓名': student['name'],
            '成績': student['score']
        })
print('students.csv 建立完成！')