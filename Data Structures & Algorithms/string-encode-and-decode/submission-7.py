class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))
            res += '/:'
            res += i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = ''
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                l+=s[i]
                i+=1
            elif s[i] == '/' and i+1 < len(s) and s[i+1] == ':':
                i+=2
                res.append(s[i:i+int(l)]) 
                i += int(l)
                l = ''
            else:
                i+=1
        return res