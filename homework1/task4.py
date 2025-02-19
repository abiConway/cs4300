import pytest

#Calculate total price given a price and the percent it will be discounted
#integer and float are valid inputs
def calculate_discount_price(price, discount_percent):

    #check that inputs are either integer or float
    if not isinstance(price, (int, float)):
        result = "Price must be a number"
    if not isinstance(discount_percent, (int, float)):
        result = "Percent dicount must be a number"
    else:

        #turn percent discount to decimal, calculate dollar amount of discont, calculate final price, format to 2 decimal points
        #could do all this in one line, but easier to read this way 
        discount_decimal = discount_percent / 100   
        discount = price * discount_decimal        
        final_price = price - discount
        final_price_formatted = round(final_price, 2)

    print("%.2f" % final_price_formatted)
    return final_price_formatted
    

#Test function with both integers and floats
#use this decorator to test a function multiple times with different inputs
@pytest.mark.parametrize("price, discount, expected_output",[
    (100, 10, 90.00), 
    (98.99, 5.5, 93.55),
])
#Pass the parameter pairs to the test
def test_calculate_discount_price(price, discount, expected_output): 
    assert calculate_discount_price(price, discount) == expected_output


#Run function and test
#change function arguments here if you want
if __name__=="__main__":
    calculate_discount_price(100, 10)
    pytest.main([__file__]) #make sure to pass the current file upon execution

