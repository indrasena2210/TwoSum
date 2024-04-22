string = input("Enter the String: ").split()

reversed_str = ""

# METHOD 1 Using step Indexing

# for word in string:
#     reversed_word = word[::-1]
#     reversed_str =  reversed_word + " " + reversed_str
# print(reversed_str)


#Method 2 reversing a word using loop


for word in string:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    # print("reversed_word: ",reversed_word)
    reversed_str = reversed_word + " " + reversed_str
print("reversed_str ",reversed_str)