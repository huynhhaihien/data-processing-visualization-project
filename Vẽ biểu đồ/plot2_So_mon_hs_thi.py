with open("clean_data.csv", "r", encoding='utf8') as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

header = header.split(",")
subjects = header[5:]

for i in range(len(students)):
	students[i] = students[i].split(",")

students.pop()

num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	for i in range(11):
		if s[i+5] != "-1":
			count += 1

	num_of_exam_taken[count] += 1

import matplotlib.pyplot as plt

labels = "0", "1", "2", "3", "4", "5", "6", "7", "8","9","10","11"  
sizes = [0, 80, 122, 2598, 4334, 318, 2730, 64261, 0, 0, 0, 1]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, startangle=90, autopct='%1.1f%%',colors=['orange', 'green', 'yellow', 'red', 'blue','gray' ],textprops={'size': 7}, radius=1,counterclock=False)

plt.title("Số môn học sinh thi")
plt.show()