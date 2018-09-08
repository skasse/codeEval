def isPrime(n):
    '''checks if prime'''
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i=5
    while (i*i<n):
        if n%i==0 or n%(i+2)==0:
            #print("not a prime, {0} / {1} = {2}".format(n, i, n/i))
            return False
        i+=6
    #print("{0} is a prime".format(n))
    return True

def trunc_test(x):
    if isPrime(x) and len(str(x))>1:
        print(x,"is prime")
        x=int(str(x)[1:])
        trunc_test(x)
    elif isPrime(x):
        print(x,"is prime")

longest_prime = 1
def append_int_list(n):
    '''prefixes integers, 1 thru 10, to n and returns them in a list''' 
    #return [int(str(x)+str(n)) for x in range(1,10)]
    global longest_prime
    a = [int(str(x)+str(n)) for x in range(1,10)]
    a = [x for x in a if isPrime(x)]
    if a:
        length = len(str(a[0]))
        if length>longest_prime:
            longest_prime = length
        print(a, length, longest_prime)
    return [append_int_list(x) for x in a if isPrime(x)]

print([append_int_list(x) for x in range(2,10)])
