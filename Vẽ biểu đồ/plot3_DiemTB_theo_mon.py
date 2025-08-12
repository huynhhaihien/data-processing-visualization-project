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

average = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	total = 0
	for i in range(11):
		if s[i+5] != "-1":
			count += 1
			total += float(s[i+5])

	average[count] += float(total)/count 
	num_of_exam_taken[count] += 1
for i in range(12):
	if num_of_exam_taken[i] != 0:
		average[i] = round(average[i]/num_of_exam_taken[i], 2)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.arange(12)

figure, axis = plt.subplots()
plt.bar(x, average)

axis.set_ylim(0,10)

plt.xticks(x, y)

axis.set_ylabel('Điểm trung bình')
axis.set_xlabel('Số môn thi')
plt.title('Điểm trung bình theo số môn thi')


rects = axis.patches


for rect, label in zip(rects, average):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height, label, ha="center", va="bottom"
    )


plt.show()