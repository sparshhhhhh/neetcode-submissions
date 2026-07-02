class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        for i, val in enumerate(temperatures):
            while st and val > st[-1][1]:
                stInd, stT = st.pop()
                res[stInd] = i - stInd
            st.append((i, val))
        return res