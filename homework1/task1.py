import pytest

#Function to print "Hello World"
def helloWorld():
    print ("Hello, World!") 

#Function to test helloWorld()
# capsys is a way to capture stdout/stderr output - see below links for help
# https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html#captures
# https://docs.pytest.org/en/stable/reference/reference.html#pytest.capture.capsys 
def test_helloWorld(capsys):
    #call function       
    helloWorld()
    
    #store output in captured as namedtuple - out and err (we want out, that should be "Hello, World!")
    captured = capsys.readouterr()

    #Test if the standard output of helloWorld is right
    assert captured.out == "Hello, World!\n"

    
# run helloworld and pytest of helloworld on file execution
# Typicall best practice is to put this in a seperate test module ("pytest" will run
# all test_*.py or *_test.py files in the directory or subdirectory) but this will 
# keep everything organized for grading purposes
if __name__=="__main__":
    helloWorld()
    pytest.main([__file__])

