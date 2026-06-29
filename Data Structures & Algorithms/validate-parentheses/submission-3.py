class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in ["(", "[", "{"]:
                st.append(i)
            elif i == ")":
                if len(st) != 0:
                    j = st.pop()
                    if j != "(":
                        return False
                else:
                    return False
            elif i == "]":
                if len(st) != 0:
                    j = st.pop()
                    if j != "[":
                        return False
                else:
                    return False
            elif i == "}":
                if len(st) != 0:
                    j = st.pop()
                    if j != "{":
                        return False
                else:
                    return False
        if len(st):
            return False
        return True