#v2
def list_match(list_1, list_2):
'''
count already has a starting value
'''
   count = 1
   for i in range(len(list_1)):
      if list_1[i] == list_2[i]:
         count += 1
   return count
