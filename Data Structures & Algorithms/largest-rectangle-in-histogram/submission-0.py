class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = []
        for i, val in enumerate(heights):
            start = i
            while st and st[-1][1] > val:
                index, height = st.pop()
                res = max(res, height*(i-index))
                start = index
            st.append((start, val))

        for i, h in st:
            res = max(res, h*(len(heights) - i))

        return res