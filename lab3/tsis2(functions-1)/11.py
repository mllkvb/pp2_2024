def isPalindrome(string):
    if(string ==string[::-1]):
        return "yea"
    else:
        return "no"
string =input()
print(isPalindrome(string))