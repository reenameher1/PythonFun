prime = int(input("Enter the number you want to verify: "))

if prime > 1:
    for i in range(2, prime):
        if(prime % i) == 0:
            print("%d is not a prime number" %(prime))
            print("%d times %d = %d" %(i,prime/i,prime))
            break
    else:
         print("%d is a prime number" %(prime))

else:
    print("%d is not a prime number" %(prime))
