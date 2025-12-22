class Solution:
    def removeStars(self, s: str) -> str:
        x = 0
        while(True):
            if x == -1:
                break
            txt = s
            x = s.find("*")
            z = s[:x-1]
            s = z + s[x+1:]
        return txt