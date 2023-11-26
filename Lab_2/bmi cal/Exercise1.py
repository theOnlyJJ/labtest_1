def calculate_bmi (height,weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))
    #weight
    bmi = weight/(height*height)
    if (bmi < 18.5):
        print("Under Weight")
        return -1
    if (bmi >= 18.5 and bmi <= 25):
        print("Normal weight")
        return 0
    if (bmi > 25):
        print("Over Weight")
        return 1

    print(bmi)

calculate_bmi(weight=57,height=1.73)