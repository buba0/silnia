def silnia(n):
    if n == 1:
        return 1
    else:
        return  n * silnia(n-1)\
            
n = int(input("Numer:\n#>"))
print(silnia(n))