def sort(l1):
    for i in range(5):  # descending order
       
        for j in range(i,6):
            if(l1[j] >l1[i]):
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp

l1 = [41,5413,52,6346,37,34]
sort(l1)
print(l1)

def sort(l1):  # ascending order
    for i in range(len(l1)):
        midpos = i
        for j in range(i+1,len(l1)):
            if(l1[j] < l1[midpos]):
                midpos = j
        temp = l1[i]
        l1[i] = l1[midpos]
        l1[midpos] = temp

l1 = [41,5413,52,6346,37,34]
sort(l1)
print(l1)

