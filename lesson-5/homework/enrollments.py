import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    enrollments = [university[1] for university in universities]
    tuitions = [university[2] for university in universities]
    return enrollments, tuitions

def mean(data):

    return sum(data) / len(data)

def median(data):

    return statistics.median(data)

enrollments, tuitions = enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)
mean_students = mean(enrollments)
median_students = median(enrollments)
mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}")
print()
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,}")
print("******************************")