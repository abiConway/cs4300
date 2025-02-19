import os, re, pytest

# Count the words in a file
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            cleaned_text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation with regex library
            words = cleaned_text.split()
            word_count = len(words)
            print(f"{filename}: {word_count} words") 
            return word_count
    except FileNotFoundError:
        return "File not found"

# Dynamically generate pytest test functions
def generate_test_function(filename, expected_word_count):
    def test_function():
        assert count_words_in_file(filename) == expected_word_count
    return test_function

#ADD any other files here!
# List of text files and their expected word counts
test_files = [
    ("task6_read_me.txt", 104), 
]

# Dynamically add test functions to the current module
for filename, expected_word_count in test_files:
    test_name = f"test_{os.path.splitext(filename)[0]}"
    test_func = generate_test_function(filename, expected_word_count)
    setattr(pytest, test_name, test_func) #Where we actually dynamically add new function



if __name__ == "__main__":
    count_words_in_file("task6_read_me.txt")
    pytest.main([__file__])