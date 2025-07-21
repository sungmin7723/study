def is_prime(n) -> bool:
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1 ):
            if n % i == 0:
                return False
    return True

F, S = map(int, input().split())
for i in range(F, S + 1):
    if is_prime(i):
        print(i)