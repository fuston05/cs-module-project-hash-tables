# Your code here
cache = {}


def histoCreator(fileName):
  ignoredChars = {"?": None, "!": None, "\"": None, ":": None, ";": None, ",": None, ".": None, "-": None, "+": None, "=": None,
      "/": None, "\\": None, "|": None, "[": None, "]": None, "{": None, "}": None, "(": None, ")": None, "*": None, "^": None, "&": None}

  # open end read file
  with open(fileName, 'r') as file:
    f = file.read()
    f = f.lower()

    # remove special chars
    ignoredCount= 0
    for i in f:
      if i in ignoredChars:
        f = f.replace(i, '')
        ignoredCount+= 1
    # if there are no ignored chars found then don't return anything. per/instructions
    if ignoredCount == 0:
      return None

    # split into a list of words
    words = f.split()

    # count words and add to cache
    wordCount = 0
    for i in range(len(words)-1):
      # if not in cahce add it or increment it's count
      if words[i] not in cache:
        cache[words[i]] = 1
      else:
        cache[words[i]] += 1
      wordCount += 1

    # get a type that we can sort: list of tuples
    pairs= []
    for k, v in cache.items():
      pairs.append((k,v))
      
    # sort cache by word count reversed, then alphabetically
    pairs= sorted(pairs, key= lambda x: (-x[1], x[0]))

    # find longest word for spacing purposes
    longestWord= 0
    for i in pairs:
      if len(i[0]) > longestWord:
        longestWord= len(i[0])
    


    # build our output:
    for i in pairs:
      # calc spaces
      space= longestWord + (longestWord - len(i[0]))- longestWord +2
      print(i[0] + space*' ' + '#' * i[1])




    # print('f type: ', type(f))
    # print('')
    # print(f)
    # print('cahce: ', cache['in'][1])
    # print('')
    # print('pairs: ', pairs)



    # print('cache: ', cache)

    # print('cache: ', cache)
    # return cache

  # loop through file against ignoredChars
    # remove all special chars:
      # " : ; , . - + = / \ | [ ] { } ( ) * ^ &

  # lowercase all words

  # split file into words list
  # loop through our list
    # add word count to cache
print(histoCreator('robin.txt'))
