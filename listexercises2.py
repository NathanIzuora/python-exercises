# largest numbers in list

thesenums = [1,2,3,4,66]
print(max(thesenums))

#sum of numbers list
thosenumbs = [1,2,4,65,22]
print(sum(thosenumbs))

#smallest numbers in list
othernums = [3,4,6,8,9,90]
print(min(othernums))

# even numbers in list
mynumbers = [2,4,5,6,7,8]
def iwantevennum (thislist):
    for n in thislist:
        if n % 2 == 0:
            print(n)
iwantevennum(mynumbers)

# multiply a list by a number
# listformulti = [1,4,6,5,3,7]
# listformulti[:] = [n * 5 for n in listformulti]
# print(listformulti)

listformulti = [1,4,6,5,3,7]
newlist = []
for n in listformulti:
    newlist.append(n * 5)
print(newlist)



# multiply two lists together
list1 = [2,4,5,3,7]
list2 = [4,7,6,8,9]
list3 = [0,0,0,0,0]

for n in range(0,len(list1)):
    list3[n] = list1[n] * list2[n]

print(list3)

# add two lists together

add1 = [2,5,3]
add2 = [5,5,7]
sum3 = [0,0,0]
for n in range(0,len(add1)):
    sum3[n] = ( add1[n] + add2[n])
print(sum3)

# use sum3 and apply it to two other matrices (matrix)
adding3 = [1,1,1]
adding4 = [3,5,4]
for n in range(0,len(adding3)):
    adding3[n] = adding3[n] + sum3[n]
    adding4[n] = adding4[n] + sum3[n]
print(adding3)
print(adding4)

# remove multiples of same number in list
numbers = [3, 5, 9, 0, 1, 5, 9, 3]
newlist = []

for nums in numbers:
    if nums not in newlist:
        newlist.append(nums)
# newlist.sort()
print(newlist)

#print(set(n))
# print(newlist)

# for n in igotalist:
#    igotalist = pop.(.index(n)igotalist.index(n))



