def swap(lists,index1,index2):
    temp = lists[index1]
    lists[index1] = lists[index2]
    lists[index2] = temp

def pivot(lists,pivot_index,end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1,end_index+1):
        if lists[i] < lists[pivot_index]:
            swap_index += 1
            swap(lists,swap_index,i)
    swap(lists,pivot_index,swap_index)
    return swap_index

def quickSort(lists,left,right):
    if left < right:
        pivot_index = pivot(lists,left,right)
        quickSort(lists,left,pivot_index-1)
        quickSort(lists,pivot_index+1,right)
    return lists
        
print(quickSort([4,1,6,7,3,2,5],0,6))