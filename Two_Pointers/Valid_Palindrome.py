# O(N^2) Time
def bruteforce_valid_palindrome(input_array):

  



# O(N) Time & O(1) Space Complexity Solution. However, our algorithm will only run (n/2) times, since two pointers are traversing toward each other.
def valid_palindrome(input_array):
  first = 0
  last = len(input_array)-1

  while first < last:
    if input_array[first]!=input_array[last]:
      return false
      
    first = first+1
    last = last-1    

  return true

# Driver Code
def main():

    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):        
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("\nIs it a palindrome?.....", is_palindrome(test_cases[i]))

if __name__ == '__main__':
    main()
