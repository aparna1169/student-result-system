
while True:
    name=input("enter student name:")
    s1=int(input("enter 1st sub marks="))
    s2=int(input("enter 2nd sub marks="))
    s3=int(input("enter 3rd sub marks="))
    total=s1+s2+s3
    avg=total/3
    print("total=",total,"average=",avg)
    if avg>=95:
        print("GRADE A CONGRATSS BROO")
    elif avg>=75:
        print("GRADE B BROO TRY HARDER")
    else:
        print("FAILL COME ONN STUDY BROO")

    with open("students.txt","a") as f:
        f.write(f"{name},{s1},{s2},{s3},{total},{avg}\n")
    choice=input("are you ready for another ones marks??(yes/no):").strip().lower()
    if choice=="no":
        print("program ended now goo see your kids veshalu")
        break

 
