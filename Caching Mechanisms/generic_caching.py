# Generic Caching mechanism

# function object
def caching(f):                      
    cache = {}
    def wrapper(n):                  
        try:
            return cache[n]
        except:
            cache[n] = f(n)
            return cache[n]
    return wrapper


# recursive function object
def fibo(n):                        
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
    
print(id(fibo))                     # print id of old fibo
fibo = caching(fibo)                # fibo --> caching(fibo) - no longer points to original fibo object
print(id(fibo))                     # print id of new fibo

from math import cos
cos = caching(cos)

for i in range(1000):
    fibo(i)
print(fibo(1010))    

print("\n")

for i in range(100):
    cos(i)
print(cos(100))
