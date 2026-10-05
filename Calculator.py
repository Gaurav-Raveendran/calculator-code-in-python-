print("Hello")
print("input your numbers")
m=int(input("enter no of nos:"))
numbers=[]
for i in range(m):
    k=float(input("enter numbers:"))
    numbers.append(k)
print('''1=+
2=-
3=/
4=*''')
c=int(input("choose a function:"))
if c==1:
    total=sum(numbers)
    print(total)
elif c==2:
    total=numbers[0]
    for num in numbers[1:]:
        total-=num
    print(total)
elif c==3:
    total=numbers[0]
    try:
      for num in numbers[1:]:
          total/=num
      print(total)
    except ZeroDivisionError:
      print("cannot divide by zero")
elif c==4:
    total=numbers[0]
    for num in numbers[1:]:
        total*=num
    print(total)
else:
    print("the operation numbers only exist between 1-4")
