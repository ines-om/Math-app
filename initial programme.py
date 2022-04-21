import math
import numpy
from numpy import e

print("------------- Properties of numbers! -------------")

n = input("Insert your number here: ")
nr = float(n)

print("The number inserted is: " + "\n")

#EVEN OR UNEVEN
if (nr%2==0): 
    print("- even; ")
if (nr%2==1): 
    print("- uneven; ")

#Finding divisors
numbers = []    
for i in range (1, (int(nr)+1)):
    if (nr%i==0):
        numbers.append(i)

#PRIME OR NOT
if numbers == [1, int(n)]:
    print("- a prime number;")

#DIVISIBILITY
print("- divisible by: ")
for number in numbers:
    print("  -- " + str(number))

#If number is prime
if numbers == [1, int(n)]:
    print("factorization: " +  str(n))
if (len(numbers) == 3):
    number_square = numbers[1]
    square = (number_square)
    print("Factorization: "+ str(square) + "^2")


else:
    primes= []
    exponent = []
    for number in numbers:
        divisors = []
        for i in range(1, (int(number))):
            if (number%i==0): 
                divisors.append(i)
            if i == (int(number)-1):
                if (len(divisors)==0):
                    primes.append(number)
                elif (len(divisors)==1):
                    primes.append(number)
                else:
                    exponent.append(number)

    print(primes)
                


