dictionary={
    "name":"Victor",
    "last_name":"Cruz",
    "age":"39"
}

for data in dictionary.items():
    key = data[0]
    value=data[1]
    print(f"la clave es: {key} y el valor es: {value}")
    
    
    
fruits=["banana","manzana","mandarina","pera"]

for fruit in fruits:
    if fruit=='mandarina':
        continue
    print(f"Me voy a comer una {fruit}")
print("Bucle terminado")
    
for fruit in fruits:
    if fruit=='manzana':
        break
    print(f"Me voy a comer una {fruit}")
print("Bucle terminado")

name="Victor Cruz"
for character in name:
    print(character)
print("Bucle terminado")

numbers=[5,2,4,5,2,1]
for number in numbers:
    print(number)
print("Bucle terminado")

duplicates_numbers=[x*2 for x in numbers]
print(duplicates_numbers)
print("Bucle terminado")
