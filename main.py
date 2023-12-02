bakueuropeanlyceum = {
    "8a3": {
        "child1": {
            "name": "Tuqay",
            "surname": "Mehdiyev",
            "age": 14,
            "points": 91
        },
        "child2": {
            "name": "Farid",
            "surname": "Rasulzada",
            "age": 13,
            "points": 86
        },
        "child3": {
            "name": "Cavid",
            "surname": "Abbasli",
            "age": 13,
            "points": 90
        },
        "child4": {
            "name": "Turqay",
            "surname": "Azimli",
            "age": 13,
            "points": 96
        },
        "child5": {
            "name": "Kamal",
            "surname": "Alizada",
            "age": 13,
            "points": 82
        },
        "child6": {
            "name": "Banu",
            "surname": "Quliyeva",
            "age": 13,
            "points": 85
        },
        "child7": {
            "name": "Nesrin",
            "surname": "Isayeva",
            "age": 13,
            "points": 83
        }
    },
    "7a2": {
        "child1": {
            "name": "Fidan",
            "surname": "Mikayilzada",
            "age": 12,
            "points": 95
        },
        "child2": {
            "name": "Selcan",
            "surname": "Aghayeva",
            "age": 12,
            "points": 75
        },
        "child3": {
            "name": "Tuncay",
            "surname": "Mehdiyev",
            "age": 12,
            "points": 70
        },
        "child4": {
            "name": "Banu",
            "surname": "Tahirzada",
            "age": 12,
            "points": 78
        },
        "child5": {
            "name": "Ughur",
            "surname": "Allahverdi",
            "age": 12,
            "points": 80
        },
        "child6": {
            "name": "Sama",
            "surname": "Isali",
            "age": 12,
            "points": 78
        },
        "child7": {
            "name": "Elxan",
            "surname": "Nasibli",
            "age": 12,
            "points": 50
        }
    },
    "8a1": {
        "child1": {
            "name": "Zehra",
            "surname": "Heydarli",
            "age": 13,
            "points": 90
        },
        "child2": {
            "name": "Aybaniz",
            "surname": "Gulverdi",
            "age": 14,
            "points": 83
        },
        "child3": {
            "name": "Orxan",
            "surname": "Nasibli",
            "age": 14,
            "points": 89
        },
        "child4": {
            "name": "Rasul",
            "surname": "Dirdali",
            "age": 13,
            "points": 73
        },
        "child5": {
            "name": "Fatima",
            "surname": "Palverdi",
            "age": 13,
            "points": 72
        },
        "child6": {
            "name": "Ali",
            "surname": "Tuloydena",
            "age": 14,
            "points": 90
        },
        "child7": {
            "name": "Isa",
            "surname": "Isayev",
            "age": 13,
            "points": 83
        }
    },
    "2a3": {
        "child1":{
            "name":"Charles",
            "surname":"Leclerc",
            "age":14,
            "points":88
        },
        "child2":{
            "name":"Max",
            "surname":"Verstappen",
            "age":13,
            "points":56
        },
        "child3":{
            "name":"Carlos",
            "surname":"Sainz",
            "age":14,
            "points":76
        },
        "child4":{
            "name":"George",
            "surname":"Russell",
            "age":13,
            "points":70
        },
        "child5":{
            "name":"Lando",
            "surname":"Norris",
            "age":13,
            "points":80
        },
        "child6":{
            "name":"Sergio",
            "surname":"Perez",
            "age":14,
            "points":90
        },
        "child7":{
            "name":"Pierre",
            "surname":"Gasly",
            "age":14,
            "points":67
        }
    }
}
def handle_create():
    print("You selected 'create'.")
    option = input("Do you want to create a 'class' or 'student'?:")
    if option.lower() == "class":
        clname = input("Enter class name: ")
        bakueuropeanlyceum[clname] = {}
        print(f"Class '{clname}' created successfully!")
    elif option.lower() == "student":
        class_name = input("Enter the class name for the new student: ")
        if class_name in bakueuropeanlyceum:
            student_name = input("Enter the student name: ")
            surname = input("Enter the student surname: ")
            age = int(input("Enter the student age: "))
            points = int(input("Enter the student points: "))
            student_id = f"child{len(bakueuropeanlyceum[class_name]) + 1}"
            bakueuropeanlyceum[class_name][student_id] = {
                "name": student_name,
                "surname": surname,
                "age": age,
                "points": points,
            }
            print(f"Student '{student_name}' added to class '{class_name}' successfully!")
        else:
            print(f"Error: Class '{class_name}' does not exist.")
    else:
        print("Invalid option.")

