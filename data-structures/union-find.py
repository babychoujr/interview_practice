class DSU(object):

    def __init__(self):
        # saving par 
        self.par = range(1001)
        
        # stores rank
        self.rank = [0] * 1001
    
    # keep looking for the parent until you find X
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    # union 
    def union(self, x, y):
        # find the roots of both x and y
        xr, yr = self.find(x), self.find(y)

        # if both roots are the same parent
        if xr == yr:
            return False
        # if both roots are different, check the ranking (ranking holds how many values are inside of the component)
        # if root of x is smaller than y, than replace the parent of x with y
        elif self.rank[xr] < self.rank[yr]:
            self.par[x] = yr
        
        # if root of y is smaller than x, than replace the parent of y with x
        elif self.rank[xr] > self.rank[yr]:
            self.par[y] = xr
        # if equals, this could be either way but replace parent of root of y with xr, and add one rank to the root of xr
        else:
            self.par[yr] = xr
            self.rank[xr] += 1
        
        return True