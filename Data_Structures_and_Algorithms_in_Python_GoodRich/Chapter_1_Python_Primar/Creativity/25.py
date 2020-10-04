"""
C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""
def RemovePunctuation(str):
    strlist = list(str)
    print(strlist)
    for i in strlist:
        if i in [',','.','"',"'","!"]:
            strlist.remove(i)
    str = ''.join(strlist)
    print(str)
RemovePunctuation("Hello, There!")

