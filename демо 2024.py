# номер 5 перестановки чисел
# for n in range(1, 100):
#     r = bin(n)[2::]
#     if (n % 3) == 0:
#         r += r[-3::]
#     else:
#         r = r + bin(n % 3 * 3)[2::]
#         m = int(r, 2)
#     if(m < 166 and m > 151):
#         print(r, m, n)
# def tr(n):
#     s = ''
#     while(n >0 ):
#         s = str(n % 3 )+ s
#         n //=3
#     return s
# for n in range (1, 1000):
#     r = tr(n)
#     if (n % 3 ) == 0:
#         r += r[-2::]
#     else:
#         r+= tr((n%3 ) * 5)
#     m = int(r, 3)
#     if(m > 133 ):
#         print(n , m)
# номер 8. комбинаторика
# from itertools import*
# k =0
# for x in permutations ('0234567', r = 5):
#     s = ''.join(x)
#     if (s[0] != '0'):
#         s = s.replace('2', '0').replace('4', '0'). replace ('6', '0')
#         s = s.replace('3', '1').replace('5', '1').replace('7', '1')
#         if ('00' not in s and '11' not in s):
#             k+=1
# print(k)
#  nomer 12
# res = set()
# for n in range(10, 1000):
#  s = '5' + '2'*n
#  while '52' in s or '2222' in s or '1122' in s:
#    if '52' in s:
#     s = s.replace('52', '11', 1)
#    if '2222' in s:
#     s = s.replace('2222', '5', 1)
#    if '1122' in s:
#     s = s.replace('1122', '25', 1)
#  if sum(map(int, s)) == 64 :
#     print(n)
# номер 13 маска сети . перевести все 10е числа в двоичные
# print(bin(192), bin(168), bin(32), bin (160), bin(240))
#  номер 14 вставление букв

# for x in('123456789abcdefghi'):
#     a = int(f'98897{x}21', 19 ) + int(f'2{x}923', 19)
#     if a % 18 == 0:
#         print(x, a //18)

# номер 15  логика
# def f(x, y):
#     return ((x+2*y)< a) or (y > x) or (x > 60)
#
# for a in range (200):
#     if all(f(x, y) == 1 for x in range(200) for y in range(200)):
#         print(a)
# for x in ('0123456789abcdefghi'):
#     a = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
#     if (a % 18 == 0):
#         print(x, a//18)

# for n in range(1, 200):
#     s = '5' + '2'*n
#     while"52" in s or "2222" in s or "1122" in s:
#         if "52" in s:
#             s = s.replace("52", "11", 1)
#         if "2222" in s:
#             s = s.replace("2222", "5", 1)
#         if "1122" in s:
#             s = s.replace("1122", "25", 1)
#     if sum(map(int, s)) == 64:
#         print(n, s)
# n = []
# N = []
# for x in range (10):
#     for y in range(1000):
#         a = int(f'1{x}2157{y}4')
#         if a% 2024 == 0:
#             n.append(a)
#             N.append( a //2024)
#             N.sort()
#             n.sort()
# print(n , N)
#5
# a = set()
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     r+= bin(n%3)[2:].zfill(2)
#     r+= bin(int(r , 2)%5)[2:].zfill(3)
#     if 1_111_111_10 <= int(r, 2) <= 1_444_444_416:
#         a.add(int(r, 2))
# print(len(a))
# def tr(n):
#     s = ''
#     while(n>0):
#         s = str(n % 3 ) + s
#         n = n //3
#     return s
# for n in range(0, 100):
#     r = bin(n)[2:]
#     if(r.count('1')%  2 == 0 ):
#         r = r +'0'
#     else:
#         r = r + '1'
#     if (r.count('1') % 2 == 0):
#         r = r + '0'
#     else:
#         r = r + '1'
#     if(int(r, 2) > 81):
#         print(n, tr(n), int(r, 2))
# for x in ('0123456789abcdefg'):
#     a = int(f'51{x}49', 17) + int(f'2{x}041', 17)
#     if (a % 11 == 0):
#         print(x, a//11)


