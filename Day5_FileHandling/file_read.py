with open("marks.txt") as f:
    marks = [int(mark.strip()) for mark in f.readlines()]

print("Marks Report\n")
student = 1
total_marks =0
for mark in marks:
    total_marks += int(mark)    
    print(f"Student: {student} : {mark}")   
    student +=1
print("------------------")
print("Total marks : ",total_marks)
print("Average marks : ",int(total_marks) / int(len(marks)))
print("Highest marks : ",max(marks))
print("Lowest marks : ",min(marks))



'''
with open("movies.txt") as f:
    counter =1
    for movie in f:        
        print(f"Movie {counter}: {f.readline()}")
        counter +=1

counter = 0
    for movie in f:
        content = f.readline()
        if content == "":
            break
        print("Movie",counter+1 ,":", content)
        counter += 1
'''