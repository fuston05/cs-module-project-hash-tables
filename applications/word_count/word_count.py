
def word_count(s):
    ignoredChars = [
        "?", "!", "\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"
    ]

    countedWords = {}

    s = s.lower()

    # check for special chars and remove,
    ignoredCount = 0
    for i in s:
        for c in ignoredChars:
            if i == c:
                ignoredCount += 1
                s = s.replace(i, '')

    # if no special chars return NONE
    if ignoredCount == 0 and len(s) == 0:
        return {}

    # build look-up table
    word_list = s.split()
    for word in word_list:
        if word not in countedWords:
            countedWords[word] = 1
        else:
            countedWords[word] += 1

    return countedWords


if __name__ == "__main__":
    print('')
    # print(word_count(""))
    print('')
    # print(word_count("Hello    hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print('')
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print('')
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print('')
