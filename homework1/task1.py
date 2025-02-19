import pytest

#Function to print "Hello World"
def hello_world():
    print ("Hello, World!") 


#Function to test helloWorld()
# capsys is a way to capture stdout/stderr output - see below links for help
# https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html#captures
# https://docs.pytest.org/en/stable/reference/reference.html#pytest.capture.capsys 
def test_hello_world(capsys):
    #call function       
    hello_world()
    
    #store output in captured as namedtuple - out and err (we want out, that should be "Hello, World!")
    captured = capsys.readouterr()

    #Test if the standard output of helloWorld is right
    assert captured.out == "Hello, World!\n"

    
# run helloworld and pytest of helloworld on file execution
if __name__=="__main__":
    hello_world()
    pytest.main([__file__]) #make sure to pass the current file upon execution

