# Complete the function to return the tens digit of a given integer
def tens_digit(num):

  num = num // 10

  return num % 10


# Invoke the function with any integer
print(tens_digit(123))
