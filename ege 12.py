# s = '8'*70
# while "2222" in s or "8888" in s:
#     if "2222" in s:
#         s = s.replace("2222", "88", 1)
#     else:
#         s = s.replace("8888", "22", 1)
#     print (s)

# s ='2'+ '5'*81
# print(s)
# while "25" in s or "355" in s or "4555" in s:
#     if "25" in s:
#         s = s.replace("25", "4", 1)
#     if "355" in s:
#         s = s.replace("355", "2", 1)
#     if "4555" in s :
#         s = s.replace("4555", "3", 1)
#     print(s)

# s = '1'+ '0'*33
# k = 0
# while '1' in s or "100" in s:
#     if "100" in s:
#         s = s.replace ("100", "0001", 1)
#     else:
#         s =s.replace ('1', "00", 1)
# for i in s:
#     if i == '0':
#         k+=1
# print(k)

# s = '1'*46 + '2'*31
# while "1111" in s:
#     s = s.replace("1111", "2", 1)
#     s = s.replace("222", '1', 1)
# print(s)

# к исходной строке, содержащей не более 50 шестерок приминили операции,
#  и получии 21. 1. пербор сверху или
# for i in range(1, 51):
#     s = '6' * i
# # s = '6'*48
#     while "66" in s:
#         s = s.replace("66", "1", 1)
#         s = s.replace("11", "2", 1)
#         s = s.replace("22", "6", 1)
#     if s == "21":
#         print(i)

# s = '>' + '1'*11 + '2'*12 + '3' * 30
# while ">1" in s or ">2" in s or ">3" in s:
#     if ">1" in s:
#         s = s.replace(">1", "22>", 1)
#     if ">2" in s:
#         s = s.replace(">2", "2>", 1)
#     if ">3" in s:
#         s = s.replace(">3", "1>", 1)
#     print(s, s.count('2')* 2 + s.count('1')*1)

# for i in range(1, 50):
#     for j in range (1, 50):
#         for d in range(1, 50):
#             s = '0' + '1'*i + '2'*j +'3' *d
#             while "01" in s or "02" in s or "03" in s:
#                 s = s.replace("01", "302", 1)
#                 s = s.replace("02", "3103", 1)
#                 s = s.replace("03", "20", 1)
#             if s.count('1') == 28 and s.count('2') == 34 and s.count('3') == 45:
#                 print(i)

#когда нужно посчитать максимальное количество чего то в строке и нам
#не известен порядок, то нужно найти порядок дающие макс значение
# s = "9992" * 33 + '2' * 14 + '29' + '1'*14
# while "999" in s or "22" in s:
#     if "999" in s:
#         s = s.replace("999", '12', 1)
#     else:
#         s = s.replace("22", '1', 1)
#     print(s.count('1'))

# for i in range(1, 11):
#     s = '5'*i
#     while "555" in s or "888" in s:
#         s = s.replace("555", "8", 1)
#         s = s.replace("888", "55", 1)
#     print(s)


# s = '1'
# for n in range(3, 10000):
#     s = '8'*n
#     while "18" in s or "388" in s or "888" in s:
#         if "18" in s:
#             s = s.replace("18", "8", 1)
#         if "388" in s:
#             s = s.replace("388", "81", 1)
#         if "888" in s:
#             s = s.replace("888", "3", 1)
#     if s.count('1') == 3:
#         print(n)
# ms = 0
# # for n in range(3, 10000):
# #     s = '2'*n
# #     while "12" in s or "322" in s or "222" in s:
# #         if "12" in s:
# #             s = s.replace("12", "2", 1)
# #         if "322" in s:
# #             s = s.replace("322", "21", 1)
# #         if "222" in s:
# #             s = s.replace("222", "3", 1)
# #     sm = sum(map(int, s))
# #     ms = max(sm, ms)
# # print(ms)

# for n in range(4, 200):
#     s = '5' + n*'2'
#     while "72" in s or "522" in s or "2222" in s:
#             s=s.replace("72", "2" , 1)
#             s=s.replace("522", '27', 1)
#             s=s.replace("2222",'5', 1)
#     sm = sum(map(int, s))
#     if (sm == 63):
#         print(n)

# for n in range(3, 100):
#     s = '3' + n*'5'
#     while "25" in s or "355" in s or "555" in s:
#         s=s.replace("25", "32", 1)
#         s = s.replace("355", "25", 1)
#         s = s.replace("555", "3", 1)
#     sm = sum(map(int, s))
#     if sm == 17:
#         print (n)

# for n in range(1, 1000):
#     string = ''
#     string1 = ''
#     summm = 0
#     while n > 0:
#         string += str(n % 3)
#         n //= 3
#     n2 = string
#     if (n % 2) == 0:
#         n2 = '1' + n2 + '0' + '0'
# a = []
# for x in range(3, 10000):
#     s = "3"+"5"*x
#     while "333" in s or "555" in s:
#         if "555" in s:
#             s= s.replace("555", "3", 1)
#         else:
#             s=s.replace("333", "5", 1)
#     m = list(map(int, s))
#     a.append(sum(m))
# print(max(a))

# s = '5'*38
# while '555' in s or '333' in s:
#     if '555' in s:
#         s = s.replace('555', '3', 1)
#     else:
#         s = s.replace('333', '5', 1)
#     print(s)

# s = '12' * 13
# while '12' in s or '2222' in s:
#     s = s.replace('12', '2', 1)
#     s = s.replace('222', '2', 1)
# print(s)

























