# fo = 0
# f1 = 1
# f2 = f0 + f1
# fn = f(n-1) + f(n-2)




def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib = fibonacci(int(input("Enter any number: ")))
print(fib)
