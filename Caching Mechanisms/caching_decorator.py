# Type of Caching Mechanism that uses a decorator class

# decorator class
class Caching:                      
    def __init__(self, f):
        self._f = f
        self.cache = {}
    
    def __call__(self, x):
        try:
            return self.cache[x]
        except:
            self.cache[x] = self._f(x)
            return self.cache[x]
            
@Caching
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# testing code
print(fibo(10))
print(fibo(100))


