def match_words(words):
  ctr = 0
  lst = []
  for word in words:
   if len(words) > 1 and word[0] == word[-1]:
    ctr += 1
    lst.append(word)
   print("List of word with first and last character same \n")
   return ctr
count = match_words(['NAMAN','1221','Gincy'])
print("Number of word with first and last character same:" , count)