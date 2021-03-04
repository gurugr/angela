heights = input("Enter students height :\n").split(" ")

for x in range(0,len(heights)):
  heights[x] = int(heights[x])


height_list = []
for height in heights:
  height_list.append(int(height))


print("Value List :",height_list)
total_height = 0
for max_val in height_list:
  total_height += max_val

print("total Height is : ",total_height)

total_student = 0
for student in range(0,len(height_list)):
  total_student += 1

print("Total Students :",total_student)

average = total_height/total_student
print("Total Round Avg :",round(average))
print("Total Avg :","%.2f" %average)







