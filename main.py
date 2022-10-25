from add import add_fruit
from divide import divide_fruit
from multiply import multiply_fruit
apples = int(input("how many apples? "))
oranges = int(input("how many oranges? "))
fruit = add_fruit(apples, oranges)
print(fruit)
divide = divide_fruit(apples, oranges)
print(divide)
multiply = multiply_fruit(apples, oranges)
print(multiply)