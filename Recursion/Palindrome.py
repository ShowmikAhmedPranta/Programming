def is_palindrome(A,low,high):
    if(low>high):
        return True   
    else:
        if(A[low] != A[high]):
            return False
        else:
            return is_palindrome(A,low+1,high-1)
        
            
