print("1. Create odd and even list Program")

python_list=[10,501,22,37,100,999,87,351] #input list is given

'''To find even and add number in the given list, 
checked for conditional statement'''
even_number_list=[number for number in python_list if number % 2 ==0] #Condition checked for even number list

odd_number_list=[number for number in python_list if number % 2 !=0] #Condition checked for odd number list

#To print the even list and add list as an output
print("Even number list is:")
print(even_number_list)
print("Odd number list:")
print(odd_number_list)


print("2. Get Prime number list and count the Prime numbers Program")
python_list = [10, 501, 22, 37, 100, 999, 87, 351] #input list is given
prime = []  # Initialize an empty list to store prime numbers found

# Iterate through each number in the python_list
for i in python_list:
    prime_counter = 0  # Initialize a counter for the number of divisors of 'i'
    # A prime number has exactly two divisors: 1 and itself.


    # Iterate through numbers from 1 up to (but not including) the current number 'i'
    for j in range(1, i):
        # Check if 'i' is perfectly divisible by 'j'
        if (i % j == 0):
            # If 'i' is divisible by 'j', it means 'j' is a divisor of 'i'.
            # Increment the prime_counter because we found a divisor.
            prime_counter += 1

    # After checking all numbers from 1 to i-1, if the prime_counter is equal to 1,
    # it means that the number 'i' has exactly one divisor in the range (1, i).

    if (prime_counter == 1): #checks the condition
        prime.append(i)  # If 'i' is prime, add it to the 'prime' list

#print the output
print(f"Original list: {python_list}")
print(f"Prime numbers found: {prime}")
length=len(prime) #count the prime numbers

print("Prime number's count: ", length) #print the count



print("3. Find and count the Happy Numbers from the python list Program")
def is_happy(n): #define the function to find the number is happy or not
    """
    A happy number is a number which eventually reaches 1 when replaced
    by the sum of the square of its digits repeatedly. If the process
    loops endlessly in a cycle that does not include 1, then the number
    is not a happy number.
    """
    seen = set()  # Initialize an empty set to keep track of numbers encountered

    while n != 1 and n not in seen:
        # Continue the process as long as the number is not 1
        # and we haven't seen this number before (to avoid infinite loops).

        seen.add(n)  # Add the current number to the 'seen' set.

        sum_of_squares = 0  # Initialize a variable to store the sum of squared digits.

        for digit in str(n):
            # Convert the number to a string to iterate through its digits.
            sum_of_squares += int(digit) ** 2  # Convert each digit to an integer, square it, and add it to the sum.

        n = sum_of_squares  # Update 'n' with sum of squared digits.
    return n == 1  # If the loop ends and 'n' is 1, the original number is happy.
                   # Otherwise (if 'n' is in 'seen' and not 1), it's not happy.

python_list = [10, 501, 22, 37, 100, 999, 87, 351] #input list is given

happy_numbers_count = 0  # Initialize a counter for the number of happy numbers found.

happy_numbers = []  # Initialize an empty list to store the happy numbers.

# Iterate through each number in the python_list.
for num in python_list:

    # Call the 'is_happy' function to check if the current number is happy.
    if is_happy(num):

        happy_numbers_count += 1  # If it's a happy number, increment the counter.
        happy_numbers.append(num)  # Add the happy number to the 'happy_numbers' list.

# Print the results.
print(f"Original list: {python_list}")
print(f"Happy numbers in the list: {happy_numbers}")
print(f"Count of happy numbers: {happy_numbers_count}")


print("4. Sum of first and last digit of an integer program:")
print( "Please Enter an integer number: ")

number = int(input())#get integer input from the user

# We are type casting it in string, since we need to use the index
number = str(number)

# Storing first and last digit in a variable
first_digit = int(number[0])#first digit is getting by index of 0
last_digit = int(number[-1])#last digit is getting by negative index value of -1

# Adding these two variables
addition = first_digit + last_digit

# Display our output
print('Addition of first and last digit of the number is',
	addition)


