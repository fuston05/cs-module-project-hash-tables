
def word_count(s):
    countedWords= {}
    # Your code here
    bannedChars = {"\"": None, ":": None, ";": None, ",": None, ".": None, "-": None, "+": None, "=": None, "/": None, "\\": None, "|": None, "[": None, "]": None, "{": None, "}": None, "(": None, ")": None, "*": None, "^": None, "&": None}
    s= s.lower().strip()
    for letter in s:
        if letter in bannedChars:
            s= s.replace(letter, '')
    s= s.split()

    for word in s:
      if word not in countedWords:
        countedWords[word]= 1
      else:
        countedWords[word] +=1

    return countedWords


if __name__ == "__main__":
    print('')
    # print(word_count(""))
    print('')
    # print(word_count("Hello    hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print('')
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print('')
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print('')
