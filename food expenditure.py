# the stuff itself isn't hard to do it's just that I was stuck on it for a hot min so it deserves to be here
times = float(input("How many times a week do you eat at the student cafeteria?: "))
price = float(input("The price of a typical student lunch?: "))
groc = float(input("How much money do you spend on groceries in a week?: "))

# I was having trouble w realizing that a daily variable isn't necessary if you have the weekly total since you can just divide it by 7
weekly = groc + price * times
print("Average food expenditure:")
print(f"Daily: {weekly/7} euros")
print(f"Weekly: {weekly} euros")
