def arithmetic_arranger(problems,display):
    #Variables a usar
    separados = []
    resultados= []
    #checkear errores
    if len(problems) > 5:
        #máximo de 5 problemas
        print("Error: Too many problems")
        exit()

    for operaciones in problems:
        #separar por espacio y agrego a una lista con valores
        separados.append(operaciones.split(' '))

        #unzip valores 3 variables: primero, operador, segundo
        primero, operador, segundo = zip(*separados)
    #check: son enteros?
    for i in primero:
        #print(f'Conversion {i}')
        try:
            int(i)
        except:
            print("Error: Numbers must only contain digits.")
            exit()
        if len(i)>4:
            print("Error: Numbers cannot be more than four digits.")
            exit()

    for i in segundo:
        #print(f'Conversion {i}')
        try:
            int(i)
        except:
            print("Error: Numbers must only contain digits.")
            exit()
        if len(i)>4:
            print("Error: Numbers cannot be more than four digits.")
            exit()

    #check: operadores + o -
    #hacer la suma
    for i in separados:
        print(f'operacion: {i}')
        if i[1] =='+':
            suma = str(int(i[0]) +int(i[2]))
            resultados.append(suma)

        elif i[1] =='-':
            resta = str(int(i[0]) +int(i[2]))
            resultados.append(resta)
        else:
            print("Error: Operator must be '+' or '-'")
            exit()
    print(f'Resultados:  {resultados}')

   #When the second argument is set to True, the answers should be displayed.
    if display is True:
        #print de prueba
        print(f'separados: {separados}')
        print(f'Separado 1: {separados[1]}')
        """print(separados[1][0])
        print(primero)
        print(segundo)
        print(operador)"""

        #print correctos
        #establecer un separador: 4 espacios entre cada columna y luego la diferencia entre el máximo de caracteres
        for i in separados:
            print(max(len(i[0]),len(i[2])))


    else: print(f'Operación realizada pero no se muestra resultado')

#    return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)