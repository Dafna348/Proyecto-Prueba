print("Bienvenidos al programa por favor dijite las notas a continuaci'on")
nota1 = int(input("Digite su primera nota: "))
nota2 = int(input("Digite su primera nota: "))
nota3 = int(input("Digite su primera nota: "))
if(nota1 ==70):
    print("Tienes derecho  a hacer ampliacion del curso debido a tu primera nota")
elif(nota1 <=60):
    print("Lo sentimos reprovaste el curso debido a tu primera nota")
else:
    print("Felicidades lograste pasar el curso con tu primera nota")
if(nota2 ==70):
    print("Tienes derecho  a hacer ampliacion del curso debido a tu segunda nota")
elif(nota2 <=60):
    print("Lo sentimos reprovaste el curso debido a tu segunda nota")
else:
    print("Felicidades lograste pasar el curso con tu segunda nota")

if(nota3 ==70):
    print("Tienes derecho  a hacer ampliacion del curso debido a tu tercer nota")
elif(nota3 <=60):
    print("Lo sentimos reprovaste el curso debido a tu tercera nota")
else:
    print("Felicidades lograste pasar el curso con tu tercer nota")