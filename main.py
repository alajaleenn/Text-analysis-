from collections import Counter
import string

print("add your book path:")
path=input()


#Reading the text book
with open(path,"r",encoding="utf-8") as book:
    content=book.read()

#Cleaning the data
words=content.split(" ")
words=[word.strip(string.punctuation).lower() for word in words if word.strip(string.punctuation)]


#Calculating number of words 
numOFwords=len(words)

#Searching for the unique words
uniqueWords=Counter(words)
topWords=uniqueWords.most_common(5)


print("--------Text Analysis Summary--------")
print("Number of words in the book: ",numOFwords)
print("Number of uniqe words: ",len(uniqueWords))
for word, count in topWords:
   print(f"word ({word})is repeted {count} times")

