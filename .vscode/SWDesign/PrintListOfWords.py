# Example 1 - Common Design Mistakes

# Program Goal, print a list of words delimeted by commas

# Solution 1 - What's wrong?
list_of_words = ["hello", "yes", "goodbye", "last"]
# print(list_of_words[0] + ", " + list_of_words[1]+ ", " + list_of_words[2] + ", " + list_of_words[3])

# what if an element added or delimiter changed

# to_print = ""

# for i in range(len(list_of_words)-1) :
#     to_print += list_of_words[i] + ", "
# to_print += list_of_words[len(list_of_words)-1]

# print(to_print)


# Solution 3
print(",".join(list_of_words))


# Best solution
DELIMITER = ","
print(DELIMITER.join(list_of_words))