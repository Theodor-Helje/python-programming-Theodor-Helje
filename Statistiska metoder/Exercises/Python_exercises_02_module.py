def congruent(a: int, b: int, p: int) -> bool:
    return a % p == b % p

def divisor(a: int, b: int) -> bool:
    return b % a == 0

def prime(a) -> bool:
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True


def test_congruence():
    a = congruent(5,2,3)
    b = not congruent(1,4,2)
    return a and b

def test_divisor():
    a = divisor(2,12)
    b = not divisor(5,7)
    return a and b

def test_prime():
    a = prime(37)
    b = not prime(8)
    return a and b


if __name__ == '__main__':
    print(f"Congruence test: {test_congruence()}")
    print(f"Divisor test: {test_divisor()}")
    print(f"Prime test: {test_prime()}")