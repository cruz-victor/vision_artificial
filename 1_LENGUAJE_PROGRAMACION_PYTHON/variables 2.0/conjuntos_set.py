#Su usan datos que no se mutan.
#En set usar tuplas, no listas ni diccionarios
set_one=set(["Dato 1","Dato 2"])
print(set_one)

set_two={"dato 1","dato 2"}
print(type(set_two))
print(set_two)

#Conjunto dentro de otro conjunto
set_three=frozenset(["dato 1", "dato 2"])
set_four={set_three, "dato 3"}
print(type(set_four))
print(set_four)

#Teoria de conjuntos
set_1={1,3,5,7}
set_2={1,3,7}

#result=set_2.issubset(set_1)
result=set_2 <= set_1
print(result)

# result=set_2.issuperset(set_1)
result=set_2>set_1
print(result)

result=set_2.isdisjoint(set_1)
print(result)
