'''
Input: a List of integers
Returns: a List of integers
'''



def moving_zeroes(arr):
    zerovalue_item =0
      
    for i in range(len(arr)):
        # remove zero value items and append them at the end
        if arr[i]==zerovalue_item:       
            arr.remove(zerovalue_item)
            print(len(arr))
            arr.append(zerovalue_item)        
            print(arr)
           # if there are not any , return array             
        else:
            print(arr)                 
            
    return arr

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]


    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")