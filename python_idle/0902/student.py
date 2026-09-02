import sys
from student import Student

s1 = Student("羅同學",35,"0912345678")

print(s1.name)
print(s1.age)
print(s1.phone)

s1.take_exam()
s1.do_homework()

print(sys.path)

##student.test()
