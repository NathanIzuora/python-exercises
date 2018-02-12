# loop 1 to 10 
for n in range(1,11):
    # n += 1
   print('all nums 1 to 10:', n)

# n to m
m = int(input('start num? '))
n = int(input('end num? '))
for b in range(m,n+1):
   print('M to N ', b)

# print odd numbers


for r in range(1,11):
    if r % 2 != 0:
        print(r)

# creating a box
for i in range(0,5):
    for j in range(0,5):
        print("*" , end = " ")
    print(i)



