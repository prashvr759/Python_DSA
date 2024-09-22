
# O(N^2) time 
def bruteforce_3sum(s):

  for i in range(length(s)-1):
    for j in range(length(s)):






# O(N) time and O(N) space complexity
def three_sum(s,total_sum):

  first = 1
  second = first + 1
  last = length(s)-1
  triplet = []
  while first < last:
    triplet = s[first] + s[second] + s[last]
    if triplet == total_sum:
      return True
    elif triplet < first:
      first = first + 1
      second = second + 1
    elif triplet > last:
      last = last -1

  return True
  
def main():


if __name__ == '__main__':
    main()
