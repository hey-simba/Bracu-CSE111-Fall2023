

#Task1
def amikenomota(height,weight):
      height=height/100
      bmi=weight/(height**2)
      bmi=round(bmi,1)
      if bmi<18.5:
        print(f"Score is {bmi}. You are Underweight")
      elif 18.5<=bmi<=24.9:
        print(f"Score is {bmi}. You are Normal")
      elif 25<=bmi<=30:
        print(f"Score is {bmi}. You are Overweight")
      else:
        print(f"Score is {bmi}. You are Obese")
h=int(input("Please give your height in cm: "))
w=int(input("Please give your weight in kg: "))
amikenomota(h,w)