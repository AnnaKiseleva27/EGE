#2 правило произведения
# from itertools import product
# k = 0
# for x in product('KM', 'KYMA','KEMA','KYMA', 'YA' ):
#     s = ''.join(x)
#     k = k+1
# print (k)

# k = 0
# for a in 'LT':
#     for b in 'LETO':
#         for c in 'LETO':
#             for d in 'LETO':
#                 s = a+b+c+d
#                 k = k + 1
# print (k)
# 4
# функция product подключается из библиотеки интертулс.
#с помощью нее можно сделать перебор.
# в коде ниже, перебор, где ЭЮЯ встрчаются только на 1 и поселдней позиции слов,
# а АВСг на остальных.
# from itertools import product
# k = 0
# for x in product('ЭЮЯ','ABCп','ABCп','ABCп','ЭЮЯ'):
#     s = ''.join(x)
#     k = k+1
# print (k)
#случаи и подсчет от противного
#12
# from itertools import product
# k = 0
# for x in product('ЖИРАФ', repeat = 5):
#     s = ''.join(x)
#     if s.count ('Ж') == 1 and s[0] != 'Ф' and s[-1] != 'Р':
#         k = k+1
# print (k)
#7
# from itertools import product
# k = 0
# for x in product ('АНИМЕ', repeat = 4):
#     s = ''.join(x)
#     k = k+1
# for x in product ('АНИМЕ', repeat = 5):
#     s = ''.join(x)
#     k = k+1
# for x in product ('АНИМЕ', repeat = 6):
#     s = ''.join(x)
#     k = k+1
# print(k)
#пересатновки
#13
# from itertools import permutations
# k = 0
# for x in set(permutations('accacin')):
#         k = k+1
# print (k)
#14
# from itertools import permutations
# k = 0
# for x in set(permutations('kaliu')):
#     s = ''.join(x)
#     if s[0] != 'u' and 'ia' not in s:
#         k = k+1
# print (k)
#16
#all - все условия выполнились
# sub - множество
# from itertools import permutations
# k = 0
# for x in set(permutations('peckari')):
#     s = ''.join(x)
#     #if s[0] != 'i' and 'ie' not in s and 'ia' not in s and 'ir' not in s :
#     if s[0] != 'i' and all(sub not in s for sub in ['ie', 'ia', 'ir']):
#         k = k+1
# print (k)
#15
# from itertools import permutations
# k = 0
# w = ['оу', 'уо ', 'кл','лк','кн', 'нк', 'лн','нл'] #список запрещенных сочетаний
# for x in set(permutations('колун')):
#     s = ''.join(x)
#     if all(sub not in s for sub in w):
#         k = k +1
# print (k)
#цифры
#18
# from itertools import product
# k = 0
# for x in product ('01234567', repeat = 4):
#     s = ''.join(x)
#     if s[0] != '0' and s[-1] in '04':
#         k = k+1
# print (k)
#19 возрастание и убывания (каждый след символ >= / <= предыдущего)
# from itertools import product
# k = 0
# for x in product ('01234567', repeat = 5):
#     s = ''.join(x)
#     if s[0] >= s[1]>=s[2]>=s[3] and s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
#         k = k+1
# print (k)
#AAAAA AAAAB AAAAC
# from itertools import product
# k = 0
# for x in product('AKRY', repeat = 5):
#     k = k+1
#     s= ''.join(x)
#     if k == 150:
#         print (k,s)
#22
# from itertools import product
# k = 0
# for x in product('aoy', repeat = 5):
#     k = k+1
#     s= ''.join(x)
#     if s == 'yayay':
#         print (k,s)
#23
# from itertools import product
# k = 0
# for x in product('akry', repeat = 5):
#     k = k+1
#     s= ''.join(x)
#     if s[0] == 'k':
#     #if s == 'kaaaa':
#         print (k,s)
#         break
#24
# from itertools import product
# k1 = 0
# k2 = 0
# k = 0
# for x in product('aoy', repeat = 5):
#     k = k+1
#     s= ''.join(x)
#     if s == 'yayay':
#         k1 = k
#         if s == 'oyoya':
#             k2 = k
# print (k1 - k2 +1)
#домашка кегэ
#11
# from itertools import product
# k = 0
# for x in product ('ABCD', repeat = 4):
#     s = ''.join(x)
#     if s[0] <= s[1] and s[1] <= s[2] and s[2] <= s[3]:
#         k = k+1
#     print (k)
#12
# from itertools import product
# k = 0
# for x in product ('гeпaрд', repeat = 5):
#     s = ''.join(x)
#     if s[0] != 'a' and s[-1] != 'e' and s.count ('г') == 1:
#         k = k+1
#     print (k)
# 13
# from itertools import product
# k = 0
# for x in  product('0123456789', repeat = 3):
#     s = ''.join(x)
#     if s[0] <= s[1] <= s[2] and s[0] != '0':
#         k = k +1
# print (k)
# 15
# from itertools import permutations
# k = 0
# for x in permutations('вайфу', r= 4):
#     s = ''.join(x)
#     if s[0] != 'й' and s.count('вф') == 0 and s.count ( 'фв') == 0 :
#         k = k+1
# print(k)


