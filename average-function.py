def average(a,b,c):
    average = (a + b + c)/3 
    return average
a = float(input("Entar 1st number: "))
b = float(input("Entar 2nd number: "))
c = float(input("Entar 3rd number: "))

result = average(a, b, c)
print(f"The average of entered numbers is: {result}")