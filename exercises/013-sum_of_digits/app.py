# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
    
    num = (num // 10)% 10

    return num+num+num



# Invoke the function with any three-digit number
print(digits_sum(123))
