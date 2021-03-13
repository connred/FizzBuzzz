#For loop to run thru numbers 1-100
for fizzbuzz in range(101):
    #check if multiple of 3 AND 5 
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz") #print
        continue
    #check if multiple of 3
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    #check if multiple of 5
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)