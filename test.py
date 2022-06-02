from decimal import DivisionByZero


i = 322
while i <=10:
    print(i)
    i +=1
else:
    print('opps the i is now', i)


try:
    print(5/1)
except DivisionByZero as e:
    print(e)
else:
    print('inside else')