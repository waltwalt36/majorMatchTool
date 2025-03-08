import csv

# Example dictionary where the key is the major and the value is a list of courses
majors_courses = {
    "Animal Science": [
        "AVS 1500 - Introduction to Animal Science",
        "AVS 1510 - Introduction to Animal Science Laboratory",
        "BIOL 1030 - General Biology I",
        "BIOL 1040 - General Biology II"
    ],
    "Computer Science": [
        "CS 1010 - Introduction to Computer Science",
        "CS 1020 - Data Structures"
    ],
    "Mechanical Engineering": [
        "ME 1010 - Introduction to Mechanical Engineering",
        "ME 2010 - Thermodynamics",
        "ME 2020 - Fluid Mechanics"
    ]
}

# Create or open the CSV file to write data
with open('majors_courses.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Major", "Course"])

    # Write each major and its corresponding courses
    for major, courses in majors_courses.items():
        for course in courses:
            writer.writerow([major, course])

print("CSV file created successfully!")