# Description
# In a certain encrypted message which has information about the location(area, city), the characters are jumbled such that
# first character of the first word is followed by the first character of the second word, then it is followed by
# second character of the first word and so on

# In other words, let’s say the location is bandra,mumbai
# The encrypted message says ‘bmaunmdbraai’.

# Sample Input:   bmaunmdbraai
# Sample Output:  bandra,mumbai

# Let’s say the size or length of the two words wouldn’t match then the smaller word is appended with # and then encrypted in the above format.

# With this in mind write a code to identify the right location and print it as place,city.
# area = ""
# city = ""
# counter = len(text)
# print("count of string is: {0}".format(counter))
# print("entered string is: " + text)
# if counter % 2 == 0:
#     print("YAY !! Your entered area and city have same number of characters.")
#     for x in range(counter):
#         if x % 2 == 0:
#             area = area + text[x]
#         else:
#             city = city + text[x]
# else:
#     print("HEY !! Your entered area and city do not have same number of characters.")

# print("Entered area is:" + area)
# print("Entered city is:" + city)
# print("" + area + "," + city)
# Type your code here
# print(message1, message2)
