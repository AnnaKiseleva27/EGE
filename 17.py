# with open("17.txt") as file:
#     a = [int(x) for x in file]
#     print(a)
# a = [int(x) for x in open("17.txt")]
# print(a)
# am = [x for x in a if str(abs(x))[0] == '8']
# m = max(am)

# with open("17.txt") as file:
#     a = [int(x) for x in file]
#     ans = []
#     m = 0
#     for i in range(len(a)):
#         if(str(abs(a[i]))[0] == '8'):
#             m = max(m , a[i])
#     for i in range(0, len(a)- 2):
#         x, y, z = a[i], a[i+1], a[i+2]
#         if(str(abs(x))[0] == '6') + (str(abs(y))[0] == '6')+(str(abs(z))[0] == '6') <= 1:
#             if(x+y+z >= m):
#                 ans.append(x+y+z)
#     print(min(ans), len(ans))

# with open(r"C:\Users\Анна\OneDrive\Документы\DEV EGE IT\BBB.txt") as file:
#     n = int(file.readline())
#     a = [int(file.readline()) for i in range(n)]
#     b = [int(file.readline()) for i in range(n)]
# rec = 10000000
# i = 0
# j =0
# while(i <n and j <n):
#     rec = min(rec, abs(a[i] - b[j]))
#     if a[i] < b[j]:
#         i+=1
#     else:
#         j+=1
# print(rec)
# with open(r"C:\Users\Анна\Downloads\17_12249.txt") as file:
#     a = [int(x) for x in file]
#     ans =[]
#     m = 0
#     for i in range(len(a)):
#         if a[i]> 0:
#             if len(str(a[i])) == 5 and a[i] % 10 == 3:
#                 if (a[i] > m):
#                     m = a[i]
#     for i in range(len(a) - 2):
#         x, y, z = a[i], a[i + 1], a[i + 2]
#         if(str(abs(x))[0] == '3') + (str(abs(y))[0] == '3')+(str(abs(z))[0] == '3') > 0:
#             if (x+y+z <= m) :
#                 ans.append(x+y+z)
#     print(len(ans), max(ans))

# f = open(r"C:\Users\Анна\Downloads\17_8__1t7bu (1).txt")
# a = [int(x) for x in f]
# ans = []
# for i in range(len(a)):
#     if a[i] % 16 == 3 and a[i] % 4 != 0 and a[i] % 64 != 0:
#         ans.append(a[i])
# print(max(ans) - min(ans) , len(ans))

# f = open(r"C:\Users\Анна\Downloads\17_2__1t7bm.txt")
# a = [int(x) for x in f]
# ans =[]
# for i in range(len(a)- 1):
#     if a[i] % 9 ==0 and a[i] % 13 != 0 and a[i+1] % 9 ==0 and a[i+1] % 13 != 0:
#         ans.append(a[i] + a[i+1])
# print(len(ans), min(ans))

# f = open(r"C:\Users\Анна\Downloads\1__1vf52.txt")
# a = [int(x) for x in f]
# ans = []
# mx = max([int(x) for x in a if x % 15 == 0])
# for i in range(len(a)-1):
#     if a[i] > mx or a[i+1] > mx:
#         ans.append(a[i]+a[i+1])
# print(len(ans), min(ans))

# f = open(r"C:\Users\Анна\Downloads\8__1vf5e.txt")
# a = [int(x) for x in f]
# ans = []
# for i in range(len(a) -1):
#     if a[i] % 5 == 0 or a[i+1] % 5 == 0:
#         if (a[i]+a[i+1]) % 10 == 0:
#             ans.append(a[i] + a[i+1])
# print(len(ans), max(ans))

# f = open(r"C:\Users\Анна\Downloads\9__1vf5f.txt")
# a = [int(x) for x in f]
# ans = []
# for i in range(len(a)-1):
#     if (a[i]+a[i+1]) % 134 == 0:
#         ans.append(a[i]+a[i+1])
# print(len(ans), max(ans))
#
# f = open(r"C:\Users\Анна\Downloads\10__1vf5g.txt")
# a = [int(x) for x in f]
# ans  = []
# for i in range(len(a) - 1):
#     if abs(a[i] -a[i+1]) % 2 == 0 and (a[i] % 11 == 0 or a[i+1] % 11 ==0):
#         ans.append(a[i] +a[i+1])
# print(len(ans), min(ans))

# f = open(r"C:\Users\Анна\Downloads\17_2__1d7nd.txt")
# a = [int(x) for x in f]
# ans = []
# for i in range(len(a)-1):
#     if a[i] % 11 != a[i+1] % 11 and (a[i] % 13 == 0 or a[i+1] % 13 ==0):
#         ans.append(a[i]+a[i+1])
# print(len(ans), max(ans))

# f = open(r"C:\Users\Анна\Downloads\17_6__1d7nl.txt")
# a = [int(x) for x in f]
# ans  = []
# mx = max([int(x) for x in a if x % 41 == 0])
# for i in range(len(a) -1):
#     if a[i]+a[i+1] < mx:
#         ans.append(a[i+1] +a[i])
# print(len(ans), max(ans))

# f = open(r"C:\Users\Анна\Downloads\8__1n2v3.txt")
# a = [int(x) for x in f]
# ans = []
# for i in range (len(a)):
#     for j in range(i+1, len(a)):
#         if (a[i] * a[j]) % 34 != 0:
#             ans.append(a[i]+a[j])
# print(len(ans), max(ans))

# f = open(r"C:\Users\Анна\Downloads\17_1__1kac1.txt")
# a = [int(x) for x in f]
# mn = min(a)
# ans = []
# for i in range(len(a)-1):
#     if a[i] % 2506 == mn or a[i + 1] % 2506 == mn:
#         ans.append(a[i] * a[i+1])
# print(len(ans), min(ans))

# f = open(r"D:\ФАЙЛЫ\17-1.txt")
# a = [int(x) for x in f]
# srar = sum(a) // len(a)
# ans = []
# for i in range(len(a)-2):
#     if a[i] < srar or a[i+1] < srar or a[i+2] < srar:
#         if abs(a[i]) % 10 == 6 or abs(a[i+1]) % 10 == 6 or abs(a[i+2]) % 10 == 6:
#             ans.append(a[i] + a[i+1] + a[i+2])
# print(len(ans), max(ans))











