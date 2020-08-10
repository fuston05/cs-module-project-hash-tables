def no_dups(s):
    dupLess= {}
    # split s into a list of separated words
    s= s.split()

    # loop through list using 'enumerate' for index access, add words to dict to remove dups.
    for i, word in enumerate(s):
        # maintain original order???
        # store them in the dict with their original index as the val???
        if word not in dupLess:
            dupLess[word]= i
    
    results= []
    # loop over dict:
    for k, _ in dupLess.items():
        #push to results list
        results.append(k)
    # join back to a string,
    # strip whitespace
    newStr= ', '
    newStr= newStr.join(results).strip()

    return newStr


if __name__ == "__main__":
    # print('')
    # print(no_dups(""))
    # print('')
    # print(no_dups("hello"))
    # print('')
    # print(no_dups("hello hello"))
    # print('')
    # print(no_dups("cats dogs fish cats dogs"))
    print('')
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
    print('')