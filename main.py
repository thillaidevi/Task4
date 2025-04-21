print("1. Create odd and even list Program")

python_list=[10,501,22,37,100,999,87,351] # Input list is given

'''To find even and add number in the given list, 
checked for conditional statement'''
even_number_list=[number for number in python_list if number % 2 ==0] # Condition checked for even number list

odd_number_list=[number for number in python_list if number % 2 !=0] # Condition checked for odd number list

# To print the even list
print("Even number list is:")
print(even_number_list)

# To print the odd list
print("Odd number list:")
print(odd_number_list)


print("2. Get Prime number list and count the Prime numbers Program")
python_list = [10, 501, 22, 37, 100, 999, 87, 351] # Input list is given
prime = []  # Initialize an empty list to store prime numbers found

# Iterate through each number in the python_list
for i in python_list:
    prime_counter = 0  # Initialize a counter for the number of divisors of 'i'
    # A prime number has exactly two divisors: 1 and itself.

# Iterate through numbers from 1 up to (but not including) the current number 'i'
    for j in range(1, i):
        # Check if 'i' is perfectly divisible by 'j'
        if i % j == 0:
            # If 'i' is divisible by 'j', it means 'j' is a divisor of 'i'.
            # Increment the prime_counter because we found a divisor.
            prime_counter += 1

    # After checking all numbers from 1 to i-1, if the prime_counter is equal to 1,
    # it means that the number 'i' has exactly one divisor in the range (1, i).

    if prime_counter == 1: # Checks the condition
        prime.append(i)  # If 'i' is prime, add it to the 'prime' list

#print the output
print(f"Original list: {python_list}") # Printing original list
length=len(prime) #count the prime numbers
print("Prime number's Count: ", length) #print the count

print(f"Prime numbers found: {prime}") # Prime list is printed



print("3. Find and count the Happy Numbers from the python list Program")
'''A happy number is a number which eventually reaches 1 when replaced by the sum of the square of its digits repeatedly. 
If the process loops endlessly in a cycle that does not include 1, then the number is not a happy number'''

python_list = [10, 501, 22, 37, 100, 999, 87, 351] # Input list is given

happy_numbers = [] # Initialize an empty list to store the happy numbers.

count = 0 # Initialize counter as 0

# Iterate through each number in the python_list
for num in python_list:
    seen = set()  # Keep track of numbers encountered to detect cycles
    n = num
    # Continue the process until n becomes 1 (happy number) or a cycle is detected
    while n != 1 and n not in seen:
        seen.add(n)

        digit_sum_of_squares = 0 # Initialize a variable to store the sum of squared digits.

        # Calculate the sum of the squares of the digits
        for digit in str(n):
            digit_sum_of_squares += int(digit)**2 # Convert each digit to an integer, square it, and add it to the sum.

        n = digit_sum_of_squares  # Update 'n' with sum of squared digits.

    # If n is 1, the original number is a happy number
    if n == 1:
        happy_numbers.append(num) # Add the happy number to the 'happy_numbers' list.
        count += 1 # If it's a happy number, increment the counter

# Print the list of happy numbers found
print("Happy Numbers:", happy_numbers)

# Print the total count of happy numbers
print("Count of Happy Numbers:", count)



print("4. Sum of first and last digit of an integer program:")
print( "Please Enter an integer number: ")

number = int(input()) # Get integer input from the user

# We are type casting it in string, since we need to use the index
number = str(number)

# Storing first and last digit in a variable
first_digit = int(number[0]) # First digit is getting by index of 0
last_digit = int(number[-1]) # Last digit is getting by negative index value of -1

# Adding these two variables
addition = first_digit + last_digit

# Display our output
print('Addition of first and last digit of the number is', addition)


print("5. Ways to make Rs.10 using Rs.1, Rs.2,Rs.5 and Rs 10 coins in python Program")
# Initialize Rs.10 target value
target = 10

# The code uses nested loops to explore all possible combinations of Rs. 1, Rs. 2, Rs. 5, and Rs. 10 coins.
# The  '//' operator performs integer division, discarding any remainder. This is used to limit the loops to the maximum possible number of each coin

