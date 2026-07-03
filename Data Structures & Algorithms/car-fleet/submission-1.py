class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        for p, s in pair:
            t = (target - p) / s
            st.append(t)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)