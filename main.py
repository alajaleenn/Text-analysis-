from collections import Counter
import string
from docx import Document


print("what is your file type? .txt or .docx or .pdf?")
filetype=input().strip()

if filetype == ".docx" or filetype == ".txt":
  print("add your book path:")
  path=input().strip()

#Reading the text book
  if filetype==".txt":
    with open(path,"r",encoding="utf-8") as book:
      content=book.read()
  elif filetype==".docx":
    doc=Document(path)
    paragraphs=doc.paragraphs
    content="\n".join([p.text for p in paragraphs])



#Calculating number of sentences 
  sentences= content.split(".")
  sentences=[s.strip() for s in sentences if s.strip()]
  numOfSentences=len(sentences)

#Cleaning the data
  words=content.split()
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
else:
    print("Unsupported file type")