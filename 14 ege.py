#print(int('101110', 2)) #перевод в 10сс

#перевод в нужную сс
# x = 173
# a = []
# while x>0:
#     a = [x%16] + a
#     x = x//16
# print(a) #вывод как надо

# print(bin(100) [2:]) # 10cc -> 2cc
# print(oct(100) [2:]) # 10cc -> 8cc
# print(hex(173) [2:]) # 10cc -> 16cc

#1
# x = 7**103+20*7**204-3*7**57+97
# a = []
# while x>0:
#     a = [x%7] +a
#     x = x// 7
# print (a.count(6)) #подсчет эл-тов
#2
# x = 7**103+6*7**104-3*7**57+98
# a = []
# while x>0:
#     a = [x%7] + a
#     x = x// 7
# print (sum(a)) #сумма списка
#3
# x = 6**203 +5*6**405-3*6**144+76
# a = []
# while x>0:
#     a = [x%6] + a
#     x = x// 6
# print(a.count(0) - a.count(5)) #разница всегда > 0

#4 A,B,C,D,E,F,G
# G-? сколько их G = 16 => просто считаем 16
# x = 17**5 + 85**8 - 10
# a = []
# while x >0:
#     a = [x%17] +a
#     x = x //17
# print (a) #[4, 11, 8, 10, 16, 0, 0, 0, 16, 16, 16, 16, 7]
# print(a.count(16)) #5

#5 параметр - перебор
# for x in range (1, 100):
#     t = 81**20 - 9**x + 50
#     a = []
#     while (t>0):
#         a = [t%9] + a
#         t = t // 9
#     if(sum(a) == 138):
#             print(x)
#6
# for x in range (1, 1000):
#     t = 64**12- 8**14 +x
#     a = []
#     while (t>0):
#         a = [t%8] + a
#         t = t // 8
#     if(a.count(7) ==12 and a.count(1) == 1):
#             print(x)
#6.2
# for x in range (1, 1000):
#     t = oct(64**12- 8**14 +x)
#     if t.count('7') == 12 and t.count('1') == 1:
#         print(x)
#         break

#7 9009x(18)+ 2257x(18), cист.cчисл <20
# for x in '0123456789abcdefgh':
#     a = int(f'9009{x}', 18) + int(f'2257{x}', 18)
#     if a % 15 == 0:
#         a = a//15
#         print(x, a)

# for x in range(18):
#     a = 11*18**4 + 2*18**3 + 5*18**2 + 16*18 + 2*x
#     if a % 15 == 0:
#         print(a//15)

#8
# for x in range(1,22):
#     for y in range (0,13):
#         a = (x*22**4 + 2*22**3 + 3*22**2 + x*22 + 5) - (6*13**4 + 7*13**3 + y*13**2 + 9*13 + y)
#         if a % 57 == 0:
#             print(a//57)

# for x in '123456789abcdefghijkl':
#     for y in '0123456789abc':
#         a = int(f'{x}23{x}5', 22)-int(f'67{y}9{y}', 13)
#         if a % 57 == 0:
#             print(x, y, int(x,22)+int(y,13), a//57)

#9 уравнения
# for n in range (0,100):
#     if n*n + 2*n + 3 == 9 *(n+2) +3:
#         print (n)
#         break

#10 найти систему счисления
#56 и 45 заканчиваются на 1. найти систему счисления
# for n in range(1,20):
#     if 56 % n == 1 and 45 % n == 1:
#         print (n)
#         break

# 338 d cc n содержит 3 цифры и последния == 2. максим сс?
# for n in range(2, 40):
#     if 338 % n == 2 and n**2 <= 338 < n**3:
#         print (n)

#11 найти сколько чисел <= 50 в 2 сс заканчиваются на 011
# k =0
# for x in range (1, 51):
#     b = bin(x)
#     if (b[-3] + b[-2] + b[-1] == "011"):
#         k += 1
#         print(k)
# в 3 сс зак на 21
# for x in range (3, 51 ):
#     t = x
#     a = []
#     while x >0:
#         a = [x%3] + a
#         x = x // 3
#     if a[-1] == 1 and a[-2] ==2:
#         print(t, a)
# в 16 сс заканчиваются на "c", числа меньше 100
# for x in range (1, 100):
#     if (x % 16 == 12):
#         print (x)

# какая то задачка
# for x in range (1, 100):
#     if 10<= x < 100 and x % 16 == 10 and x % 5 == 3:
#         print (x)

#
# for n in range (0, 100):
#     if 27<=n<81 and 49<=n<343 and n//8%8 == 1 and n % 8 =f= 7:
#         print (n)

# for x in range(10):
#     for y in range(1000):
#         a = int(f'1{x}2139{y}4')
#         if a % 2023 == 0:
#             print(a, a//2023)

# for x in range (21, 30):
#     if x % int('100', 3) == int('11', 3):
#    print (x)

# for x in '0123456789abcdefgh':
#     a = int(f'9009{x}', 18) + int(f'2257{x}', 18)
#     if a % 15 == 0:
#         a = a//15
#         print(x, a)

# for x in '0123456789abcdefg':
#     a = int(f'9759{x}', 17 ) + int(f'3{x}108', 17)
#     if a % 11 == 0:
#         print(x, a //11)
#
# for x in '0123456789a':6', 12) == int(f'55{x}87', 14):
# #         print(x, int(f'55{x}87', 14))
#    if int(f'3364{x}', 11) + int(f'{x}794

# for x in '123456789abcdefghig':
#     for y in '123456789abcdefghig':
#         a = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
#         if a % 18 == 0:
#             print(x, y, a//18)
# x = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 -2*25**4 - 2024
# a = []
# while x >0:
#     a = [x%25] +a
#     x = x //25
# print(a.count(0)) #5
# x = 2 * 729**333 + 2*243**334 - 81**335 + 2 *27**336 - 2*9**337-338
# a =[]
# while x>0:
#     a = [x%9]+a
#     x = x//9
# print(a.count(1)+a.count(2)+a.count(3)+a.count(4)+a.count(5)+a.count(6)+a.count(7)+a.count(8)+a.count(0))