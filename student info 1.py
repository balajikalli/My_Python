# Define the students' information as a list of dictionaries

students = [
    {
        "Name": "John Doe",
        "ID": 123456,
        "Date of Birth": "1999-05-15",
        "Gender": "Male",
        "Email": "john.doe@example.com",
        "Phone": "(555) 123-4567",
        "Address": "123 Main St, Springfield, USA",
        "Course": "Computer Science",
        "Year": "3rd Year",
        "GPA": 3.8,
        "Emergency Contact": {
            "Name": "Jane Doe",
            "Relationship": "Mother",
            "Phone": "(555) 987-6543"
        }
    },
    {
        "Name": "Emily Smith",
        "ID": 234567,
        "Date of Birth": "2000-08-22",
        "Gender": "Female",
        "Email": "emily.smith@example.com",
        "Phone": "(555) 234-5678",
        "Address": "456 Elm St, Springfield, USA",
        "Course": "Mechanical Engineering",
        "Year": "2nd Year",
        "GPA": 3.6,
        "Emergency Contact": {
            "Name": "Robert Smith",
            "Relationship": "Father",
            "Phone": "(555) 876-5432"
        }
    },
    {
        "Name": "Michael Brown",
        "ID": 345678,
        "Date of Birth": "1998-11-30",
        "Gender": "Male",
        "Email": "michael.brown@example.com",
        "Phone": "(555) 345-6789",
        "Address": "789 Oak St, Springfield, USA",
        "Course": "Business Administration",
        "Year": "4th Year",
        "GPA": 3.9,
        "Emergency Contact": {
            "Name": "Linda Brown",
            "Relationship": "Sister",
            "Phone": "(555) 765-4321"
        }
    }
]

# Print the student information
for student in students:
    print("Student Information")
    print("--------------------")
    print(f"Name: {student['Name']}")
    print(f"ID: {student['ID']}")
    print(f"Date of Birth: {student['Date of Birth']}")
    print(f"Gender: {student['Gender']}")
    print(f"Email: {student['Email']}")
    print(f"Phone: {student['Phone']}")
    print(f"Address: {student['Address']}")
    print(f"Course: {student['Course']}")
    print(f"Year: {student['Year']}")
    print(f"GPA: {student['GPA']}")
    print("\nEmergency Contact")
    print("-----------------")
    print(f"Name: {student['Emergency Contact']['Name']}")
    print(f"Relationship: {student['Emergency Contact']['Relationship']}")
    print(f"Phone: {student['Emergency Contact']['Phone']}")
    print("\n-------------------------------------\n")
