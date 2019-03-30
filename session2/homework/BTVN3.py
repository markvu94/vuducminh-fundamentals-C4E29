height = float(input("dien chieu cao (cm) "))
weight = float(input("dien can nang(kg) "))
BMI = weight/((height/100)**2)

if BMI <16:
    print("severely underweight")
elif BMI <18.5:
    print("underweight")
elif BMI <25:
    print("normal")
elif BMI <30:
    print("overweight")
else:
    print ("obese")




