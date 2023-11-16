a=[2,54,56,12,23,334,43,6,8,2,53,7,82,21,12]

def bubbelsort(arr):
    length=len(arr)
    
    for i in range(length-1,0,-1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return arr
    
print(bubbelsort(a))