birth_year=int(input("Enter your birth year:"))
current_year=int(input("Enter the current year:"))
age=current_year-birth_year
years_you_have=90-age
months_you_have=years_you_have*12
weeks_you_have=years_you_have*52
days_you_have=years_you_have*365
print(F"You have total {months_you_have} months, {weeks_you_have} weeks and {days_you_have} Days to touch 90s.")
