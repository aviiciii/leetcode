# https://leetcode.com/problems/palindrome-number/

# find if number is palindrome  or not
def isPalindrome(x: int) -> bool:
    temp = x
    rev = 0
    while(x > 0):
        dig = x % 10
        rev = rev * 10 + dig
        x = x // 10
    if(temp == rev):
        return True
    else:
        return False

def main():
    num = int(input("Enter a number: "))
    print(isPalindrome(num))

if __name__ == '__main__':
    main()