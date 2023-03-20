#An anagram is a word or phrase formed by rearranging the letters of

# a different word or phrase. In other words, both strings must contain

# the same exact letters in the same exact frequency.



# Write a python script that reads 2 strings from command line and finds

# out whether they are anagrams or not.

# If they are not anagrams, then the script should find and print the

# minimum number of character deletions required to make the two strings

# anagrams. Otherwise, just print that they are anagrams.



# **Input Format**



# - The first line contains a single string, **a**.

# - The second line contains a single string, **b**.



# Expected input and output:

# ```

# $ python3 solution.py

# a: Tom Marvolo Riddle

# b: I Am Lord Voldemort

# remove 7 characters from 'Tom Marvolo Riddle' and 8 characters from 'I Am Lord Voldemort'



# $ python3 solution.py

# a: tom marvolo riddle

# b: i am lord voldemort

# remove 0 characters from 'tom marvolo riddle' and 1 characters from 'i am lord voldemort'



# $ python3 solution.py

# a: tom marvolo riddle

# b: i am lordvoldemort

# they are anagrams



# $ python3 solution.py

# a: tom riddle

# b: voldemort

# remove 3 characters from 'tom riddle' and 2 characters from 'voldemort'

# ```
input_a = str(input("a: "))#get inputs
input_b = str(input("b: "))
dict_a = {}#init dicts
dict_b = {}
count_a = 0
count_b = 0
for char in input_a:
  dict_a[char] = dict_a.get(char, 0) + 1#fill dicts
for charr in input_b:
  dict_b[charr] = dict_b.get(charr, 0) + 1
d1_keys = set(dict_a.keys())#get keys into sets
d2_keys = set(dict_b.keys())
count_a = len(d1_keys - d2_keys)#number of different keys in keys of a wrt b
count_b = len(d2_keys - d1_keys)#number of different keys in keys of b wrt a
d_keys_removed = d1_keys - (d1_keys - d2_keys)#keys that exist in both dicts

for remaining in d_keys_removed:#trying to find if those keys have same numbered values
  a = dict_a[remaining]
  b = dict_b[remaining]
  if(a!=b):
    if(a > b): #if value exists more in a
      count_a = count_a + 1 #should be removed from a
    else:
      count_b = count_b + 1 #if more in b remove from b
if(count_a == 0 and count_b == 0):#if there hasn't been a difference found
  print("they are anagrams")    
else:
  print("remove " + str(count_a )+" characters from '"+ input_a + "' and " + str(count_b) +" characters from '"+ input_b + "'")