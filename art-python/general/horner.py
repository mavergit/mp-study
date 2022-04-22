# returns value of poly[0]+ poly[1]x + .. + poly[n]*x^n
def horner(poly, n, x):
    result = poly[n-1]
    # Horner's method
    for i in range(1, n):    
        result = result*x + poly[n-i-1]
    return result

coeffs = [int(item) for item in input('Enter polynomial coefficients starting with zeroth power and separated by space: ').split()]

print(coeffs)
n = len(coeffs)
print('number of coefficients: ', n)

x =int(input('argument for evaluation: '))
print('x =',x)

print('Value of polynomial at x =',x,' is ' , horner(coeffs, n, x))


