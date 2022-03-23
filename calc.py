
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

print("1. Add\n2. Sub\n3. Product\n4. Divide\n5. Power\n6. Cube\n7. Sqrt")

num_3 =int(input("Enter an input to calculate: "))

if num_3 == 1:
    add = num_1+num_2
    print("The sum is",add)

if num_3 == 2:
    sub = num_1-num_2
    print("The sub is",sub)

if num_3 == 3:
   product = num_1*num_2
   print("The product is",product)

if num_3 == 4:
   div = num_1/num_2
   print("The div is",div)

if num_3 == 5:
   power = num_1**num_2
   print("The power is",power)

if num_3 == 6:
   Cube_1 = num_1**3
   Cube_2 = num_2**3
   print("The cube of 1st no is",Cube_1)
   print("The cube of 2nd no is",Cube_2)

if num_3 == 7:
    sqrt_1 = num_1**0.5
    sqrt_2 = num_2**0.5
    print("The sqrt of 1st no is",sqrt_1)
    print("The sqrt of 2nd no is",sqrt_2)

