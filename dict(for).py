n=int(input("How many students?"))
students={}
for i in range(n):
    name=input(f"Enter name of student{i+1}:")
    mark=int(input(f"Enter mark of{name}:"))
    students[name]=mark
    print("\nDictionary:",students)
    topper=max()
       