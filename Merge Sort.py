
import re


def merge(list1, list2):
    i = 0
    j = 0
    combined = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
   
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def mergeSort(lists):
    if len(lists) == 1:
        return lists
    mid = int(len(lists)/2)
    left = lists[:mid]
    right = lists[mid:]
    return merge(mergeSort(left),mergeSort(right))

print(mergeSort([101,99,8,5,69,2,1,7,0,1]))