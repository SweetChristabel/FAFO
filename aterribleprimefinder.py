number = 2
counter = 0
print("Running finder...")
while True:
    divisor = 1
    amount = 0
    
    while True: 
        if number % divisor == 0:
            amount += 1
        divisor += 1
        if divisor >= number-1:
            break
    if divisor >= number-1:
        if amount == 1:
            print (number)
            counter += 1
        number += 1
    if number == 1000:
        break
print ("That is all")
print(f"Primes found: {counter}")