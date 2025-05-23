def sort(l1):
    for i in range(len(l1)-1 , 0 , -1):
        for j in range(i):
            if l1[j] > l1[j+1]:
                temp = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = temp

l1 = [2,314,13,5,315,13]
sort(l1)
print(l1)







    