students = {
    101: {
        "info":('Ravi', "ECE"),
        "Courses": ["python","MySQL","CSS","CSS"]
    },
    102: {
        "info":("Uday","CSC"),
        "Courses": ["python","python","data analyst","html"]
    }
}

for student_id, data in students.items():

    print("\nStudnets ID: ",student_id)

    name,branch = data["info"]
    print('name:' , name)
    print("branch: ",branch)

    print("all Courses:",data["Courses"])

    unique_courses = set(data["Courses"])
    print("unique courses:",unique_courses)