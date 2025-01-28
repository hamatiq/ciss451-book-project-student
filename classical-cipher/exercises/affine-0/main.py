#greatest common divisor
def pd(n):
    pds =[]
    divisor = 2
    while n >1:
        if n % divisor == 0:
            pds.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    return pds
#euler's totient function
def phi(n):
    if n == 1:
        return 1
    pds = pd(n)
    result = n
    for p in pds:
        result *= (1 - 1 / p)
    return int(result)

#user input 
# number = int (input("Enter a number: "))
# prime_fac = pd(number)
# print (f"Prime factors of {number} are: {prime_fac}")
# result = phi(number)
# print (f"ɸ({result})")

# ɸ(26)∙26 = 312
proof = phi(26) * 26
print (proof)
result = phi (52)
print (52*result)