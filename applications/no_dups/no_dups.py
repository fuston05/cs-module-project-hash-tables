def no_dups(s):
  # short on time, so i took the fast way for now
  # Your code here
  newStr= ''
  if s == '':
    return ""
  s= s.split()
  s= set(s)
  for i in s:
    newStr+= i+' '
  return newStr.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))