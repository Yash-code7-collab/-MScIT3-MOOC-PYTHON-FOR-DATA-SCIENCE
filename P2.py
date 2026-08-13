
student_marks=[50,68,45,45,80,99,45,68,89,70]
student_names=["yash","meet","Dhruvi","Urvish","Pratik","Hero","Anis","Natho","Urvesh","Dhamo"]
student_tuple_marks=tuple(student_marks)
student_dict=dict()

print("Marks List :: ",student_marks)
print("Name List :: ",student_names)
print("Marks in tuple :: ",student_tuple_marks)

for i,j in zip(student_marks,student_names):
    student_dict[j]=i
    

print("Dict :: ",student_dict)

avg = sum(student_marks)/len(student_marks) # divide for find avreage


print("Highest Name :: ",max(student_marks))
print("Lowest Name :: ",min(student_marks))
print("Average Name :: ",avg)

print("Marks Above Avrage")
for i,j in student_dict.items():
    if j > avg:
        print("Name --> ",i,",Marks --> ",j)


ConvertedSet_marks=set(student_marks)
print("Converte tuple of Marks into set :: ",ConvertedSet_marks)