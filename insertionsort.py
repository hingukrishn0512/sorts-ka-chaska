def insertionsort(l1):

    for i in range(1,len(l1)):
        sortnumber = l1[i]
   #using swap case
        while l1[i-1] > sortnumber and i>0:
            l1[i] , l1[i-1] = l1[i-1] , l1[i]
            i = i-1


l1 = [24,124,135,246,63,67,4,1,42]

insertionsort(l1)
print(l1)




