nom = input("Escriba su nombre: ")
apellido = input ("Escriba su apellido: " )
edad = int( input("Digite su edad:  "))
print("Bienvenido, tu objetivo es adivinar el numero secreto")
numerosecreto = float(input("Digite el numero que cree ser correcto "))
if(numerosecreto==110):
    print("Felicitaciones ",nom, apellido,"lograste adivinar el numero secreto, que suerte tienes")
elif(numerosecreto > 110):
    print("Lo lamento", nom, apellido,  " No lograste adivinar el numero intentalo otra vez, a lo mejor la suerte si esta de tu lado esta vez") 
elif (numerosecreto < 110):
    print("Lo lamento", nom, apellido,  " No lograste adivinar el numero intentalo otra vez, a lo mejor la suerte si esta de tu lado esta vez")  