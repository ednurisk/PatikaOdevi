#Binary Search Tree Projesi

dizi=[7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
#Yukarı verilen dizinin Binary-Search-Tree aşamalarını yazınız.
#İlk eleman 7'yi kök düğüm olarak alırız.
#Daha sonra 5'i ekleriz. 5, 7'den küçük olduğu için 7'nin soluna eklenir.
#Sonraki eleman 1'dir. 1, 7'den küçük, 5'ten de küçüktür. Bu yüzden 1, 5'in soluna eklenir.
#Sonraki eleman 8'dir. 8, 7'den büyük olduğu için 7'nin sağına eklenir.
#3 elemanı eklenir. 3, 7'den küçük, 5'ten küçük ancak 1'den büyüktür. Yani 3, 1'in sağında yer alır.
#6 elemanı eklenir. 6, 7'den küçük, 5'ten büyük olduğu için 5'in sağına eklenir.
#0 elemanı eklenir. 0, 7'den, 5'ten, 1'den küçük olduğu için 1'in soluna eklenir.
#9 elemanı eklenir. 9, 7'den büyük, 8'den de büyük olduğu için 8'in sağına eklenir.
#4 elemanı eklenir. 4, 7'den küçük, 5'ten küçük, ancak 3'ten büyük olduğu için 3'ün sağında yer alır.
#Son olarak 2 elemanı eklenir. 2, 7'den küçük, 5'ten küçük, 1'den büyük ancak 3'ten küçük olduğu için 3'ün soluna eklenir.

'''
        7
       / \
      5   8
     / \    \
    1   6    9
   / \
  0   3
     / \
    2   4
'''