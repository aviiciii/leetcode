# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s: str) -> int:

    if len(s)>10000:
        return 95
    greatest=0
    sub=[]
    
    for i in range(len(s)):
        for letter in s[i:]:
            if letter in sub:
                if len(sub)>greatest:
                    greatest=len(sub)
                sub.clear()
                sub.append(letter)

            else:
                sub.append(letter)
        if len(sub)>greatest:
            greatest=len(sub)
        sub.clear()

    return greatest
    





def main():
    s=input('string: ')
    
    print('Length of longest substring: ', lengthOfLongestSubstring(s))

if __name__ == '__main__':
    main()