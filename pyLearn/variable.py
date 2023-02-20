#!/usr/bin/python

x = 5
y = 10
def _sum(x, y=10):
    sum = x + y
    return sum

# print(_sum(2))

## String
def play_String():
    import time
    str = 'Hello World!'
    print("LEN", len(str)," ")
    time.sleep(1)
    print(str[1])
    for e in str:
        print(e)
        time.sleep(2)
# play_String();

## LIST

def playList():
    list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
    print(list[1:-1])
# playList();

def playListLoop():
    list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
    listLen = len(list)
    i = 0
    while i < listLen:
        print(list[i])
        i = i+1

# playListLoop();

## Remove duplicate Element
def playListRemoveDuplicate():
    list = [ 'abcd', 786 , 786 , 2.23, 'john', 70.2, 'abcd']
    listLen = len(list)
    listArr = []
    listDupArr = []
    i = 0
    while i < listLen:
        if list[i] not in listArr:
            listArr.append(list[i])
        else:
            listDupArr.append(list[i])
        i = i+1

    print(listArr)
    print(listDupArr)

# playDic And count
def playDictionary():
    dict = {}
    list = [ 'abcd', 786 , 786 , 2.23, 'john', 70.2, 'abcd']
    listLen = len(list)
    listArr = []
    listDupArr = []
    i = 0
    while i < listLen:
        if list[i] not in listArr:
            dict[list[i]] = 1
            listArr.append(list[i])
        else:
            dict[list[i]] = dict[list[i]] + 1
            listDupArr.append(list[i])
        i = i+1

    print(listArr)
    print(listDupArr)
    print(dict)
    print(dict.keys().mapping)

playDictionary()