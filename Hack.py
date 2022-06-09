from Crypto.Util.number import *
import RSAwienerHacker
import gmpy2
import Arithmetic

def WienerHacker(e, n):
    '''基于连分数的Wiener攻击'''
    d = RSAwienerHacker.hack_RSA(e, n)
    print(f"d:{d}")


def dpHacker(e, n, dp):
    '''dp泄露'''
    for x in range(1, e):
        if(dp*e - 1) % x == 0:
            if (n % ((dp * e - 1) // x + 1)) == 0:
                p = (dp * e - 1) // x + 1
                q = n//p
                r = (p-1)*(q-1)
                d = gmpy2.invert(e, r)
                print(f"d:{d}")


def IntegerFactorizationHacker(n1, n2, e1, e2):
    '''gcd去求解共同的素因子q'''
    p = gmpy2.gcd(n1, n2)
    q1 = n1 // p
    q2 = n2 // p
    r1 = (q1-1)*(p-1)
    r2 = (q2-1)*(p-1)
    d1 = gmpy2.invert(e1, r1)
    d2 = gmpy2.invert(e2, r2)
    print(f"d1:{d1}")
    print(f"d2:{d2}")


def dpAnddqHacker(dp, dq, p, q, c):
    '''dp和dq泄露'''
    m1 = gmpy2.powmod(c, dp, p)
    m2 = gmpy2.powmod(c, dq, q)
    print(f"m1:{long_to_bytes(m1)}")
    print(f"m2:{long_to_bytes(m2)}")


def LowEHacker(e, n, c):
    '''低加密指数攻击，e过于小'''
    k = 0
    while 1:
        res = gmpy2.iroot(c + k * n, e)
        if (res[1] == True):
            m = long_to_bytes(res[0])
            print(f"m:{m}")
            break
        k = k + 1

def CommonModeHacker(e1 ,e2 ,c1 ,c2 , n):
    '''共模攻击'''
    s = Arithmetic.egcd(e1 ,e2)
    s1 = s[0]
    s2 = s[1]
    if s1 < 0:
        s1 = - s1
        c1 = gmpy2.invert(c1, n)
    elif s2 < 0:
        s2 = - s2
        c2 = gmpy2.invert(c2, n)

    m = pow(c1, s1, n) * pow(c2, s2, n) % n
    print(long_to_bytes(m))


def main():
    pass

if __name__ == '__main__':
    main()