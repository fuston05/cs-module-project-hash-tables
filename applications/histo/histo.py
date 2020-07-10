# Your code here
cache= {}
def histoCreator(fileName):
  ignoredChars = {"?": None, "!": None, "\"": None, ":": None, ";": None, ",": None, ".": None, "-": None, "+": None, "=": None, "/": None, "\\": None, "|": None, "[": None, "]": None, "{": None, "}": None, "(": None, ")": None, "*": None, "^": None, "&": None}

  # open end read file
  with open(fileName, 'r') as file:
    file.readlines()
 


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