import time
def partition(arr,low,high,create_lines,time_interval): 
    i = ( low-1 )        
    pivot = arr[high]     
    create_lines(arr,getcolor(len(arr),low,high,i,i))
    time.sleep(time_interval)
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            create_lines(arr,getcolor(len(arr),low,high,i,j,True))
            time.sleep(time_interval)
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
        create_lines(arr,getcolor(len(arr),low,high,i,high,True))
        time.sleep(time_interval)

    create_lines(arr,getcolor(len(arr),low,high,i,j,True))
    time.sleep(time_interval)
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high,create_lines,time_interval): 
    if low < high: 
        pi = partition(arr,low,high,create_lines,time_interval) 
        quickSort(arr, low, pi-1,create_lines,time_interval) 
        quickSort(arr, pi+1, high,create_lines,time_interval) 
    
def getcolor(datalen,low,high,i,curr,isSwapping=False):
    color=[]
    for j in range(datalen):
        if j>=low and j<=high:
            color.append("steel blue")
        else:
            color.append("sea green")
        if j==high:
            color[j]="indian red"
        elif j==i:
            color[j]="goldenrod"
        elif j==curr:
            color[j]="slate gray"
        
        if isSwapping:
            if j==i or j==curr:
                color[j]="coral1"
    return color