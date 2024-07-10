#Lambda es una funcion anonima
multiple_per_two= lambda x:x*2;
print(multiple_per_two(5))

numbers=[1,2,3,4,5,6,7,8,9]

def is_pair(number):
    if(number%2 == 0):
        return True
    
# pair_numbers=filter(is_pair, numbers)
# print(list(pair_numbers))

pair_numbers=filter(lambda number:number%2==0 , numbers)
print(list(pair_numbers))