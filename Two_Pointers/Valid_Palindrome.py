def valid_palindrome(input_array):
  first = 0
  last = len(input_array)-1

  while first < last:
    if input_array[first]!=input_array[last]:
      return false
      
    first = first+1
    last = last-1    

  return true
    
