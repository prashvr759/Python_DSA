
# O(N^2) time 
def bruteforce_3sum(s):

  for i in range(length(s)-1):
    for j in range(length(s)):






# O(N) time and O(N) space complexity
def three_sum(s,total_sum):
  s.sort()
  
  for i in range(len(s)-2):
    second = i + 1
    last = len(s)-1
    
    while first < last:
      triplet = s[i] + s[second] + s[last]
      if triplet == total_sum:
        return True
      elif triplet < target:
        first = first + 1
      else:
        last = last -1

  return True
  
def main():
  s  = [1,4,8,3,20,6]
  target = 13
  three_sum(s,target)
  


if __name__ == '__main__':
    main()
