def arithmetic_arranger(problems,est = False):
    # Variables a usar
    todos = []  # todos los listados
    resultados = []
    primero = []
    segundo = []
    operador = []
    longitud = []
    relleno = " "
    check2 = "Error: Operator must be '+' or '-'."
    # check1 :5 problemas
    if len(problems) > 5:
        # máximo de 5 problemas
        return "Error: Too many problems."

    for k in problems:
        # separar por espacio y agrego a una lista con valores
        oper = k.split(' ')
        primero.append(oper[0])
        segundo.append(oper[2])
        operador.append(oper[1])
    #agrego a un conjunto
    def conjunto(listado):
        return todos.append(listado)
    # obtengo todos los primeros términos de cada operación
    conjunto(primero)
    conjunto(operador)
    conjunto(segundo)
    # print(todos)
    toditos = list(zip(primero, operador, segundo))
    # print(toditos)
    for i in operador:
        # check2: operadores + o -
        if i == "+":
            pass
        elif i == "-":
            pass
        else:
            #arranged_problems = print(check2)
            #print("Error: Operator must be '+' or '-'.")
            return "Error: Operator must be '+' or '-'."
    # check4: hasta 4 digitos
    def largo (entrada):
        if len(entrada) > 4:
            #arranged_problems = print('Error: Numbers cannot be more than four digits.')
            return 'Error: Numbers cannot be more than four digits.'
    for i in toditos:
        # check4: hasta 4 digitos
        if len(i[0]) > 4:
            #arranged_problems = print('Error: Numbers cannot be more than four digits.')
            #print('Error: Numbers cannot be more than four digits.')
            return 'Error: Numbers cannot be more than four digits.'
        if len(i[2]) > 4:
            #arranged_problems = print('Error: Numbers cannot be more than four digits.')
            #print('Error: Numbers cannot be more than four digits.')
            return 'Error: Numbers cannot be more than four digits.'
        #check enteros a cada valores
        try:
            a = int(i[0])
            b = int(i[2])
        except:
            #arranged_problems = print('Error: Numbers must only contain digits.')
            #exit()
            return 'Error: Numbers must only contain digits.'
        # check2: operadores + o - y hace la operatoria
        if i[1] == '+':
            suma = a+b
            resultados.append(suma)
            # print(f'Sumando: {suma}')
        elif i[1] == '-':
            resta = a-b
            resultados.append(resta)
            #print(f'Restando: {resta}')
        else:
            #arranged_problems = print(check2)
            return "Error: Operator must be '+' or '-'."
        longitud.append(max(len(i[0]), len(i[2])))
    # print(resultados)
    toditos = list(zip(primero, operador, segundo, resultados, longitud))
    conjunto(resultados)
    conjunto(longitud)

    reng1 = ""  # primer numero
    reng2 = ""  # simbolo mas segundo numero
    divisor = ""  # lineas horizontales
    reng3 = ""  # resultados
    for i in toditos:
        # componentes: (primero,operador, segundo,resultados,longitud)
        reng1 += "  " + i[0].rjust(i[4], relleno) + "    "
        reng2 += i[1] + " " + i[2].rjust(i[4], relleno) + "    "
        divisor += "-" * len("  " + i[0].rjust(i[4], relleno)) + "    "
        reng3 += str(i[3]).rjust(len("-" * len("  " + i[0].rjust(i[4], relleno))), relleno) + "    "
    if est == True:
        #arranged_problems = print(f'{reng1.rstrip()}\n{reng2.rstrip()}\n{divisor.rstrip()}\n{reng3.rstrip()}')
        return reng1.rstrip()+"\n"+reng2.rstrip()+"\n"+divisor.rstrip()+"\n"+reng3.rstrip()
    else:
        #arranged_problems = print(f'{reng1.rstrip()}\n{reng2.rstrip()}\n{divisor.rstrip()}')
        return reng1.rstrip() + "\n" + reng2.rstrip() + "\n" + divisor.rstrip()

arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
print("        ")
print("   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172")
