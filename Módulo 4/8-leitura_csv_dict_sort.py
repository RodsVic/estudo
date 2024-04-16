courses = []

with open("dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)

for course in sorted(courses, key=lambda course: course["language"]):
    print(f"{course["language"]}: {course["category"]}")
    
print()

for course in sorted(courses, key=lambda course: course["category"], reverse=True):
    print(f"{course["language"]}: {course["category"]}")
