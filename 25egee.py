# from fnmatch import*
#
# def f(n):
#     imin = 100000
#     if n**0.5 == int(n ** 0.5):
#         for i in range(2, 100):
#             if (n % i ) == 0:
#                 imin  = i
#                 return n / imin
#                 break
#     return 0
# for i in range(1, 10000000):
#     if fnmatch(str(i), '3*52?') and f(i) != 0:
#         print(i, f(i))
#
# for i in range(100000):
#     i = i*i
#     if fnmatch(str(i), '4*1?009'):
#         print(i, i**0.5)
# def div(n):
#     d = set()
#     for i in range(1, int(n**0.5)+1):
#         if n % i ==0:
#             if i % 2 ==0:
#                 d.add(i)
#             if (n//i)% 2 == 0:
#                 d.add(n //i)
#     return len(d), sum(d)
#
# for i in range(65000, 1000000):
#     l , c = div(i)
#     if fnmatch(str(i), '6*97*5?') and l >= 4:
#             print(i, c)
#
# for i in range(40_130_000, 10**12, 4013):
#     if fnmatch(str(i), '123?4*5679'):
#         print(i, i // 4013)
# def f(n):
#     d= set()
#     for i in range(1, int(n **0.5) +1):
#         if n % i == 0:
#             d.add(i)
#             d.add(n // i)
#     return len(d)
#
# def stepen(n):
#    if  n > 0 and  (n & (n - 1)) == 0:
#        return 1
#
# for i in range(2031*31, 10**9, 2031*31):
#     if fnmatch(str(i), '*31*65?') and stepen(f(i)):
#         print(i, i //2031)
#
# def s(n):
#     suma = 0
#     while(n > 0):
#         suma+=n %10
#         n //=10
#     return suma
# for i in range(0, 10**10, 2023):
#     if fnmatch(str(i), '1?1?1?1*1') and s(i) == 22:
#         print(i)
# def f(n):
#     d = set()
#     for i in range(1, int(n**0.5)+1):
#         if n % i ==0:
#             d.add(i)
#             d.add(n // i)
#     return len(d), sum(d)
#
# for i in range(53, 10**7, 53):
#     l, c = f(i)
#     if fnmatch(str(i), '*2?2*') and (str(i) == str(i)[::-1]) and l >30:
#         print(i, c)
#
#
# def erat(N):
#     primes = [i for i in range(N + 1)]
#     i = 2
#     while i <= N:
#         if primes[i] != 0:
#             j = i + i
#             while j <= N:
#                 primes[j] = 0
#                 j = j + i
#         i += 1
#     primes = [i for i in primes if i != 0]
#     return primes
#
# def is_prime(x):
#     for d in range(2, int(x**0.5) +1):
#         if x % d == 0:
#             return 0
#     return 1
# def f(n):
#     d = set()
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             d.add(i)
#             d.add(n //i)
#     return [x for x in d if is_prime(x) != 0]
# for i in range(9, 10**7, 10):
#     if fnmatch(str(i), '34?8*9'):
#         a = f(i)
#         if len(a) >4:
#             print(i, max(a))
# def f(n):
#     suma = 0
#     ss = 0
#     while (n >0):
#         if (n % 10 ):
#             ss += n % 10
#             if  (n%10)% 2 == 1:
#                 suma += n % 10
#         n //= 10
#     return ss, suma
# for i in range(10**8):
#     s, sn = f(i)
#     if fnmatch(str(i), '124*5*79') and i % sn== 0:
#         print(i, s)
# def f(n):
#     d = set()
#     for i in range(1, int(n **0.5)+1):
#         if n % i == 0:
#             d.add(i)
#             d.add(n // i)
#     return d
# for i in range(10**7):
#     if fnmatch(str(i), '9?*55*7'):
#         print(i, sum(f(i)) % 21)
