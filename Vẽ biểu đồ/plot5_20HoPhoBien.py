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

name = []
name_count = []

for s in students: 
	s_name = s[1].split(" ")
	lastname = s_name[0]
	if lastname not in name:
		name.append(lastname)
		name_count.append(1)
	
	else:
		name_count[name.index(lastname)] += 1

counted_max_num = []
sort_index  = []

for i in range(len(name)):
	max_number = 0
	for j in range(len(name)):
		if name_count[j] > max_number and name_count[j] not in counted_max_num:
			max_number = name_count[j]

	counted_max_num.append(max_number)

for max_num in counted_max_num:
	for i in range(len(name)):
		if name_count[i] == max_num and i not in sort_index:
			sort_index.append(i)

name_sorted = []
name_count_sorted = []

for index in sort_index:
	name_sorted.append(name[index])
	name_count_sorted.append(name_count[index])

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(20)
y = np.arange(20)

fig, axis = plt.subplots()

plt.bar(x, name_count_sorted[0:20])

axis.set_ylim(0, 25000)

plt.xticks(x, name_sorted[0:20])

axis.set_ylabel('Số học sinh')
# axis.set_xlabel('Tuổi')

rects = axis.patches 

labels = name_count_sorted[0:]
for rect, label in zip(rects, labels):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')
plt.title('20 họ phổ biến trong kì ')

plt.show()