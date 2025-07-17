from collections import Counter
import string

print("add your book path:")
path=input()


#Reading the text book
with open(path,"r",encoding="utf-8") as book:
    content=book.read()


#Calculating number of sentences 
sentences= content.split(".")
sentences=[s.strip() for s in sentences if s.strip()]
numOfSentences=len(sentences)

#Cleaning the data
words=content.split(" ")
words=[word.strip(string.punctuation).lower() for word in words if word.strip(string.punctuation)]


#Calculating number of words 
numOFwords=len(words)



#average number of words in a sentence 
average=round(numOFwords/numOfSentences)

#Searching for the unique words
uniqueWords=Counter(words)
topWords=uniqueWords.most_common(5)


print("--------Text Analysis Summary--------")
print("Number of words in the book: ",numOFwords)
print("Average number of words per sentence: ",average)
print("Number of uniqe words: ",len(uniqueWords))
print("Top 5 words repeted: ")
for word, count in topWords:
   print(f" ({word}) is repeted {count} times")

