##### python simple classes task
#task1

##given a string and a non-negative int n, return a larger string that is n copies of the original string.




class string_times:
    def st_times(self,str,n):
       result = ""
       for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
            result = result + str  # could use += here
       return result


z=string_times()
print(z.st_times('hi',2))
print(z.st_times('hi',1))
print(z.st_times('hi',3))





#given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever 
# is there if the string is less than length 3. Return n copies of the front
class front_times:
    def front_times_n(self,str,n):
        front_len = 3
        if front_len > len(str):
            front_len = len(str)
        front = str[:front_len]
        result = ""
        for i in range(n):
              result = result + front
        return result 

z=front_times()
print(z.front_times_n('Chocolate',2))
print(z.front_times_n('chocolate',3))
print(z.front_times_n('ABC',3))

class only_even_chr:
 def string_bits(self,str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result


z=only_even_chr()
print(z.string_bits('Hello'))
print(z.string_bits('Hi'))
print(z.string_bits('Heeololeo'))
  
###given a non-empty string like "Code" return a string like "CCoCodCode".

class repition:
    def string_splosion(self,str):
      result = ""
      for i in range(len(str)):
          result = result + str[:i+1]
      return result
  
z=repition()
print(z.string_splosion('Code'))
print(z.string_splosion('abc'))
print(z.string_splosion('ab'))


##given a string, return the count of the number of times that a substring length 2 appears
#  in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1
#  (we won't count the end substring).

class last_Str:
    def last2(self,str):
      if len(str) < 2:
        return 0
      last2 = str[len(str)-2:]
      count = 0
  # Check each substring length 2 starting at i
      for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
         count = count + 1
      return count
z=last_Str()
print(z.last2('hixxhi'))
print(z.last2('xaxxaxaxx'))
print(z.last2('axxxaaxx'))

####given an array of ints, return the number of 9's in the array.

class count_list:
  def array_count9(self,nums):
    count = 0
  # Standard loop to look at each value
    for num in nums:
      if num == 9:
        count = count + 1
    return count
  
z=count_list()
print(z.array_count9([1,2,9]))
print(z.array_count9([1,9,9]))
print(z.array_count9([1,9,9,3,9]))

###Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

class array:
    def array_front9(self,nums):
      end = len(nums)
      if end > 4:
        end = 4
      for i in range(end):  # loop over index [0, 1, 2, 3]
        if nums[i] == 9:
          return True
      return False

z=array()
print(z.array_front9([1,2,9,3,4]))
print(z.array_front9([1,2,3,4,9]))
print(z.array_front9([1,2,3,4,5]))

##Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

class sequence:
    def array123(self,nums):
   # Note: iterate with length-2, so can use i+1 and i+2 in the loop
       for i in range(len(nums)-2):
         if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
       return False
  
z=sequence()
print(z.array123([1,1,2,3,1]))
print(z.array123([1,1,2,4,1]))
print(z.array123([1,2,1,2,3]))



#Given 2 strings, a and b, return the number of the positions 
# where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings
#  appear in the same place in both strings.


class string_match:
    def matching(self,a,b):
        shorter=min(len(a),len(b))
        count=0
        for i in range(shorter-1):
            a_sub=a[i:i+1]
            print(a_sub)
            b_sub=b[i:i+1]
            print(b_sub)
            if a_sub==b_sub:
                count=count+1
        return count

z=string_match()
print(z.matching('xxcaazz','xxbazz'))
print(z.matching('abc','abc'))

