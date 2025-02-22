while True :
    salary = float(input("Please enter your salary for the month: "))
    month_name = input("Please enter the name of the month you are storing the salary for: ")
    rent_percentage = float(input("Enter the percentage allocated for rent: "))
    electricity_percentage = float(input("Enter the percentage allocated for electricity: "))
    savings_percentage = float(input("Enter the percentage allocated for savings: "))
    total_percentage = savings_percentage + rent_percentage + electricity_percentage
    if total_percentage >100 :
     print(f"error:total percentage is {total_percentage}%,which exceeds 100%. please try again")
    else :
     break
    
    # Calculate the amounts allocated to savings, rent, and electricity
savings = salary * (savings_percentage / 100)
rent = salary * (rent_percentage / 100)
electricity = salary * (electricity_percentage / 100)
    
    # Calculate total spending on savings, rent, and electricity
total_expenses = savings + rent + electricity
    #calculate the remainder of the salary after expenses
remainder = salary - total_expenses
    #yearly rent and electricity costs
yearly_rent = rent * 12
yearly_electricity = electricity * 12
    #salary raised to the power of 2 (just for fun)
salary_squared = salary ** 2
    # Assume Nabiha saves an additional random amount, e.g., $50
additional_savings = 50
savings_ratio = additional_savings / savings if savings != 0 else 0



print(f"\nResults for {month_name}:") 
print(f"1. Amount allocated to savings: ${savings:.2f}")
print(f"2. Amount allocated to rent: ${rent:.2f}")
print(f"3. Amount allocated to electricity: ${electricity:.2f}")
print(f"4. Total amount spent on savings, rent, and electricity: ${total_expenses:.2f}")
print(f"5. Remaining salary after expenses: ${remainder:.2f}")
print(f"yearly rent: ${yearly_rent}")
print(f"yearly electricity: ${yearly_electricity}")
print(f"7. Your salary raised to the power of 2 (for fun!): ${salary_squared:.2f}")
print(f"If you saved an additional ${additional_savings} this month, it would be {savings:.2f} times the amount allocated to savings.")



