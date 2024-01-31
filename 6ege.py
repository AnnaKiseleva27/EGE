# cnt = 0
# for x in range(-177, 177):
#     for y in range(-353, 0):
#         if y < x and y < -x and y > x - 125000 ** 0.5 and y> -x - 125000 ** 0.5:
#             cnt+=1
# print(cnt)
# a = int("75332", 13)+int("23173", 13)
# print(a//12)
# def f(n):
#     if (n==0) :return 0;
#     if (n % 2 == 1) :return f(n-1)+1
#     if (n % 2 == 0) :return f(n / 2)
#def f( a, b):
 #   if a<b or a == 9 or a == 16: return 0
 #   if a == b: return 1
#    if a > b: return f(a-1,  b) + f(a-2, b) +f(a//3, b)
#print(f(19, 3))
# def f(n):
#     a = []
#     while n > 0:
#         a = [n % 10] + a
#         n = n // 10
#     return sum(a)
# for n in range(1, 30):
#
#     if(f(n) % 2 ==0):
#         x = '10' + (bin(n)[2::]) + "00"
#     else: x = "11" + (bin(n)[2::]) + "11"
#     if (int(x, 2) > 503):
#         print(n, int(x, 2))
# s = ">"+"1"*25 + "2"*17 + "3"*10
# while ">1" in s or ">2" in s or ">3" in s:
#     if ">1" in s:
#         s=s.replace(">1", "22>3", 1)
#     if ">2" in s:
#         s = s.replace(">2", "2>", 1)
#     if ">3" in s:
#         s=s.replace(">3", "11>2", 1)
# x = int(s[:-1])
# a = []
# while(x>0):
#     a = [x % 10] +a
#     x = x//10
# print(sum(a))
# for x in range(1, 80):
#     a = 3*80**3 + x*80**2 +7*80 + 5 + 1*80**3 + 4*80**2 + x*80 + 0
#     if(a% 17 == 0):
#         print(x, a//17)

for i in range(1, 1000000):
    if i == 17*(i% 1024):
        print(i)