# Create a dictionary where:
# Keys = student names
# Values = marks (integer)
# Write a menu-based program where the user presses a key
# ('A', 'B', 'C', 'D') depending on the operation they want to perform:
# A - Add a student
# B - Update marks
# C - Search for a student
# D - Display all students and marks

dict={"riya":34}
while True:
    operation=input("enter ('A', 'B', 'C', 'D') or 'Q' to quit :")
    match operation:
        case "A":
            name=input("enter name:")
            marks=int(input("enter marks:"))
            dict.update({
                name:marks
            })
            print("updated dictionary -",dict)
        case "B":
            print("present dictionary -",dict)
            name=input("whose marks do you want to update:")
            marks=int(input("enter updated marks:"))
            dict[name]=marks
            print("updated dictionary -",dict)
        case "C":
            name=input("which student are you searching for:")
            for i in dict:
                if name==i:
                    print(name,":",dict[name])
                else:
                    print(name,"does not exist")
        case "D":
            print(dict)
        case "Q":
            print("Goodbuy!")
            break
        case _:
            print("wrong veriable!")