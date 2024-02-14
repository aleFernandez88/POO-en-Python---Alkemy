def verificar_calificacion(nota1,nota2,nota3):
    prom= (nota1+nota2+nota3)/3
    if(prom>6):
        resultado = "Aprobado"
    else:
        resultado="Reprobado"
    # prom = nota1+nota2+nota3/3
    # if (prom>6):
    #   resultado ="Aprobado"
    # else : 
    #   resultado="Reprobado"
    return resultado

n1 = int(input("ingrese la nota 1: "))
n2 = int(input("ingrese la nota 2: "))
n3 = int(input("ingrese la nota 3: "))

# print(verificar_calificacion(n1,n2,n3)) 

