def caching_fibonacci():
    cashe = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1 
        
        if n in cashe:
            return cashe[n]

        cashe[n] = fibonacci(n - 1) + fibonacci (n-2)
        return cashe[n]
    return fibonacci
    
fib = caching_fibonacci()


print(fib(10))  
print(fib(20)) 