def handle_read():
    print("You selected 'read'.")
    option = input("Do you want to read 'class' or 'student'? ")
    if option.lower() == "class":
        print("Available classes:", list(bakueuropeanlyceum.keys()))
        class_name = input("Enter the class name to view: ")
        if class_name in bakueuropeanlyceum:
            print(f"Class '{class_name}': {bakueuropeanlyceum[class_name]}")
        else:
            print(f"Error: Class '{class_name}' does not exist.")
    elif option.lower() == "student":
        class_name = input("Enter the class name: ")
        student_id = input("Enter the student ID: ")
        if class_name in bakueuropeanlyceum and student_id in bakueuropeanlyceum[class_name]:
            print(f"Student '{student_id}' details: {bakueuropeanlyceum[class_name][student_id]}")
        else:
            print(f"Error: Student '{student_id}' not found in class '{class_name}'.")
    else:
        print("Invalid option.")

def handle_change():
    print("You selected 'change'.")
    option = input("Do you want to change 'class' or 'student'? ")
    if option.lower() == "class":
        print("Available classes:", list(bakueuropeanlyceum.keys()))
        class_name = input("Enter the class name to change: ")
        new_class_name = input("Enter the new class name: ")
        if class_name in bakueuropeanlyceum:
            bakueuropeanlyceum[new_class_name] = bakueuropeanlyceum.pop(class_name)
            print(f"Class '{class_name}' changed to '{new_class_name}' successfully!")
        else:
            print(f"Error: Class '{class_name}' does not exist.")
    elif option.lower() == "student":
        class_name = input("Enter the class name: ")
        student_id = input("Enter the student ID to change: ")
        if class_name in bakueuropeanlyceum and student_id in bakueuropeanlyceum[class_name]:
            new_points = int(input("Enter the new points for the student: "))
            bakueuropeanlyceum[class_name][student_id]["points"] = new_points
            print(f"Points for student '{student_id}' in class '{class_name}' changed to '{new_points}' successfully!")
        else:
            print(f"Error: Student '{student_id}' not found in class '{class_name}'.")
    else:
        print("Invalid option.")

def handle_delete():
    print("You selected 'delete'.")
    option = input("Do you want to delete 'class' or 'student'? ")
    if option.lower() == "class":
        print("Available classes:", list(bakueuropeanlyceum.keys()))
        class_name = input("Enter the class name to delete: ")
        if class_name in bakueuropeanlyceum:
            bakueuropeanlyceum.pop(class_name)
            print(f"Class '{class_name}' deleted successfully!")
        else:
            print(f"Error: Class '{class_name}' does not exist.")
    elif option.lower() == "student":
        class_name = input("Enter the class name: ")
        student_id = input("Enter the student ID to delete: ")
        if class_name in bakueuropeanlyceum and student_id in bakueuropeanlyceum[class_name]:
            bakueuropeanlyceum[class_name].pop(student_id)
            print(f"Student '{student_id}' deleted from class '{class_name}' successfully!")
        else:
            print(f"Error: Student '{student_id}' not found in class '{class_name}'.")
    else:
        print("Invalid option.")

ask = input("What do you want to do?(create, read, change, delete):")

if ask.lower()=="create":
    handle_create()
elif ask.lower() == "read":
    handle_read()
elif ask.lower() == "change":
    handle_change()
elif ask.lower() == "delete":
    handle_delete()
else:
    print("Invalid option. Please choose one of: create, read, change, delete.")