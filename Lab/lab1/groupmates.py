#coding:utf-8
groupmates = [
    {
        "Name": u"Никита",
        "Group": "2254",
        "Age": 23,
        "Marks": [5,5,4,4,4]
    },
    {
        "Name": u"Максим",
        "Group": "2254",
        "Age": 24,
        "Marks": [4,4,4,5,5]
    },
    {
        "Name": "Danya",
        "Group": "2254",
        "Age": 23,
        "Marks": [4,5,5,4,4]
    },
    {
        "Name": "Ctepa",
        "Group": "2254",
        "Age": 26,
        "Marks": [4,4,5,5,4]
    }
]
def print_students (students):
    print u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20)
    for student in students:
        print \
              student["Name"].ljust(15), \
              student["Group"].ljust(8), \
              str(student["Age"]).ljust(8), \
              str(student["Marks"]).ljust(20)
    print "\n"

print_students(groupmates)

def srednee(students, min_avg):
    result = []
    for a in students:
        avg = sum(a["Marks"]) / len(a["Marks"])
        if avg >= min_avg:
            result.append(a)
    return result

if __name__ == "__main__":
    print("Vse studenti")
    print_students(groupmates)

    print("Studenti so srednim balom >= 4.0")
    print_students(srednee(groupmates, 4.0))
