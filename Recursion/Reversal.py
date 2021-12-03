def reversal(arr, start, stop):
    if(start>=stop):
        return arr
    else:
        arr[start], arr[stop] = arr[stop], arr[start]
        return reversal(arr, start+1, stop-1)