print("5. Ways to make Rs.10 using Rs.1, Rs.2,Rs.5 and Rs 10 coin in python Program")
def find_ways_to_make_amount(amount, coins):
    """
    Finds all the possible combinations of coins to make a given amount.
    amount: The target amount (10)
    coins: A list of available coin denominations (1,2,5 and 10)
    """

    ways = [] # List to store all the valid combinations of coins.

    def find_combinations(target, current_combination, index):
        """
        Recursive helper function to find coin combinations.
        target: The remaining amount to make.
        current_combination: The list of coins used in the current combination.
        index: The index of the coin to consider in the 'coins' list.
        """
        if target == 0:
            ways.append(current_combination[:])  # Add a copy of the combination if the condition met
            return

        # If the target is negative or no more coins are available
        if target < 0 or index >= len(coins):
            return

        # Include the current coin (coins[index]) zero or more times
        for i in range(target // coins[index] + 1):
            # Create a new combination by including the current coin 'i' times.
            new_combination = current_combination + [coins[index]] * i

            # Recursively find combinations with the reduced target and next coin.
            find_combinations(target - coins[index] * i, new_combination, index + 1)

    # Sort the coins to potentially optimize and for consistent output (optional)
    coins.sort() #sort the coin

    # Start finding combinations with the given amount and an empty combination
    find_combinations(amount, [], 0)

    # Return the list of all valid combinations
    return ways

target_amount = 10 #targetted amount is declared
available_coins = [1, 2, 5, 10] #list of coins

#function call
combinations = find_ways_to_make_amount(target_amount, available_coins)

#display the result
print(f"All the ways to make Rs.{target_amount} using coins {available_coins}:")
for way in combinations:
    print(way)

print(f"\nTotal number of ways: {len(combinations)}") #print the total number of way to make Rs.10



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
def firstNonRepeating_element(arr, n): #function to find the first non repeating element
    # Loop for checking each element
    for i in range(n):
        j = 0 # Initialize a variable to track comparisons.
        # Checking if ith element is present in array
        while (j < n):
            if (i != j and arr[i] == arr[j]): # Break if the element is found at a different index.
                break
            j += 1
        # if ith element is not present in array
        # except at ith index then return element
        if (j == n):
            return arr[i]

    # If no non-repeating element is found, return -1.
    return -1

arr = [9, 4, 9, 6, 7, 4] # List of integers
n = len(arr) #length of integer list
print("First non-repeating elements in the list [9, 4, 9, 6, 7, 4] is: ")
print(firstNonRepeating_element(arr, n))  #function call



print("8. Find the minimum element of sorted and rated list program")
def findmin(arr):
    res = arr[0] # Initialize the result with the first element of the list.

    # Iterate through the list starting from the second element.
    for i in range(1, len(arr)):
        res = min(res, arr[i]) # Compare and update 'res' with the smaller value
    return res # Return the smallest number

arr = [5, 6, 8, 2, 3, 4] #list
sorted_arr = sorted(arr)  # Sorting the array in ascending order
print("Sorted List is:", sorted_arr)
print("Minimum element of sorted and rated list is:") # Display message.
print(findmin(arr)) #function call



print("9. Find the Triplets from the list [10, 20, 30, 9] with the value=59")
# Function to find three numbers in a list that sum up to a target value.
def find_triplets(numbers, target_sum):
    # Iterate through the list using three nested loops.
    # i: The first number's index.

    for i in range(len(numbers)):

        # j: The second number's index, starts after i to avoid duplicate combinations.
        for j in range(i + 1, len(numbers)):

            # k: The third number's index, starts after j

            for k in range(j + 1, len(numbers)):

                # Check if the sum of the three numbers equals the target.
                if numbers[i] + numbers[j] + numbers[k] == target_sum:

                    # Return the triplet if the condition is satisfied.
                    return [numbers[i], numbers[j], numbers[k]]

    # If no triplet matches the target sum, return an empty list
    return []

numbers = [10, 20, 30, 9] # List of numbers to search in.
target_sum = 59 # Target sum to find among triplets.

# Call the function and store the result.
result = find_triplets(numbers, target_sum)

# Display the result to the user.
if result:
    print("Triplets:", result)
else:
    print("No triplet found")



print("10. Create Sublist with sum=0 from the list [4, 2, -3, 1, 6]")
def find_sublist_with_zero_sum(numbers):
    # Dictionary to store cumulative sums and their corresponding indices.
    cumulative_sums = {0: -1} # Initialize with sum 0 to handle zero-sum sublists starting at index 0.

    current_sum = 0 # Tracks the cumulative sum while iterating.

    # Iterate through the list, tracking the index and current number.
    for i, number in enumerate(numbers):
        current_sum += number # Update the cumulative sum.

        # Check if the current cumulative sum has been seen before
        if current_sum in cumulative_sums:
            # Return the indices that form the zero-sum sublist
            return cumulative_sums[current_sum] + 1, i

        # Store the cumulative sum with its current index.
        cumulative_sums[current_sum] = i

        # Return None if no zero-sum sublist is found.
    return None

def main():
    numbers = [4, 2, -3, 1, 6] #input list

    # Call the function
    result = find_sublist_with_zero_sum(numbers)
    if result:
        start_index, end_index = result
        # print the output
        print(f"Sublist with sum 0 found between indices {start_index} and {end_index}: {numbers[start_index:end_index + 1]}")
    else:
        # print the output
        print("No sublist with sum 0 found.")

main() #call the main function
