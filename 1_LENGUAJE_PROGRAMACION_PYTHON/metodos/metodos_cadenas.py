cadena_1="Hola soy Victor"
cadena_2="Bienvendio crack"
cadena_3="Hola,soy,Victor"

# print(dir(cadena_1))
# print(dir(4))

result=cadena_1.upper()
result=cadena_1.lower()

first_letter_upper=cadena_1.capitalize()


find_word=cadena_1.find("a")

#Index lanza una excepcion si no encuentra el texto
index_word=cadena_1.index("a")

is_numeric=cadena_1.isnumeric()
is_alfnumeric=cadena_1.isalpha()

count_similars=cadena_1.count("o")

count_characters=len(cadena_1)

start_with=cadena_1.startswith("Ho")
end_with=cadena_1.endswith("do")

new_string=cadena_1.replace("Hola","Hola universo")
split_string=cadena_3.split(",")


# print(result)
# print(first_letter_upper)
# print(find_word)
# print(index_word)
# print(is_numeric)
# print(is_alfnumeric)
# print(count_similars)
# print(count_characters)
# print(start_with)
# print(end_with)
# print(new_string)
print(split_string)
print(split_string[0])
print(type(split_string))





