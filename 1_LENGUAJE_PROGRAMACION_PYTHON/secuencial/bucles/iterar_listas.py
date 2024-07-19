#Funciona con listas
# animals=["dog", "cat","pig","eagle"]
# numbers=[10,20,30,40]

#Funciona con tuplas
animals=("dog", "cat","pig","eagle")
numbers=(10,20,30,40)

# for animal in animals:
#     print(animal)

for num in numbers:
    print(num)
       
for animal,number  in  zip(animals, numbers):    
    print(f"recorriendo lista 1: {animal}")
    print(f"recorriendo lista 2: {numbers}")
    
for num in range(5):
    print(num)
    
for num in range(len(numbers)):
    print(numbers[num])

for num in enumerate(numbers):
    index=num[0]
    value=num[1]
    print(f'El indice es: {index} y el valor es: {value}')
    

