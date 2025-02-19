import pytest


# Used ChatGPT for this https://chatgpt.com/share/67b533ef-bfec-8007-b80a-46014b0381e1 
#Function 1
#Simply check if a number is less than or greater than 0, oherwise it is zero. 
#Make suer the argument passed is the correct data type
def is_neg_pos_zero(number):
    #check that number is either a valid data type
    if not isinstance(number, (int, float)):
        result = "Input must be a number"
    else:
        if number < 0:
            result = "Number is negative"
        elif number > 0:
            result = "Number is positive"
        else:
            result = "Number is zero"
    print(result)
    return result

#Function 2
# Find the first 10 prime numbers 
# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/ 
def print_ten_prime_numbers():
    result = []
    num =  2
    while len(result) < 10:
        is_prime = True

        # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
            # If num is divisible by any number between 2 and n / 2, it is not prime
            if (num % i) == 0:
                is_prime = False
        if is_prime:
            result.append(num)
        num += 1
    print(*result) #use * operater to print without parenthesis and commas


#Function 3
#Loop through 1-100, adding each number to total
def sum_one_to_hundred():
    sum = 0
    num = 1
    while num <= 100:
        sum += num
        num += 1
    print(sum)
    return sum  #good to return sum, then don't have to test the standard output


#Test 1
#use this decorator to test a function multiple times with different inputs
#https://www.google.com/search?q=test+multiple+inputs+in+pytest&oq=test+multiple+inputs+in+pytest&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRifBTIHCAYQIRifBTIHCAcQIRifBTIHCAgQIRifBTIHCAkQIRifBdIBCTEwMTA4ajBqOagCALACAQ&sourceid=chrome&ie=UTF-8 
#https://pytest-with-eric.com/introduction/pytest-parameterized-tests/#:~:text=Pytest%20parameterized%20testing%20is%20a,and%20provide%20better%20test%20coverage.
@pytest.mark.parametrize("input, expected_output",[
    ("seven", "Input must be a number"),
    (1, "Number is positive"),
    (-1, "Number is negative"),
    (0, "Number is zero"),
])
#pass the parameter pairs to the test
def test_is_neg_pos_zero(input, expected_output): 
    assert is_neg_pos_zero(input) == expected_output


#Test 2
#pass the standard out/err to the test function
def test_print_ten_prime_numbers(capsys):
    #call function
    print_ten_prime_numbers()
    #store output in captured as namedtuple - out and err (we want out, that should be "Hello, World!")
    captured = capsys.readouterr()

    #Test if the standard output of helloWorld is right
    assert captured.out.strip() == "2 3 5 7 11 13 17 19 23 29"


#Test 3
#realizing I should have passed 1 and 100 as parameters to function, maybe for a later date
def test_sum_one_to_hundred():
    assert sum_one_to_hundred() == 5050

if __name__=="__main__":
    #Change the neg/pos/zero number tested here
    is_neg_pos_zero("hello")
    print_ten_prime_numbers()
    sum_one_to_hundred()
    pytest.main([__file__]) #make sure to pass the current file upon execution

    
