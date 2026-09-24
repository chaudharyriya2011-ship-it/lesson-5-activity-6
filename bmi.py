height = float(input("Enter height in cms "))
weight = float(input("enter weight in kg "))
bmi = weight/(height/100)**2
print("The bmi is " , bmi )
if bmi<=18.5:
    print("Under weight")
elif bmi<=24.9:
    print("healthy")
elif bmi<=29.9:
    print("over weight")
elif bmi<=39.9:
    print("severe over weight")
else:
    print("obese")