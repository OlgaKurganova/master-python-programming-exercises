
def apple_sharing(n,k):
  # Your code here
  # Calculate how many apples each student gets
    apples_per_student = k // n
    # Calculate how many apples remain in the basket
    remaining_apples = k % n

     # Return both results as a tuple
    return apples_per_student, remaining_apples
 

print(apple_sharing(6,50))
