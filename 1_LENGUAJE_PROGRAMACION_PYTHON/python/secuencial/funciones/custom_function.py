#Funcion simple
def greetings():
    print("Hola victor cg")
    
greetings()

def greetings(name, gender):
    gender=gender.lower()
    if(gender=="mujer"):
        print(f"Hola Reyna {name} como estas")
    elif (gender=="hombre"):
        print(f"hola {name} como andas")

greetings("Juana","mujer")
greetings("Carlos","hombre")

def calculate_password(number):
    return number*10

password=calculate_password(10)
print(password)

def generate_fullname():
    first_name="Victor"
    last_name="Cruz"
    return first_name, last_name

name, last_name=generate_fullname()
print(f"Tu nombre es {name}")
print(f"Tu apellido es {last_name}")