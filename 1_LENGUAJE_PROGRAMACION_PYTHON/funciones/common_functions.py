def phrase(name, last_name, adjetive="inteligente"):
    return f"Hola {name} {last_name} eres un {adjetive}"

result_phase=phrase("Victor", "Cruz", "Capo")
print(result_phase)

result_phase=phrase(adjetive= "Capisicmo", name="Victor", last_name="Quintanilla")
print(result_phase)

result_phase=phrase(name="Victor", last_name="Quintanilla")
print(result_phase)