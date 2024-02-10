destination_weight = 0
gravity = 0

# float input function returns the input as a decimal
earth_weight = float(input('Enter your weight: '))
planet = int(input('Enter the planet number (1-7): '))

if planet == 1: 
  gravity = 0.38
elif planet == 2:
  gravity = 0.91
elif planet == 3:
  gravity = 0.38
elif planet == 4:
  gravity = 2.53
elif planet == 5:
  gravity = 1.07
elif planet == 6:
  gravity = 0.89
elif planet == 7:
  gravity = 1.14
else: 
  print('The number you have inputted was not recognized. Please try again')

destination_weight = (earth_weight * gravity)
print(destination_weight)

# at first I tried adding print to all of the elif statements and then realized that was redundant, so.. oops
