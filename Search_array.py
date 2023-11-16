arr=[1,2,3,4,5,6,7,8,9]

target=10

index=0
found=False
numberUsed=len(arr)

while ((found==False) and (index<numberUsed)):
    if (target==arr[index]):
        found=True
    else:
        index+=1
        
if found:
    print(index)
else:
    print('NO')




