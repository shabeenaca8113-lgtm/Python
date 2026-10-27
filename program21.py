words=input("Enter words separated by spaces:").split()
longest_word=max(words,key=len)
print("Length of the longest word:",len(longest_word))
