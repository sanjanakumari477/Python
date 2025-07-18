num = int(input("Enter a number: "))

# Check if number is positive, negative, or zero
if num > 0:
    print("Number is Positive")

    # Check even or odd
    if num % 2 == 0:
        print("It is Even")
    else:
        print("It is Odd")

    # Nested if to check prime
    if num == 1:
        print("1 is neither prime nor composite")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print("It is a Prime Number")
        else:
            print("It is Not a Prime Number")

elif num < 0:
    print("Number is Negative")

    # Check divisibility
    if num % 3 == 0:
        print("It is divisible by 3")
    else:
        print("It is not divisible by 3")

else:
    print("Number is Zero")
    print("Zero has no sign and is not prime or odd/even")
