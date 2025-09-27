medical_cause = input("Do you have a medical cause Yor N: ")
atten = int(input("enter the attendance of student"))

if medical_cause == 'Y': # checking the condition 1
    print("you are allowed")
else:
    if atten>=75: #Checking the condition 2
        print("Allowed")
    else:
        print("Not allowed")