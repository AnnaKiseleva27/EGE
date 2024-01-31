# a = [3072, 4272, 5672, 7443, 9651, 12147, 15176, 18816, 22848, 27603]
# m = 0
# for i in range(len(a) - 1):
#     for j in range(i+1, len(a)):
#         if a[i] % 4 ==0 and a[j] % 4 == 0:
#             m = max(m , a[i] * a[j])
# print(m)

# a = [3072, 4272, 5672, 7443, 9651, 12147, 15176, 18816, 22848, 27603]
# k = 0
# for i in range(len(a) -1):
#     for j in range(i+1, len(a)):
#         s = a[i] + a[j]
#         print(a[i], a[j] , s)
# n = int(input())
# a = []
# a = [int(i) for i in input().split()]
# while(n):
#     i = int(input())
#     a.append(i)
#     n-=1
# print(a)
# for i in range(n):
#     i = int(input())
#     a.append(i)
# print(a)
# n = int(input())
# a = []
# mx = 0
# for i in range(n):
#     k = int(input())
#     a.append(k)
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         mx = max(mx, a[i] * a[j])
# print(mx)
# f = open(r"C:\Users\Анна\Downloads\27-13a__1vjmy.txt")
# n = f.readline()
# mx = 0
# a = [int(x) for x in f]
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         s = a[i] + a[j]
#         if s % 12 == 0:
#             mx = max(mx, s)
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\15_A__1vjym.txt")
# n = f.readline()
# a = [int(x) for x in f]
# s = mx = 0
# for i in range(len(a)- 1):
#     for j in range(i+1, len(a)):
#         s = a[i] + a[j]
#         if s % 7 == 0:
#             mx = max(mx, s)
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\27A_4__1vq0j.txt")
# n = f.readline()
# a = [int(x) for x in f]
# ans = []
# for i in range(len(a)-2):
#     for j in range(i+1, len(a) -1):
#         if abs(a[i] - a[j]) % 2 ==0 and (a[i] % 16 == 0 or a[j] % 16 ==0):
#             ans.append([a[i], a[j]])
# ans.sort(key = lambda x : x[0]+x[1])
# ans.reverse()
# print(ans)

# делимость
# f = open(r"C:\Users\Анна\Downloads\1_B__2kc3h.txt")
# mx = [0]*11
# ms = 0
# n = int(f.readline())
# x = int(f.readline())
# for i in range(n - 1):
#     if mx[x%11] < x:
#         mx[x%11] = x
#     x = int(f.readline())
#     t = (11 - x % 11) % 11
#     if (x+mx[t]) > ms:
#         ms = x + mx[t]
# print(ms)

# f = open(r"C:\Users\Анна\Downloads\4_B__2kc2v.txt")
# mx = 0
# m1 = m3 = m15 = m5 = 0
# n = int(f.readline())
# x = int(f.readline())
# for i in range(n-1):
#     if x > m1: m1 = x
#     if x > m3 and x % 3 != 0: m3 = x
#     if x > m5 and x % 5 != 0: m5 = x
#     if x > m15 and x % 15 != 0: m15 = x
#     x = int(f.readline())
#     if (x*m1 > mx) and (x*m1) % 15 !=0:
#         mx = x*m1
#     if (x * m3 > mx) and (x * m3) % 15 != 0:
#         mx = x * m3
#     if (x * m5 > mx) and (x * m5) % 15 != 0:
#         mx = x * m5
#     if (x * m15 > mx) and (x * m15) % 15 != 0:
#         mx = x * m15
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\3_A__2kc31 (2).txt")
# ms = 0
# mx1 = [0]*9
# mx2 = [0]*9
# mx = []
# mxx = 0
# n = int(f.readline())
# for i in range(n):
#     a = int(f.readline())
#     for j in range (9):
#         if a % 9 == j:
#             if a >= mx1[j]:
#                 mx2[j] = mx1[j]
#                 mx1[j] = a
#             elif a>= mx2[j]:
#                 mx2[j] = a
# for x in mx1:
#     for y in mx2:
#         if (x+y) % 9 !=0:
#             mx.append(x+y)
# for x in mx1:
#     for y in mx1:
#         if (x+y) % 9 !=0 and x != y:
#             mx.append(x+y)
# for x in mx2:
#     for y in mx2:
#         if (x+y) % 9 !=0 and x != y:
#             mx.append(x+y)
# print(max(mx))
#
# f = open(r"C:\Users\Анна\Downloads\5_B__2kc2q.txt")
# n = int(f.readline())
# x = int(f.readline())
# mx = 0
# ost = [0]*7
# for i in range(n - 1):
#     if ost[x%7] < x:
#         ost[x%7] = x
#     x = int(f.readline())
#     for j in range(len(ost)):
#         for k in range(len(ost)):
#             if (j + k + x%7) % 7 == 0:
#                 mx= max(mx, ost[j] + ost[k] + x)
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\27_B__1pa6l.txt")
# n = int(f.readline())
# x = int(f.readline())
# ms = 0
# m1 = m17 = m34 = m2 = 0
# for i in range(n - 1):
#     if x >m1 : m1 = x
#     if x > m2 and x%2 ==0: m2 = x
#     if x> m17 and x %17 ==0: m17 = x
#     if x> m34 and x %34 ==0: m34 = x
#     x = int(f.readline())
#     if (x*m1 > ms) and (x*m1) % 34 ==0:
#         ms = x*m1
#     if (x*m2 > ms) and (x*m2) % 34 ==0:
#         ms = x*m2
#     if (x*m17 > ms) and (x*m17) % 34 ==0:
#         ms = x*m17
#     if (x*m34 > ms) and (x*m34) % 34 ==0:
#         ms = x*m34
# print(ms)

