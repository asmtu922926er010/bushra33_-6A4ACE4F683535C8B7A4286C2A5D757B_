n=int(input("Enter the year:"))
   if n% 400==0and n% 100==0:
     print("The given year is leap year")
elif n%4==0and n%100=0:
     print("The given is leap year")
else:
     print("The given is not leap year")