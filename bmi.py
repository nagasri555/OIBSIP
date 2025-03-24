def body_mass(w,h):
    return w/h**2
w=float(input("Enter weight in kgs: "))
h=float(input("Enter height in meters: "))
BMI=body_mass(w,h)
print("BMI is : ",BMI)
if BMI <=18.5:
    print("You are under weight")
elif 18.5<BMI<=24.9:
    print("You are normal") 
elif 24.9<BMI<=29.9:
    print("You are over weight")
else:
    print("You are obese.")