


while True:
    print ("hello")
    salary = float(input("enter the salary for the month:  $")) 
    month = input("enter the name of the month you are storing the salary for: ")
    saving = float(input("please enter percentage for saving: "))
    rent = float(input("please enter percentage for rent: "))
    electricity = float(input("please enter percentage for electricity: "))

    total_percentage = saving + rent + electricity

    if total_percentage >100:
      print(f"error:the total percentage is {total_percentage}%,which exceeds 100%. please try again.")
    else:
       print({"total_percentage"})

        
print(f"saving:{saving}%")
print(f"rent:{rent}%")
print(f"electricity:{electricity}%")