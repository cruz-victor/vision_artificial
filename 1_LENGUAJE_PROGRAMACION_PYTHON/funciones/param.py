def sum(a,b):
    return a+b

result=sum(10,15)
print(result)

def sum(list):
    total=0
    for number in list:
        total=total+number
    return total

result=sum([5,10,15])
print(result)

#El parametro multiple va como ultimo parametro
# def sum(*numbers):
#     return sum(numbers)

result=sum([5,10,1])
print(result)