#Generar los n primeros numeros primos

def is_prime_number(number):
    for i in range (2, number-1):
        if number%i==0: return False
    return True;

def get_list_of_prime_numbers(quantity_of_numbers):
    prime_numbers=[]
    for i in range(2,quantity_of_numbers+1):
        if is_prime_number(i): prime_numbers.append(i)
    return prime_numbers        
        
print(is_prime_number(8))
prime_numbers=get_list_of_prime_numbers(10)
print(type(prime_numbers))
print(prime_numbers)