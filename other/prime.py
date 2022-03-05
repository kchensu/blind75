def prime(n):
    primes = []
    is_prime = [0, 0] + [1]*(n-1)
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = 0
    return primes


print(prime(18))
