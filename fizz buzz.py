# when using range() you need to take the greatest number in the range you want and add one to it for it to actually print what you want

for number in range(1, 101):
  if number % 3 == 0:
    print ("Fizz")
  elif number % 5 == 0:
    print ("Buzz")
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  else:
    print(number)

# % is the modulo operator, can be used to find whether a number is the multiple of something else
