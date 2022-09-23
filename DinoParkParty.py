#Dinosaur Park Party Planner
choice = 0
while choice < 4:
        print("Welcome to the Dinosaur Park Party Planner")
        print("Choose the type of party:")
        print("1. Group Rate Admission Party")
        print("2. Bare Bones Package")
        print("3. Deluxe Party Package")
        print("4. Quit")
        choice = int(input("Enter choice: "))

#1 Group Rate       
        if (choice == 1):
                print("By reserving a group party slot of 10 or more people your group will be admitted to the Park at the group discount rate.")
                adults = int(input("How many adults (13+) in your party? "))
                kids = int(input("How many kids (2-12) in your party? "))
                price = (adults * 5) + (kids * 4)
                print("Total cost for Group Rate Party Package will Be:", "$",price)
                price = 0
#2 Bare Bones            
        if (choice == 2):
                member = int(input("Are you a member? Press 1 for Yes and 2 for No: "))
                if (member == 1):
                        price = 99
                else:
                        price = 119
                print("The base price covers admission for up to 12 people.")
                add = int(input("Will there be more than 12 people? Press 1 for Yes and 2 for No: "))
                if (add == 1):
                        extra = int(input("Enter the amount of additional people: "))
                        price += (extra * 3)
                print("Total cost for Bare Bones Party Package will Be:", "$",price)
                price = 0
#3 Deluxe
        if (choice == 3):
                member = int(input("Are you a member? Press 1 for Yes and 2 for No: "))
                if (member == 1):
                        price = 175
                else:
                        price = 199
                print("The base price covers admission for up to 12 people.")
                add = int(input("Will there be more than 12 people? Press 1 for Yes and 2 for No: "))
                if (add == 1):
                        extra = int(input("Enter the amount of additional people: "))
                        price += (extra * 3)   
                print("Total cost for Deluxe Party Package will be:", "$",price)   
                price = 0     
else:
        print("Thank you for using the Dinosaur Park Party Planner. Goodbye!")