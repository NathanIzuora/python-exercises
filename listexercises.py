
# even numbers
numbers1 = [1,3,4,7,9,6,7,]

def findEvenNumnbers (list):
    for r in list:
        if r % 2 == 0:
            print(r)

findEvenNumnbers(numbers1)

# largest numbers in list
largenumbers = [1,2,3,4,5,6,7]
largenumbers2 = [4,6,2,77,54]

def getlargenums (list):
    biggestnum = list [0]
    for x in (list):
        if x > biggestnum:
            biggestnum = x
    return biggestnum
print(getlargenums(largenumbers))


# largest number in list alternative
bigolnums = [1,2,5,7,8]
print(max(bigolnums))

