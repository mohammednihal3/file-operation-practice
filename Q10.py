f=open("student2.txt","a")

name=input("enter student name:")
course=input("course name:")
age=input("age :")
mark=input("enter mark:")

f.write("\nname:"+name)
f.write("\ncourse:"+course)
f.write("\nage"+age)
f.write("\nmark"+mark)
f.write("\n*************")
f.close()