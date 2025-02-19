import pytest
    
#create list of favorite books
favorite_books = [ 
        ("A Wise Man's Fear" , "Patrick Rothfuss"),
        ("Ishmael" , "Daniel Quinn"),
        ("Mouse Tales", "Arnold Lobel"),
        ("Red Rising", "Pierce Brown")
        ]

#Print the first 3 by slicking
def print_fav_books():
    for title, author in favorite_books[:3]:
        print(f"{title} by {author}")


#create a student database dictionary with names and sudent IDs
students = {
    "Name1" : 1234,
    "Name2" : 2345,
    "Name3" : 3456,
}

#Test favorite books printed right
def test_print_fav_books(capsys):
    print_fav_books()
    captured = capsys.readouterr()
    assert captured.out == (
        "A Wise Man's Fear by Patrick Rothfuss\n"
        "Ishmael by Daniel Quinn\n"
        "Mouse Tales by Arnold Lobel\n"
        )
    
#Test favorite books was a list
def test_list():
    assert isinstance(favorite_books, list)

#Test students was a dictionary
def test_dictionary():
    assert isinstance(students, dict)


if __name__=="__main__":
    print_fav_books()
    pytest.main([__file__]) #make sure to pass the current file upon execution

