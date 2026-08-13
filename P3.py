# create List for inputs
roll_no = []
name = []
ds = []
java = []
c = []
python = []
html = []

# Accept the details of 10 students
for i in range(1,11):
    roll_no.append(int(input("Enter Roll NO :: ")))       # Roll Number
    name.append(input("Enter Name :: "))      # Name

    ds.append(int(input("Enter DS :: ")))     # Marks in 5 subjects
    java.append(int(input("Enter Java :: ")))     # Store the student information using appropriate Python data structures (lists, tuples, and dictionaries)
    c.append(int(input("Enter C :: ")))
    python.append(int(input("Enter Python :: ")))
    html.append(int(input("Enter HTML :: ")))

print(roll_no)
print(name)
print(ds)
print(java)
print(c)
print(python)
print(html)

total_per = []
total_mark = []
grade_dict ={"A":[],"B":[],"C":[],"D":[],"F":[]}

print("="*70)
for i in range(0,len(name)):
    
    total = ds[i]+java[i]+c[i]+python[i]+html[i]        # Total Marks
    per = (ds[i]+java[i]+c[i]+python[i]+html[i])/5      # Percentage
    total_mark.append(total)
    total_per.append(per)

    if per > 80 :     # Grade (A, B, C, D, F)
        grade = "A"
    elif per > 70 :
        grade = "B"
    elif per > 60 :
        grade = "C"
    elif per > 40 :
        grade = "D"
    elif per < 35 :
        grade = "F"

    print("Name :: ",name[i],"\tTotal Marks :: ",total,"\tper :: ",per,"\tGrade :: ",grade)
    grade_dict[grade].append(name[i])      #Key = Grade
                                        #Value = List of students belonging to that grade
print("="*70)

print("Name with Grade",grade_dict)
class_score_avg = sum(total_mark)/len(total_mark)

print("Class Average Per :: ",sum(total_per)/len(total_per))        #Class average percentage
print("Highest Score :: ",max(total_mark))      # Highest scorer(s)
print("Lowest Score :: ",min(total_mark))       # Lowest scorer(s)

# Students scoring above the class averag

top_mark = []

for i in range(len(total_mark)):
    if total_mark[i] > class_score_avg :
        top_mark.append(i)
    else:
        continue

top_std_list = dict()
print("Class Avrege :: ",class_score_avg)

for i in top_mark:
    top_std_list[name[i]] = total_mark[i]

print(top_std_list)

# Students who failed in one or more subject     

print("Failed Student :: ",grade_dict["F"])

# Display the names of students in alphabetical order without modifying the original records.

sort_name = sorted(name)
print("Soerted Name :: ",sort_name)

# Find the second-highest scorer without sorting the entire dataset.

sec = -1
sec_name = ""

for i in range(len(name)):
    if total_mark[i] < max(total_mark) and total_mark[i] > sec:
        sec = total_mark[i]
        sec_name = name[i]

print("Sec Score :: ",sec)
print("sec Name :: ",sec_name)

# Display the subject in which the class has obtained the highest average marks.

sub_avg = {"ds":sum(ds)/len(name),"java":sum(java)/len(name),"c":sum(c)/len(name),"python":sum(python)/len(name),"html":sum(html)/len(name)}
highest_sub = max(sub_avg, key=sub_avg.get)

print("Highest Average Subject Name ::", highest_sub)
print("Average Marks ::", sub_avg[highest_sub])

# Remove duplicate student names (if any) and report the duplicate entries

uniq_name = set()
duplicat = dict()

for i in name :
    if i in uniq_name:
        duplicat [i] = duplicat.get(i, 1) + 1
    else :
        uniq_name.add(i)

print("Uniq Name :: ",uniq_name)

# report the duplicate entries
if duplicat:
    for name, count in duplicat.items():
        print("Duplicat Values :: ",name,"Count :: ",count)
else:
    print("No duplicates found.")