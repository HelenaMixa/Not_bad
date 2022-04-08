import time
def fun_decorator (func):
    def wrapper (*args,**kwargs):
        st=time.time()
        res=func(*args,**kwargs)
        et=time.time()
        print (f"Function running time:{func.__name__} took {str(et-st)[:6]} sec")
        return res
    return wrapper


@fun_decorator
def gcd_rem_division(num1, num2):
    print (f"GCD: {num1, num2}")
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2
    

@fun_decorator
def binary_gcd(num1, num2):
    print (f"GCD: {num1, num2}")
    shift = 0
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1
    while num1 & 1 == 0:
        num1 >>= 1
    while num2 != 0:
        while num2 & 1 == 0:
            num2 >>= 1
        if num1 > num2:
            num1, num2 = num2, num1
        num2 -= num1
    return num1 << shift

@fun_decorator
def say_hello():
    print("Hello")

#gcd_rem_division=fun_decorator(gcd_rem_division)
print ("Euclid's algorithm")
res_Eucl_alg=gcd_rem_division(15,10000000)
print(f"GCD={res_Eucl_alg}")
#binary_gcd=fun_decorator(binary_gcd)
print ("Binary Euclid algorithm")
res_Bin_Eucl_alg=binary_gcd(15,10000000)
print(f"GCD={res_Bin_Eucl_alg}")

say_hello()
