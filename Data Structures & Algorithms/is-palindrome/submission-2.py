class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        print(s)
        i = 0
        j = len(s)-1
        while i < j:
            print(i,j)
            while i<j and not s[i].isalnum():
                i+=1
                break
            while i<j and not s[j].isalnum():
                j-=1
                break
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True