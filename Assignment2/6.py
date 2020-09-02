def palindro(str):
    if(str==str[::-1]):
        print("The string {} is palindrome".format(str))
    else:
        print("Not palindrome")

str="naman"
palindro(str)