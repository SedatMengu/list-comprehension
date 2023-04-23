# elimizde bulunan herhangi bir listeden istenen koşulları sağlayan yeni listeler oluşturma işlemidir.

numbers=[1,2,3,4,5,6,7,8]

# yukardaki rakamları kullanarak bir liste oluşturalım

# eski yöntem :

liste1=[]
for i in numbers:
    liste1.append(i)
print(liste1)                    # / [1, 2, 3, 4, 5, 6, 7, 8]

# eskşi yöntem 2 :

liste2=[]

for i in range(1,9):
    liste2.append(i)
print(liste2)                  # / [1, 2, 3, 4, 5, 6, 7, 8]

# yeni yöntem : 

liste3 = [number for number in numbers]            # / [1, 2, 3, 4, 5, 6, 7, 8]
print(liste3)


# yukarıdaki listedeki elemanlarının kareleri ile bir liste oluşturalım

# eski yöntem: 
liste4=[]

for i in range(1,9):
    liste4.append(i*i)
print(liste4)               # / [1, 4, 9, 16, 25, 36, 49, 64]

# eski yöntem:
liste5=[]

for i in range(1,9):
    liste5.append(pow(i,2))
print(liste5)               # / [1, 4, 9, 16, 25, 36, 49, 64]

# yeni yöntem:

liste6= [i*i for i in numbers]
print(liste6)                      # / [1, 4, 9, 16, 25, 36, 49, 64]


# listedeki çift rakamlardan oluşan yeni bir liste yapalım

# eski yöntem:

liste7=[]
for i in range(1,9):
    if i %2 == 0:
        liste4.append(i)
    continue

print(liste7)               # / [2, 4, 6, 8]

# yeni yöntem:

liste8 = [i for i in numbers if i%2==0]
print(liste8)              # / [2, 4, 6, 8]

# listede verilen çift rakamlardan oluşan bir liste yapalım

# eski yöntem
liste9= []
for i in range(1,9):
    if i %2 == 0 :
        liste9.append(i*i)
print(liste9)                   # / [4, 16, 36, 64]

# yeni yöntem

liste10 = [pow(i,2) for i in numbers if i%2==0]

print(liste10)                  # / [4, 16, 36, 64]


# listede verilen 4ten büyülk ve çift rakamlardan oluşan bir liste yapalım


# eksi yöntem

liste11=[]
for i in range(1,9):
    if i >=4 :
        if i %2==0:
            liste11.append(i*i)
print(liste11)                   # / [16, 36, 64]

# yeni yöntem

liste12=[pow(i,2) for i in numbers if i >=4 and i %2==0 ]
print(liste12)                  # / [16, 36, 64]

rakamlar = [1,2,3,4,5]
harfler = "abcde"

# soru : 1,a 1,b 1,c 1,d 1,e 2,a 3,b şeklinde list olarak sıralama yapalım.

# eski yöntem 

liste13=[]
for i in rakamlar:
    for j in harfler:
        liste13.append((i,j))
print(liste13)

# yeni yöntem

liste14 = [(i,j) for i in rakamlar for j in harfler]
print(liste14)


liste15 = [1,2,3,4,5,6,7,8,9]
liste16 = [2,3,6,9,5]

# birinci listede bulunup ikinci listede bulunmayan rakamların karesinden yeni bir liste olutşuralım

# eski yöntem

liste17=[]
for i in liste1:
    if i not in liste2:
        liste17.append(i*i)
    else :
        continue
    
print(liste17)               # / [1, 16, 49, 64]

# yeni yöntem

liste18= [i*i for i in liste1 if i not in liste2 ]
print(liste18)                   # / [1, 16, 49, 64]

liste19=[[1,2,3],[4,5,6,7],[8,9,10,11,12]]

# yukarıdaki listede elemanların tek olanlarından bir liste olşturalı.

# eski yöntem 

liste20=[]
for i in liste20:
    for j in i:
        liste20.append(j)

print(liste20)                      # / [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# yeni yöntem

liste21 = [j for i in liste19 for j in i]
print(liste21)                     # / [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]