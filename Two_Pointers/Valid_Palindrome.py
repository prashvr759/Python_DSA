def valid_palindrome(input_array):
  first = 0
  last = len(input_array)-1

  while first < last:
    if len(input_array)=1:
      return false

    if input_array[first]==input_array[last]:
      first = first++
      last = last--
    else
      return false

return true
    
