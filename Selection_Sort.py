a=[2,54,56,12,23,334,43,6,8,2,53,7,82,21,12]


def indexOfSmallest(arr,i,num):
    min=arr[i]
    indexofmin=i
    
    for j in range(i+1,num):
        if (arr[j]<min):
            min=arr[j]
            indexofmin=j
            
    return indexofmin


def swapValues(v1,v2):
    v1,v2=v2,v1
    return v1, v2


def sort(arr,numUsed):
    print(arr)
    indexOfNextSmallest=0
    for i in range(numUsed-1):
        indexOfNextSmallest=indexOfSmallest(arr,i,numUsed)
        
        arr[i],arr[indexOfNextSmallest]=arr[indexOfNextSmallest],arr[i]
        
    return arr
        

new=sort(a,len(a))
print(new)




