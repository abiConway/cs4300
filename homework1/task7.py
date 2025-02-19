import requests
import pytest

# Get the HTTP status code of a URL
def get_status_code(url):
    response = requests.get(url)
    print(f"The status code for {url} is: {response.status_code}")
    return response.status_code

# Pytest test cases
def test_get_status_code():  # Corrected function name
    assert get_status_code("https://www.google.com") == 200

if __name__ == "__main__":
    get_status_code("https://canvas.uccs.edu/")  
    pytest.main([__file__])
