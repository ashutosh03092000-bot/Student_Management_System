# Importing important libraries
import random,string
# Taking an empty list to store student ids
student_id=[]
# Taking an empty list to store student names
student_name=[]
# Taking an empty list to store students age
student_age=[]
# Taking an empty list to store students city
student_city=[]
# Taking an empty dictionary to store student details
student={}

# Function to add a student
def Add(name,age,city):
    # Generating random alphanumeric id of length 6
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    # Appending student details in their respective lists
    student_id.append(id)
    student_name.append(name)
    student_age.append(age)
    student_city.append(city)
    # Updating dictionary with student records
    student.update({id:[name,age,city]})
    # Using for loop to print student details
    for key,value in student.items():
        print(f"Student(id,name,age,city): {key,value}\n")

# Function to update student records
def update():
    # Asking for id to update records
    i=input("Enter id:")
    if i in student.keys():
        name=input("Enter a name:")
        age=int(input("Enter a age:"))
        city=input("Enter a city:")
        # Updating the dictionary with new records however id remains the same
        student.update({i:[name,age,city]})
        print("Updated successfully!\n")
    else:
        print("Enter a valid id!\n")

# Function to delete any record
def Delete():
    # Asking for id
    i = (input("Enter id:"))
    # If id is present in dictionary then poping that record from the dictionary
    if i in student.keys():
        student.pop(i)
        print("Record deleted successfully.\n")
    else:
        print("Enter a valid id!\n")

# Function to view any record
def View():
    # Asking for id
    i = input("Enter id:")
    # Checking if the id is present in the dictionary
    if i in student.keys():
        # Displaying desired record
        for key, value in student.items():
            if key==i:
                print(f"Student details: {key,value}\n")
    else:
        print("Enter a valid id!\n")

#Driver code
if __name__ == '__main__':
    print("\t\t\tStudent Management System\n")
    # Creating an infinite loop
    while True:
        print("1.Add 2.Updated 3.Delete 4.View 5.Save 6.Quit")
        # Asking for choice
        try:
            choice= int(input("Enter a choice:"))
        except Exception as e:
            print("Select a valid option!\n")
            continue

        #if choice 1 is selected then Add() function is called
        if choice==1:
            n=input("Enter name:")
            a=int(input("Enter age:"))
            c=input("Enter city:")
            Add(n,a,c)
        # if choice 2 is selected then Update() function is called
        elif choice==2:
            update()
        # if choice 3 is selected then Delete() function is called
        elif choice==3:
            Delete()
        # if choice 4 is selected then View() function is called
        elif choice==4:
            View()
        # if choice 5 is selected then it is shows saving the record
        elif choice==5:
            print("Saved Successfully!\n")
        # if choice 6 is selected then its breaking the loop
        elif choice==6:
            break
        else:
            print("Enter a valid choice.\n")
