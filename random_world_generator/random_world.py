import random

points = 50
weather = randint(1,10)
resources = None

if weather > 5:
  resources = randint(1,5)
else:
  resources = randint(5,10)


points -= weather
points -= resources

print "Points: ", points
print "Weather: ", weather
print "Resources: ", resources