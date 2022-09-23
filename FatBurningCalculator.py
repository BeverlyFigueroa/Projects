#Created by Beverly Figueroa
#Fat Burning Heart Rate and BMI Calculator

print("Welcome to the Weber State University Human Performance Lab!")
print("Please utilize the following calculator to find your ideal fat burning heart rate and BMI.\n")

age = ()
height = ()
weight = ()

while True:
    try:
        age = int(input("Enter age: "))

        if age <= 0:
            raise TypeError("Invalid age value. Age must be greater than zero.")
        break
    except ValueError:
        print("Invalid age. Must be a number.")
    except TypeError as err:
        print(err)
    except:
        print("Invalid input")
    
while True:
    try:
        height = int(input("Enter height in inches: "))
        if height <= 0:
            raise TypeError("Invalid inches value. Height must be greater than zero.")
        break
    except ValueError:
        print("Invalid inches value. Height must be a number.")
    except TypeError as err:
        print(err)
    except:
        print("Invalid input")

while True:
    try:
        weight = int(input("Enter weight in pounds: "))
        if weight <= 0:
            raise TypeError("Invalid weight value. Weight must be greater than zero.")
        break
    except ValueError:
        print("Invalid weight value. Weight must be a number.")
    except TypeError as err:
        print(err)
    except:
        print("Invalid input")

print("Age =", age)
print("Height =", height, "in.")
print("Weight =", weight, "lbs.\n")

#Maximum heartrate
maxhr = 220 - age
#fatburning heartrate = 70% of maxhr
fbhr = round(maxhr * .70)
print("Fat Burning Heart Rate =", fbhr, "bpm")

bmi = (weight * 703) / (height * height)
print("Body Mass Index =", round(bmi,2))