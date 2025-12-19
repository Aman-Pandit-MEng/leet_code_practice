class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = [0]*(len(gain)+1)
        for i in range(len(gain)):
            a[i+1] = a[i]+gain[i]
        return max(a)