# # f = open(r"C:\Users\Анна\Downloads\27-15b__1vjn2.txt")
# f = open(r"C:\Users\Анна\Downloads\27-15a__1vjn1.txt")
# n = int(f.readline())
# cnt = 0
# m1 = m13 = m26 = m2 = 0
# for x in range(n):
#     x = int(f.readline())
#     if x % 26 == 0 : m26+=1
#     elif x % 13 == 0: m13 +=1
#     elif x % 2 == 0: m2+=1
# k26 = m26 * (m26 - 1) // 2 + m26 * (n- m26) + m2 * m13
# print(k26)

# # f = open(r"C:\Users\Анна\Downloads\27-14a__1vjmz.txt")
# f = open(r"C:\Users\Анна\Downloads\27-14b__1vjn0 (1).txt")
# n = int(f.readline())
# cnt = 0
# m1 = m11 = m22 = m2 = 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 22 == 0 : m22+=1
#     elif x % 11 == 0 : m11+=1
#     elif x % 2 == 0 : m2+=1
# k22 = m22 * (m22 - 1) // 2 + m22 * (n - m22) + m2 * m11
# print(k22)

# f = open(r"C:\Users\Анна\Downloads\27-11a__1vjmt (1).txt")
# f = open(r"C:\Users\Анна\Downloads\27-11b__1vjmu.txt")
# n = int(f.readline())
# x = int(f.readline())
# mx = 0
# ost = [0]*6
# for i in range(n - 1):
#     if ost[x%6] < x:
#         ost[x%6] = x
#     x = int(f.readline())
#     for j in range(len(ost)-3):
#         for k in range(j+1, len(ost)-2):
#             for z in range(k+1, len(ost)-1):
#                 if (j + k + z + x%6) % 6 == 0:
#                     mx= max(mx, ost[j] + ost[k] + ost[z] + x)
# print(mx)

# f = open(r"C:\Users\Анна\Downloads\27-9a__1vjmp.txt")
# f = open(r"C:\Users\Анна\Downloads\27-9b__1vjmq.txt")
# n = int(f.readline())
# mn = 1000000000000000
# ost = [10000000000]*7
# x = int(f.readline())
# for i in range(n-1):
#     ost[x%7] = min([ost[x%7], x])
#     x = int(f.readline())
#     t = (7 - x% 7) % 7
#     if (x+ ost[t])% 7 == 0:
#         mn = min(mn, x +ost[t])
# print(mn)

# n = 4
# nums = [1, 2, 3, 1]
# totalSum = sum(nums)
# currSum = maxSum = curr_minSum = minSum = nums[0]
# for i in range(1, n):
#     currSum = max(currSum + nums[i], nums[i])
#     maxSum = max(maxSum, currSum)
#     curr_minSum = min(curr_minSum + nums[i], nums[i])
#     minSum = min(minSum, curr_minSum)
# if (totalSum != minSum):
#     print(max(totalSum - minSum, maxSum))
# else:
#     print(maxSum)

