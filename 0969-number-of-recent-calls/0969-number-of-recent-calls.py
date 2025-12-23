class RecentCounter:

    def __init__(self):
        self.c = deque()

    def ping(self, t: int) -> int:
        self.c.append(t)
        #return sum(1 for i in self.c if i >= t-3000 and i <= t)
        while self.c[0] < t - 3000:
            self.c.popleft()
        return len(self.c)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)