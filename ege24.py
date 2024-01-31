

# f = open(r"C:\Users\Анна\Downloads\1-3__1ncx3.txt")
# k = 0
# #a = [str(x) for x in f]
# for x in range(1000):
#     s = f.readline()
#     if s.count('K') <s.count('O'):
#         k+=1
# print(k)

# f = open(r"C:\Users\Анна\Downloads\1-3__1ncx2.txt")
# l = r = k = 0
# for i in range(1000):
#     s = f.readline()
#     if s.count('BU') > 3:
#         k+=1
# print(k)

# f = open(r"C:\Users\Анна\Downloads\4__1ncx9.txt")
# a = f.readlines()
# abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# mx = 0
# for s in a:
#     if s.count('N') > 50:
#         for i in abc:
#             r = s.rfind(i) - s.find(i)
#             mx = max(r, mx)
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\2__1tixs.txt")
# k = mx = 0
# s = f.readline()
# for i in range(len(s)):
#     if s[i] == 'F':
#         k+=1
#         if k >mx:
#             mx = k
#     else:
#         k = 0
# print(mx)
# i = 0
# while i*'F' in s:
#     i+=1
# print(i)

# f = open(r"C:\Users\Анна\Downloads\4__1tixx.txt")
# s = f.readline()
# k = mx = 2
# for i in range(len(s)-2):
#     if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
#         k +=1
#         mx = max(mx, k)
#     else:
#         k = 2
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\7__1tiy2.txt")
# s = f.readline()
# k = mx = 0
# for i in range(len(s)):
#     if s[i] == 'B' or s[i] == 'C' or s[i] == 'E':
#         k +=1
#         if k > mx:
#             mx = k
#     else:
#         k = 0
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\7__1tiy2.txt")
# s = f.readline()
# k = mx = 0
# for i in range (len(s)):
#     if s[i] == 'C':
#         k = 0
#     else:
#         k+=1
#         if k> mx:
#             mx = k
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\11__1tiye.txt")
# k = mx = 0
# for j in range(1000):
#     s=f.readline()
#     for i in range(len(s)-2):
#         if s[i] == 'K' and s[i+2] == 'N':
#             k+=1
#             break
# print(k)
# s = f.readlines()
# k = 0
# abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in s:
#     for j in abc:
#         if 'K'+j+'N' in i:
#             k+=1
#             break
# print(k)

# f = open(r"C:\Users\Анна\Downloads\24_1__1kaci.txt")
# s = f.readline()
# k = mx = 0
# for i in range(1, len(s)-1, 2):
#     if s[i] in "AO" and s[i + 1] in "CDF":
#         k += 1
#         mx = max(mx, k)
#     else:
#         k = 0
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\15__1tiyo (1).txt")
# s = f.readline()
# k = mx = 0
# for i in range(1, len(s)-1, 2):
#     if s[i] in "BCDF" and s[i + 1] in "AE":
#         k += 1
#         mx = max(mx, k)
#     else:
#         k = 0
# print(mx)

# ровно 2024 раза, мин длина
# f = open(r"D:\ФАЙЛЫ\24\24var01.txt")
# s= f.readline()
# k = l = 0
# m = 10**8
# for r in range(len(s)):
#     if s[r] == 'A': k+=1
#     while k - (s[l] == 'A') >= 2024:
#         k -= s[l] == 'A'
#         l+=1
#     if k == 2024:
#         m = min(m, r-l+1)
# print(m)
#
# from fnmatch import *
# ans = []
# for i in range(0, 10**10+1, 31007):
#     s = str(i)
#     if fnmatch(s, '1*34?5?9'):
#         if i % 31007 == 0:
#             print(i, i//31007)
#
# не более 350 раз, макс длина
# f = open(r"D:\ФАЙЛЫ\24\24var02.txt")
# s = f.readline()
# k = m = l = 0
# for r in range(len(s)):
#     if s[r] == 'A': k+=1
#     while(k > 350):
#         if s[l] == 'A':
#             k-=1
#         l+=1
#     m = max(m , r-l+1)
# print(m)
#
# from fnmatch import *
# for i in range(0, 10**10+1, 12007):
#     s = str(i)
#     if fnmatch(s, '9*?001?1'):
#         if i % 12007 ==0:
#             print(i, i // 12007)
#
# не менее 500 раз, мин длина
# f = open(r"D:\ФАЙЛЫ\24\24var03.txt")
# s = f.readline()
# k = l = 0
# m = float('inf')
# for r in range(len(s)):
#     if s[r] == 'A':
#         k+=1
#     while (k -( s[l] == 'A')) >= 500:
#         if s[l] == 'A':
#             k-=1
#         l+=1
#     if k >= 500:
#         m = min(m , r- l +1)
# print(m)
#
# from fnmatch import *
# for i in range(0, 10**8, 5171):
#     s = str(i)
#     if fnmatch(s, '?19*8?3'):
#         print(i, i // 5171)
#
# а - не более 700 раз, а Е нет вообще
# f = open(r"D:\ФАЙЛЫ\24\24var04.txt")
# s = f.readline()
# k = l = m = 0
# for r in range (len(s)):
#     if s[r] == 'A': k+=1
#     if s[r] == 'E':
#         k = 0
#         l = r+1
#     while k > 700:
#         if s[l] == 'A':
#             k-=1
#         l+=1
#     m = max(m, r-l+1)
# print(m)
#
# from fnmatch import *
# for i in range(0, 10**8, 3377):
#     s = str(i)
#     if fnmatch(s, '?79?8*3'):
#         print(i, i //3377)
#
# а не более 3х раз
# f = open(r"D:\ФАЙЛЫ\24\24var05.txt")
# s = f.readline()
# m = k = l = 0
# for r in range(len(s)):
#     if s[r] == 'A':
#         k+=1
#     while(k > 3):
#         if s[l] == 'A':
#             k-=1
#         l+=1
#     m = max(m, r-l+1)
# print(m)
#
# from fnmatch import *
# for i in range(0, 10**8, 149):
#     s = str(i)
#     if fnmatch(s, '11*223'):
#         print(i, i //149)

