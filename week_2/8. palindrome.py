from pydoc import ispackage


input = "abcba"


def is_palindrome(string):
    end = len(string) - 1
    for start in range(len(string) // 2):
        if string[start] != string[end]:
            return False
        end -= 1
    return True


print(is_palindrome(input))
print(is_palindrome('aaaa'))
print(is_palindrome('isassasi'))