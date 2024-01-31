# def f(x, y, z, w):
#     return y and (x or z) or not(y or z) or w
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not f(x, y, z, w):
#                     print(x, y, z, w)

# for n in range(1000):
#     r = bin(n)[2:]
#     if n % 2 ==0:
#         r += r[-2:]
#     else:
#         r = '1' + r + '0'
#     if int(r, 2) < 100:
#         print(n, r)

# ans = []
# for x in range(3, 10000):
#     s = '3'+'5'*x
#     while "333" in s or "555" in s:
#         if "555" in s :
#             s = s.replace("555", "3", 1)
#         else:
#             s=s.replace("333", "5", 1)
#     a = sum(list(map(int, s)))
#     ans.append(a)
# print(max(ans))
# a = []
# x = 2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
# while x > 0:
#     a = [x % 9] + a
#     x//=9
# print(a.count(1)+a.count(2)+a.count(3)+a.count(4)+a.count(5)+a.count(6)+a.count(7)+a.count(8))

# def f(x, a):
#     return (x&a == 0) or not(x & 37 ==0) or not(x&12 == 0)
# for a in range(1, 3000):
#     if all(f(x, a) for x in range(1, 30000)):
#         print(a)

# with open(r"C:\Users\Анна\OneDrive\Рабочий стол\3\17.txt") as file:
#     a = [int(x) for x in file]
# ans = []
# m = 0
# for i in range(len(a)):
#     if (9999< a[i] < 100000) and a[i] % 10 == 3:
#         if a[i] > m:
#              m = a[i]
# for i in range(len(a) - 2):
#     if (abs(a[i]) % 10 == 3 or abs(a[i+1]) % 10 == 3 or abs(a[i+2]) % 10 == 3) and a[i]+a[i+1]+a[i+2] <= m:
#         ans.append(a[i] + a[i+1] +a[i+2])
# print(len(ans), max(ans))

# def f(s,m):
#     if s  >= 301: return m% 2 == 0
#     if m == 0:  return 0
#     h = [f(s+3, m-1), f(s*5, m-1)]
#     return any (h) if (m-1)% 2 ==0 else all(h)
# for s in range(1, 301):
#     if f(s, 2) and not f(s, 1):
#         print(s)
# for s in range(1, 301):
#     if f(s, 3) and not f(s, 1):
#         print(s)
# for s in range(1, 301):
#     if f(s, 4) and not f(s, 2):
#         print(s)

# a = [1] * 2030
# for i in range(4, 2030):
#     a[i] = (i+3)*a[i-2]
#     print(a[2028] / a[2024])

# def f(a, b):
#     if a> b or a == 16: return 0
#     if a ==b : return 1
#     return f(a+1, b)+f(a+3, b)+f(a*a, b)
# print( f(3, 20) * f(20, 26))

# s = open(r"C:\Users\Анна\OneDrive\Рабочий стол\3\24.txt").readline()
# c =''
# while c in s:
#     c+='RSQ'
# print(c in s)
# print('SQ' + c[:-1] in s)
# print('Q' + c[:-1] in s, len(c))
# print('Q' + c in s)




