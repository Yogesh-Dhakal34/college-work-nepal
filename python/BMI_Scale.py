#Develop a program to calculate the BMI given weight in kilograms and height in centimeters.


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

BMI = weight/((height*height)/10000)

print(f"The BMI is: {BMI:.1f}")

if(BMI<18.5):
    print("You need to consume some more , you are thin like a branch.")
  
elif(BMI>18.5 and BMI<24.9):
    print("You are the embodiment of a perfect body.")
  
elif(BMI>25 and BMI<29.9):
    print("You are closer to being a truck so reduce your consumption.You are a little over a healthy body.")
  
else:
    print("Congratulation!. You are beyond a normal person category so either seek medical advise or stop consuming at all. Fattiest FATTY")

