students =[]
id =[]
i = 1
while True:
    names : str = input('Enter the student name')
    if names == 'stop':
        break
    if names in students:
        print('the name already exist')
    else:
        students.append(names)
        id.append(i)
        i+=1
    
for n in range(len(students)):
    print(f"{id[n]:<5} : {students[n]:<20}")