# for x in range(16, 0, -1):
#     n1 = 5 * 17**4 + 1 * 17**3 + x*17**2 + 4 * 17 + 9
#     n2 = 2 * 17**4 + x * 17**3 + 0 * 17**2 + 4 * 17 + 1
#     if (n1+n2) % 11 == 0:
#         print((n1+n2) // 11)
#         break
# for i in range(1000000):
#     s = bin(i)[2:]
#     s += str(s.count('1') % 2)
#     s += str(s.count('1') % 2)
#     if int(s, 2) > 81:
#         print(int(s, 2), i)
#         break
# a = []
# N = int(input())
# cnt = 0
# primes = [i for i in range(N + 1)]
# primes[1] = 0
# i = 2
# while i <= N:
#     if primes[i] != 0:
#         j = i + i
#         while j <= N:
#             primes[j] = 0
#             j = j + i
#     i += 1
# primes = [i for i in primes if i != 0]
# for i in range ( len(primes) - 3):
#     if(primes[i+1] == primes[i] + 4) or primes[i+2] == primes[i]+4 or primes[i+3] == primes[i]+4:
#         cnt+=1
# print(cnt)

# a = [0] * 101
# a[1] = 1
# for i in range(2, 101):
#     if i % 3 == 0:
#         a[i] += a[i // 3]
#     a[i] += a[i - 4]
#     a[i] += a[i - 1]
# print(a[100])
# def tr(n):
#     s = ''
#     while(n>0):
#         s = str(n % 3 ) + s
#         n = n //3
#     return s
# def su(n):
#     s = 0
#     while(n>0):
#         s += n % 3
#         n = n //3
#     return s
# for n in range(100):
#     r = tr(n)
#     if(n % 2 == 0):
#         r = '1'+r+'00'
#     else:
#         r = r + str(tr(su(n)))
#     if(int(r, 3) > 168):
#         print(int(r, 3), n)
# def f(n):
#     if(n < 10):
#         return n
#     if(n >= 10):
#         return (n % 10)+ (8 * f(n//10))
# print(f(10**30))
# s = ''
# s = '>' + 26*'1' + 10*'2' + 14*'3'
# while '>1' in s or '>2' in s or '>3' in s:
#     if ">1" in s:
#         s = s.replace('>1', '22>', 1)
#     if ">2" in s:
#         s = s.replace('>2', '2>', 1)
#     if ">3" in s:
#         s = s.replace('>3', '1>', 1)
# print(s, s.count('2'), s. count('1'))
# a = open("24_21.txt").readline()
# cnt = 0
# rec = 0
# for i in range(1, len(a)):
#    if(a[i] != a[i-1]):
#        cnt+=1
#        if cnt> rec:
#            rec = cnt
#    else: cnt = 1
# print(rec)
# a = open(r"C:\Users\Анна\OneDrive\Документы\DEV EGE IT\lalala.txt").readline()
# cnt = 0
# rec = 0
# for i in range(1, len(a)):
#    if(a[i] != a[i-1]):
#        cnt+=1
#        if cnt> rec:
#            rec = cnt
#    else: cnt = 1
# print(rec)
# def f(n):
#     for i in range(1, n):
#         if(n % i == 0 and i % 10 == 9 and i != n and i != 9):
#             return i
# for i in range(600_000, 600100):
#     if(f(i)):
#         print(i , f(i))
# def f(n):
#     cnt = 0
#     while n!= 0:
#         c = n%5
#         if(c == 0):
#             cnt+= 1
#         n //= 5
#     return cnt
# for x in range(1, 100):
#     a = 4*625**1920+4*125**x-4*25**1940-3*5**1950-1960
#     if(f(a) == 1891):
#         print(x)
# 5



