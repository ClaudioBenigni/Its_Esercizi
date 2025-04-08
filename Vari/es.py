def prime_factors(n: int) -> list[int]:
    fattori = []
    divisore = 2
    
    while n > 1:
    
        if n % divisore == 0:
            fattori.append(divisore)
            n //= divisore
    
        else:
            divisore += 1
    
    return fattori

print(prime_factors(120))
