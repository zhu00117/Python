#String Formatting

# principle = 598.36
# ratio = 9.678
# interest = principle * ratio

# print(f"The interest is {interest:.2f}")

# sentence = "It's raining cats and cats"
# # # print (sentence.endswith("cats"))

# # print(sentence.index("cats"))

# print(type(sentence))

# sentence = ("It","is","a","sentence")

# print(type(sentence))


# sentence = ["It","is","a","sentence"]

# print(type(sentence))

# sentence.pop(3)

# print(sentence)

# sentence.append("sentence")

# print(sentence)

# sentence[3]="change"

# print(sentence)

# sentence.insert(3,"new")

# print(sentence)

# def skip_elements(elements):	
# 	# for element in elements:
# 	# 	return elements[::2]
# 	ele = list(enumerate(elements))
   
# 	for index, element in ele:

# 	    print(index,element)


# skip_elements(["a", "b", "c", "d", "e", "f", "g"])

# def skip_elements(elements):
#    
#     for element in elements:
# 	 return elements[::2]

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# def skip_elements(elements):
#     mylist = []
#     for index, element in enumerate(elements):
#         if index%2 == 0:
#             mylist.append(element)
#     return mylist

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
 
def count_letters(text):
  result = {}
  # Go through each letter in the text
  letters= []
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
        letters.append(letter.lower())
#   print(letters)
  for key in letters:
    if key not in result:
       result.update({key:0})
    #    print(result)
  
    # result[key]=letters.count(key)
      
    result[key]+=1
    # Add or increment the value in the dictionary
    
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
    