for coin1 in range(target + 1):
# The outer loop (coin1) iterates through all possible quantities of Rs. 1 coins (from 0 up to the target amount)

    for coin2 in range(target // 2 + 1):
    # The next inner loop (coin2) iterates through all possible quantities of Rs. 2 coins

        for coin5 in range(target // 5 + 1):
        #The next inner loop (coin5) iterates through all possible quantities of Rs. 5 coins

            for coin10 in range(target // 10 + 1):
            # The next inner loop (coin10) iterates through all possible quantities of Rs. 10 coins

                # Check if the combination matches the target value
                if coin1 + coin2 * 2 + coin5 * 5 + coin10 * 10 == target:
                    print(f"Rs.1: {coin1}, Rs.2: {coin2}, Rs.5: {coin5}, Rs.10: {coin10}")


print("6. Find the Duplicates in the 3 lists Program")
# Define the first list of integers
List1 = [10,10,11,12,15,16,18,19 ]  #list1 input is given

# Define the second list of integers
List2 = [10,11,13,15,16,19,20]  #list2 input is given

# Define the third list of integers
List3 = [10,11,11,12,15,19,21,23]  #list3 input is given

# Print a message
print("Duplicates in the 3 lists are:")

# Convert List1 to a set and find its intersection with List2 and List3
print(set(List1).intersection(List2, List3))  #Duplicates values are printed as output


print("7. Find the first non-repeating elements in a list program")

# Input list of numbers
nums = [4, 5, 1, 2, 11, 4, 1, 5, 2]

# Variable to track if a non-repeating element is found
found = False  # Initially set to False, meaning no non-repeating element is found yet

# Outer loop to go through each element in the list
for i in range(len(nums)):  # Loop through the indices of the list
    repeating = False  # Assume the current element is not repeating

    # Inner loop to compare the current element with all other elements
    for j in range(len(nums)):  # Loop through the indices again to compare
        if i != j and nums[i] == nums[j]:  # Check if indices are different and values are the same
            repeating = True  # Mark the current element as repeating
            break  # Exit the inner loop as we found a repetition

    # If the current element is not repeating
    if not repeating:  # This condition is true for non-repeating elements
        print(f"The first non-repeating element is: {nums[i]}")  # Print the element
        found = True  # Update the variable to indicate we found a non-repeating element
        break  # Exit the outer loop since we've found the first non-repeating element

# If no non-repeating element is found after checking all elements
if not found:  # This runs if the `found` variable remains False
    print("No non-repeating elements found.")  # Print a message indicating no non-repeating elements exist



print("8. Find the minimum element of sorted and rated list program")
# Input list (sorted and rotated)
nums = [24, 35, 56, 79, 61, 82, 13]  # Example list

# Initialize variables
n = len(nums) # Count is assigned to n
min_element = nums[0]  # Assume the first element is the minimum

# Loop through the list to find the minimum element
for i in range(1, n):  # Start from the second element (index 1)
    if nums[i] < min_element:  # Compare with the current minimum
        min_element = nums[i]  # Update the minimum if a smaller element is found

# Print the output
print("Sorted List of [24, 35, 56, 79, 61, 82, 13] ---> ", sorted(nums))  # Sorting the array and print

# Print the minimum element
print(f"The Minimum element is: {min_element}")

print("9. Find the Triplets from the list [10, 20, 30, 9] with the value=59")
numbers = [10, 20, 30, 9]  # The input list of numbers
target_sum = 59  # The target sum
triplets = []  # An empty list to store the triplets that satisfy the condition

# Iterate through the list using nested loops to find all possible combinations of three numbers

for i in range(len(numbers)):
# Outer loop: iterates from the first element to the last

    for j in range(i + 1, len(numbers)):
    # Middle loop: iterates from the element after 'i' to the last

        for k in range(j + 1, len(numbers)):
        # Inner loop: iterates from the element after 'j' to the last

            # Check if the sum of the current three numbers equals the target sum
            if numbers[i] + numbers[j] + numbers[k] == target_sum:

                # If the sum is equal to the target sum, we found a valid triplet
                triplets.append((numbers[i], numbers[j], numbers[k]))  # Add the triplet to the 'triplets' list

# After checking all combinations, we check if any triplets were found
if triplets:
    # If the 'triplets' list is not empty, it means we found at least one triplet
    print("Triplets found:", triplets)  # Print the list of triplets
else:
    # If the 'triplets' list is empty, it means no triplets were found
    print("No triplets found that sum to", target_sum)  # Print a message indicating no triplets were found

print("10. Create Sublist with sum=0 from the list [4, 2, -3, 1, 6]")
numbers = [4, 2, -3, 1, 6]  # The input list of numbers
sublists_with_zero_sum = []  # List to store sublists that sum to 0

# Iterate through the list to find starting points of sublists
for i in range(len(numbers)):
    current_sum = 0  # Initialize sum for the current sublist

    # Iterate from the starting point to the end of the list
    for j in range(i, len(numbers)):

        current_sum += numbers[j]  # Add the current element to the sum

        # If the sum is 0, we found a valid sublist
        if current_sum == 0:
            sublists_with_zero_sum.append(numbers[i:j + 1])  # Add the sublist to the result list

# Print the results
if sublists_with_zero_sum:
    print("Sublists with sum 0:", sublists_with_zero_sum)
else:
    print("No sublists with sum 0 found")