# f = open(r"C:\Users\Анна\Downloads\27A_2719.txt")
# f = open(r"C:\Users\Анна\Downloads\27A_2723.txt")
# n = int(f.readline())
# a = [int(x) for x in f]
# k19 = 0
# for i in range(len(a)):
#     if a[i] % 19 == 0 : k19+=1
# print(k19*(k19-1)*(k19 - 2)//6)

# f = open(r"C:\Users\Анна\Downloads\27A_2719.txt")
# f = open(r"C:\Users\Анна\Downloads\27A_2722.txt")
# n = int(f.readline())
# a = [int(x) for x in f]
# kck5 = knk5 = kcn5 = knn5 = 0
# for i in range(len(a)):
#     if a[i] % 5 == 0 and a[i] % 2 == 0: kck5 +=1
#     if a[i] % 5 ==0 and a[i] % 2 != 0: knk5 +=1
#     if a[i] % 5 != 0 and a[i] % 2 == 0:kcn5 +=1
#     if a[i] % 5 != 0 and a[i] % 2 != 0: knn5 += 1
# print(kck5 * knk5 + kck5 * knn5 + kcn5*knk5)

# f = open(r"C:\Users\Анна\Downloads\27A_2725.txt")
# n = int(f.readline())
# a = [int(x) for x in f]
# k = [0] *80
# k5 = [0]*80
# count = 0
# for i in range(len(a)):
#     ost = a[i] % 80
#     if  a[i] > 50000:
#         k5[ost] +=1
#     else:
#         k[ost] +=1
# count += k5[0]*(k5[0]-1)//2 + k5[40]*(k5[40]-1)//2
# for i in range(1, 39 + 1):
#     count += k5[i]*k5[80 - i]
# count += k5[0]*k[0]+ k5[40]*k[40]
# for i in range(1, 39 + 1):
#     count += k5[i]*k[80 - i]
#     count += k[i]*k5[80 - i]
# print(count)

# # f = open(r"C:\Users\Анна\Downloads\27A_2719.txt")
# f = open(r"C:\Users\Анна\Downloads\27B_2737.txt")
# n = int(f.readline())
# s = [0] * 2000
# count = 0
# for i in range(n):
#     x = int(f.readline())
#     if x < 2000: s[x]+=1
# count+= s[1000]*(s[1000] - 1)//2
# for i in range(1, 999+1):
#     count+= s[i] * s[2000 - i]
# print(count)

# f = open(r"C:\Users\Анна\Downloads\27B_2729.txt")
# n = int(f.readline())
# x = int(f.readline())
# ost = [1000000] * 11
# c = 100000000
# for i in range(n - 1):
#     if x < ost[x% 11]:
#         ost[x%11] = x
#     x = int(f.readline())
#     for i in range(len(ost)):
#         for j in range(i+1, len(ost)-1):
#             if (ost[i] +ost[j] + x ) % 11 == 0:
#                 c = min(c,ost[i] +ost[j] + x )
# print(c)

# f = open(r"D:\DEV EGE IT\27aaa(1).txt")
# n = int(f.readline())
# x = int(f.readline())
# ms = 0
# ans = []
# ost = [0]*113
# for i in range(n - 1):
#     if x > ost[x%113]:
#         ost[x%113] = x
#     x = int(f.readline())
#     t = (113 - x % 113) % 113
#     if (x + ost[t] > ms):
#         ms = ost[t] + x
#         ans.append(x)
#         ans.append(ost[t])
# print(ms, len(ans))

f = open(r"D:\ФАЙЛЫ\27-71b.txt")
n = int(f.readline())
s = ms = 0
ml = 0
m = [10 ** 20] * 69
l = [0] * 69
for i in range(n):
    x = int(f.readline())
    s += x
    if s % 69 == 0:
        if s > ms:
            ms = s
            ml = i + 1

    s1 = s - m[s % 69]
    l1 = (i + 1) - l[s % 69]
    if s1 > ms:
        ms = s1
        ml = l1

    if s < m[s % 69]:
        m[s % 69] = s
        l[s % 69] = i + 1
print(ms, ml)
