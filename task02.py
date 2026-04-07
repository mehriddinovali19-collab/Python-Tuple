students = [("Ali", ["Fizika", "Matematika"]),
             ("Laylo", ["Ingliz tili"]), ("Jasur",
             ["Matematika", "Informatika"])
]
subject = input("Fan nomini kiriting: ")
count = 0
for student in students:
     name, subjects = student
     if subject in subjects:
        count += 1
print(count)
