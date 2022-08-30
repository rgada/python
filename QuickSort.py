def partisan(arr,start,end):
    pivot_index = start
    while start < end:
        while start < len(arr) and arr[start] <= arr[pivot_index]:
            start += 1

        while arr[end] > arr[pivot_index]:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

def quick_sort(arr,start,end):
    if start < end:
        global count
        count += 1
        print(f"start: {start} end:{end}")
        pi = partisan(arr,start,end)
        #print(arr)
        quick_sort(arr,0,pi-1)   #left partisan
        print(f"left: {arr}")
        count += 1
        print(f"count: {count}")
        quick_sort(arr,pi+1,end) #right partisan
        print(f"right: {arr}")
        count += 1
        print(f"count: {count}")
    return arr

if __name__ == '__main__':
    count = 0
    #unsorted_arr = [11,3,10,-9,0,100,1,99,80]
    desc_arr = [9,8,7,6,5,4,3,2,1]
    print(quick_sort(desc_arr,0,len(desc_arr)-1))
    print(f"Final count: {count}")