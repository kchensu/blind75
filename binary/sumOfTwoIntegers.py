def sumOfTwoIntegers(num1, num2):
    while (num2 != 0):
        carry = (num1 & num2) << 1
        print(carry)
        num1 = num1 ^ num2
        num2 = carry
    return num1


print(sumOfTwoIntegers(1, 1))
