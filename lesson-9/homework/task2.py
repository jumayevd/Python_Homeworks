import csv
import os
grades_file = 'lesson-9/homework/grades.csv'
output_file = os.path.join(os.path.dirname(grades_file), 'average_grades.csv')

data = []

with open(grades_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({"Name": row["Name"], "Subject": row["Subject"], "Grade": int(row["Grade"])}
)

#Calculate the average grade for each subject.
averages = {}

# Group grades by subject
for record in data:
    subject = record["Subject"]
    grade = record["Grade"]
    if subject not in averages:
        averages[subject] = []
    averages[subject].append(grade)


average_grades = {subject: sum(grades) / len(grades) for subject, grades in averages.items()}



with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, average in average_grades.items():
        writer.writerow([subject, round(average, 2)])

print(f"Average grades have been written to {output_file}.")
