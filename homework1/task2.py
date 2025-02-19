import pytest

#I wanted simple, so here is a function that prints and returns key value pairs of each data type
def data_types():
    data = {
        "integer": 1,
        "float": 1.5,
        "string": "Test string",
        "boolean": True,
    }

    for key, value in data.items():
        print(f"{key}: {value}")
    
    return data


#Test goes through each key value pair, and isinstance tests the data type in each
def test_dataTypes():
    test_data = data_types()

    # isinstance compares to data type
    assert isinstance(test_data["integer"], int)
    assert isinstance(test_data["float"], float)
    assert isinstance(test_data["string"], str)
    assert isinstance(test_data["boolean"], bool)

    
#Run the function and the test
if __name__ == "__main__":
    data_types()
    pytest.main([__file__])