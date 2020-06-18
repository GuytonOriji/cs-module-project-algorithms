'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

def single_number(arr):

    # Your code here
    # gathering the values that have duplicates then removing
    # them and then the only 1 left would be the answer to
    # this question XD
  
    from collections import Counter
     

    dict_arr = Counter(arr)
    print(dict_arr)
    result = [k for k, v in dict_arr.items() if v<2]
    print(result)
    print(type(result))  
    return result[0]    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")