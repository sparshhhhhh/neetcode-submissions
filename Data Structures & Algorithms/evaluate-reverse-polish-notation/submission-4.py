class Solution:
    def calc(self, a, b, i):
        if i == "+":
            return a+b
        elif i == "-":
            return b-a
        elif i == "*":
            return a*b
        else:
            return int(b/a)

    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ["+", "-", "*", "/"]
        for i in tokens:
            print(i, st)
            if i in op:
                a = st.pop()
                b = st.pop()
                r = self.calc(int(a), int(b), i)
                st.append(r)
            else:
                st.append(i)
        return int(st[-1])