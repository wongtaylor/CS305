# type of caching mechanism that decorates function fibo with caching function

def caching(f):                       
    def wrapper(x):                     
        try:
            return wrapper.cache[x]
        except:
            wrapper.cache[x] = f(x)
            return wrapper.cache[x]
    wrapper.cache = {}
    return wrapper

@caching
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
  
  
# testing code
print(fibo(10))
prnt(fibo(1000))
