import random

# list = []
# for i in range(20):
#     list.append(random.randint(0, 100))
# print(list)

# i = 0
# db = 0
# hossz = len(list)

# while i < hossz:
#     if(list[i] >= 45 and list[i] <= 55):
#         print(f"{i}.: {list[i]}")
#         db += 1
#     i += 1
# if (db == 0): print('nem volt egy elem sem')
# szamok = input('Vesszővel elválasztva számok: ')
# szorzat = 1
# for szam in szamok.split(","):
#     szorzat *= int(szam)
# print(szorzat)

# lista = []
# for x in range(50):
#     lista.append(random.randint(0, 100))
# print(f"lista: {lista}")
# ip = int(input("keresett szam: "))
# i = 0
# while(i < len(lista) and lista[i] != ip):
#     i += 1
# if(i < len(lista)):
#     print(f"keresett szám indexe: {i}")
# else: print('nincs ilyen szám')

# also = int(input("also: "))
# felso = int(input("felso: "))
# lista = []
# for x in range(50):
#     lista.append(random.randint(also, felso))
# print(f"lista: {lista}")
# avg = round((also + felso) / 2)
# i = 0
# while(i < len(lista)):
#     if(lista[i] == avg): 
#         print(f"megvan, itt: {i}")
#         break
#     i += 1
# else: print('nincs benne')

lista = []
for x in range(10):
    lista.append(random.randint(10, 40))
print(f"{lista}")
db = 0
for elem in lista:
    i = 2
    while i < elem // 2:
        if not elem % i:
            break
        i += 1
    else: db += 1
#db = 0
#for elem in lista:
#   osztok_szama = 0
#   for vizsgalt_szam in range(2, elem // 2):
#      if elem % vizsgalt_szam == 0:
#           osztok_szama += 1
#   if osztok_szama == 0:
#       db += 1
print(f"primek szama: {db}")